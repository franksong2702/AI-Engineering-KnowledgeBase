#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Engineering Knowledge Base · 一键体检脚本（P2-5）
用法：python3 kb_health_check.py [KB根目录，默认为脚本上级目录]

检查项：
  1. wikilink 断链（支持普通 alias 与表格内 \\| 转义，排除代码段）
  2. wikilink 歧义（同名多文件）
  3. 所有 wikilink heading 必须精确存在（不只检查 Laws / ADS）
  4. Markdown table 中未转义的 wikilink alias pipe
  5. Laws wikilink alias/heading 语义一致性（`Law N：标题` 与 `#Law N — ...` 必须匹配真实 Law 标题和 family 文件）
  6. 已启用 Laws metadata schema 的 family 字段完整性
  7. frontmatter：存在性、abstraction_layer 覆盖、INDEX aliases
  8. 决策系统 ID 引用一致性（LAW/ANTI 标注与有限的近邻短语比对）
  9. ADS Markdown 与 `_machine/*.yaml` 编译结果必须同步
  10. ADS ↔ Case Library cross-reference guard（防裸 ID、文件级回退、heading 失效）
  11. 自描述数字（书数/文件数）与实际比对
  12. 环境泄漏关键词（生成模型工作环境的 skill 名等）
退出码：0=全部通过，1=有失败项。
"""
import os, re, sys, collections, subprocess

KB = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUDE = ('FABLE5',)  # 审阅文档不参与体检
BOOK_COUNT_EXPECT = 15  # 书目数（不含案例库/决策系统/图谱层）
LAW_METADATA_ENABLED = {
    'laws-of-ai-engineering/01_信息与压缩定律.md',
    'laws-of-ai-engineering/02_计算与验证定律.md',
    'laws-of-ai-engineering/03_统计与泛化定律.md',
    'laws-of-ai-engineering/04_系统与控制定律.md',
    'laws-of-ai-engineering/05_接口与边界定律.md',
    'laws-of-ai-engineering/06_经济与资源定律.md',
    'laws-of-ai-engineering/07_认识论与真理定律.md',
    'laws-of-ai-engineering/08_可靠性与失败定律.md',
    'laws-of-ai-engineering/09_人机与信任定律.md',
    'laws-of-ai-engineering/10_对抗与安全定律.md',
    'laws-of-ai-engineering/11_演化与元定律.md',
}
LAW_METADATA_FIELDS = ['定律性质', '引用层级', '引用范围', '关系说明']
LAW_METADATA_TIERS = ('核心级', '家族级', '场景级')
FAIL = 0

def say(ok, label, detail=''):
    global FAIL
    mark = '✅' if ok else '❌'
    if not ok: FAIL = 1
    print(f"{mark} {label}" + (f" — {detail}" if detail else ''))

files = []
for root, dirs, fs in os.walk(KB):
    dirs[:] = [
        d for d in dirs
        if not d.startswith('.') and d not in {'_tools', '_machine', '__pycache__'}
    ]
    for f in fs:
        if f.endswith('.md') and not any(x in f for x in EXCLUDE):
            files.append(os.path.relpath(os.path.join(root, f), KB))

def read(p): return open(os.path.join(KB, p), encoding='utf-8').read()
def strip_code(t):
    t = re.sub(r'```.*?```', '', t, flags=re.S)
    return re.sub(r'`[^`\n]*`', '', t)

# ---- 1/2 链接 ----
base_map = collections.defaultdict(list)
for f in files: base_map[os.path.splitext(os.path.basename(f))[0]].append(f)

# Accept both historical KB-root-relative links and Obsidian vault-root-relative links.
# The vault path is stable for this KB: <vault>/02_Learn/05_AI_Lessons/AI-Engineering-KnowledgeBase.
VAULT = os.path.abspath(os.path.join(KB, '..', '..', '..'))
path_set = set()
target_to_file = {}
for f in files:
    kb_rel = os.path.splitext(f)[0].replace(os.sep, '/')
    path_set.add(kb_rel)
    target_to_file[kb_rel] = f
    abs_f = os.path.join(KB, f)
    vault_rel = os.path.splitext(os.path.relpath(abs_f, VAULT))[0].replace(os.sep, '/')
    path_set.add(vault_rel)
    target_to_file[vault_rel] = f
link_re = re.compile(r'\[\[([^\]]+)\]\]')

def has_unescaped_pipe(s):
    """Return True if a wikilink body contains an unescaped alias separator pipe."""
    escaped = False
    for ch in s:
        if escaped:
            escaped = False
            continue
        if ch == '\\':
            escaped = True
            continue
        if ch == '|':
            return True
    return False

def split_wikilink_ref(inner):
    """Return (target_without_heading, heading, alias) from [[target#heading|alias]] or table-safe [[target#heading\\|alias]]."""
    # In Markdown tables Obsidian-safe aliases are written as [[target\|alias]].
    # Treat both | and \| as alias separators for validation purposes.
    alias_at = None
    alias_sep_len = 1
    i = 0
    while i < len(inner):
        if inner[i] == '\\' and i + 1 < len(inner) and inner[i + 1] == '|':
            alias_at = i
            alias_sep_len = 2
            break
        if inner[i] == '|':
            alias_at = i
            alias_sep_len = 1
            break
        i += 1
    before_alias = inner if alias_at is None else inner[:alias_at]
    alias = None if alias_at is None else inner[alias_at + alias_sep_len:].strip()
    if '#' in before_alias:
        target_part, heading = before_alias.split('#', 1)
        heading = heading.strip()
    else:
        target_part, heading = before_alias, None
    target = target_part.strip().rstrip('\\')
    return target, heading, alias

def split_wikilink_parts(inner):
    """Return (target_without_heading, alias) from [[target|alias]] or table-safe [[target\\|alias]]."""
    target, _heading, alias = split_wikilink_ref(inner)
    return target, alias

def split_wikilink_target(inner):
    return split_wikilink_ref(inner)[0]

heading_map = {
    f: set(re.findall(r'^#{1,6}\s+(.+?)\s*$', strip_code(read(f)), flags=re.M))
    for f in files
}

broken, amb, broken_heading, table_pipe = [], [], [], []
for f in files:
    t = strip_code(read(f))
    for i, line in enumerate(t.splitlines(), 1):
        is_table = line.lstrip().startswith('|')
        for m in link_re.finditer(line):
            inner = m.group(1)
            if is_table and has_unescaped_pipe(inner):
                table_pipe.append(f"{f}:{i} {m.group(0)[:80]}")
            tg, heading, _alias = split_wikilink_ref(inner)
            resolved = f if not tg else None
            if '/' in tg:
                if tg not in path_set:
                    broken.append((f, m.group(0)[:80]))
                else:
                    resolved = target_to_file[tg]
            else:
                if tg:
                    r = base_map.get(tg)
                    if not r:
                        broken.append((f, m.group(0)[:80]))
                    elif len(r) > 1:
                        amb.append((f, tg))
                    else:
                        resolved = r[0]
            if heading and not heading.startswith('^') and resolved and heading not in heading_map[resolved]:
                broken_heading.append(f"{f}:{i} {m.group(0)[:100]} -> {resolved}#{heading}")
say(not broken, f"断链检查（{len(broken)} 处）", '; '.join(f"{a}:{b}" for a, b in broken[:5]))
say(not amb, f"歧义链接检查（{len(amb)} 处）", '; '.join(f"{a}:[[{b}]]" for a, b in amb[:5]))
say(not broken_heading, f"通用 wikilink heading 精确匹配（异常 {len(broken_heading)}）", '; '.join(broken_heading[:5]))
say(not table_pipe, f"表格内未转义 wikilink alias pipe（{len(table_pipe)} 处）", '; '.join(table_pipe[:5]))

# ---- 3 Laws wikilink alias/heading 语义一致性 ----
law_titles = {}
law_headings = {}
law_targets = collections.defaultdict(set)
law_file_targets = {}
law_family_basenames = set()
for f in files:
    if not re.match(r'laws-of-ai-engineering/(?:0[1-9]|1[01])_', f):
        continue
    base = os.path.splitext(os.path.basename(f))[0]
    law_family_basenames.add(base)
    kb_rel = os.path.splitext(f)[0].replace(os.sep, '/')
    abs_f = os.path.join(KB, f)
    vault_rel = os.path.splitext(os.path.relpath(abs_f, VAULT))[0].replace(os.sep, '/')
    targets_for_file = {kb_rel, base, vault_rel}
    law_file_targets[f] = targets_for_file
    t = read(f)
    for m in re.finditer(r'^## (Law (\d+) — (.+?)(?:（|\(|$).*)$', t, re.M):
        full_heading = m.group(1).strip()
        n = int(m.group(2))
        title = m.group(3).strip()
        law_titles[n] = title
        law_headings[n] = full_heading
        law_targets[n].update(targets_for_file)

law_alias_errors = []
law_alias_re = re.compile(r'Law\s*(\d{1,3})\s*[：:]\s*([^|，,。；;）)]+)')
law_heading_re = re.compile(r'^Law\s*(\d{1,3})\s+—\s+(.+)$')

def law_target_matches(n, target, current_file_targets):
    if target:
        return target in law_targets[n]
    return bool(current_file_targets & law_targets[n])

def law_target_display(n):
    candidates = sorted(t for t in law_targets[n] if t.startswith('laws-of-ai-engineering/'))
    return candidates[0] if candidates else sorted(law_targets[n])[0]

for f in files:
    t = strip_code(read(f))
    current_file_targets = law_file_targets.get(f, set())
    for i, line in enumerate(t.splitlines(), 1):
        for m in link_re.finditer(line):
            target, heading, alias = split_wikilink_ref(m.group(1))
            target_base = os.path.basename(target)
            is_laws_target = bool((not target and current_file_targets) or ('laws-of-ai-engineering/' in target) or (target_base in law_family_basenames))
            if not is_laws_target:
                continue
            alias_law_n = None
            if alias:
                am = law_alias_re.search(alias)
                if am:
                    n = int(am.group(1))
                    alias_law_n = n
                    alias_title = am.group(2).strip()
                    true_title = law_titles.get(n)
                    if not true_title:
                        law_alias_errors.append(f"{f}:{i} Law {n} 不存在: {m.group(0)[:80]}")
                        continue
                    if alias_title != true_title:
                        law_alias_errors.append(f"{f}:{i} Law {n} 标题应为「{true_title}」但写成「{alias_title}」")
                    if not law_target_matches(n, target, current_file_targets):
                        law_alias_errors.append(f"{f}:{i} Law {n} 目标文件应为 {law_target_display(n)} 但链接到 {target or '当前文件'}")
                    if heading:
                        true_heading = law_headings.get(n)
                        if heading != true_heading:
                            law_alias_errors.append(f"{f}:{i} Law {n} heading 应为「{true_heading}」但写成「{heading}」")
            hm = law_heading_re.match(heading or '')
            if hm and int(hm.group(1)) != alias_law_n:
                n = int(hm.group(1))
                true_heading = law_headings.get(n)
                if not true_heading:
                    law_alias_errors.append(f"{f}:{i} Law {n} 不存在: {m.group(0)[:80]}")
                    continue
                if heading != true_heading:
                    law_alias_errors.append(f"{f}:{i} Law {n} heading 应为「{true_heading}」但写成「{heading}」")
                if not law_target_matches(n, target, current_file_targets):
                    law_alias_errors.append(f"{f}:{i} Law {n} 目标文件应为 {law_target_display(n)} 但链接到 {target or '当前文件'}")
say(not law_alias_errors, f"Laws wikilink alias/heading 语义一致性（异常 {len(law_alias_errors)}）", '; '.join(law_alias_errors[:5]))

# ---- 4 Laws metadata schema ----
metadata_errors = []
for f in sorted(LAW_METADATA_ENABLED):
    if f not in files:
        metadata_errors.append(f"{f}: 已启用 schema 但文件不存在")
        continue
    sections = re.split(r'(?=^## Law \d+ — )', read(f), flags=re.M)
    law_sections = [s for s in sections if s.startswith('## Law ')]
    if not law_sections:
        metadata_errors.append(f"{f}: 未找到 Law 标题")
        continue
    for s in law_sections:
        m = re.match(r'## Law (\d+) —', s)
        law_id = f"Law {m.group(1)}" if m else "未知 Law"
        callout_count = s.count('> [!metadata] 定律元信息')
        if callout_count != 1:
            metadata_errors.append(f"{f}:{law_id} metadata callout={callout_count}")
        for field in LAW_METADATA_FIELDS:
            c = s.count(f'`{field}`:')
            if c != 1:
                metadata_errors.append(f"{f}:{law_id} `{field}`={c}")
        if '`正典范围`:' in s:
            metadata_errors.append(f"{f}:{law_id} 仍使用旧字段 `正典范围`")
        tier_match = re.search(r'> - `引用层级`:\s*(.+)', s)
        if tier_match and not tier_match.group(1).strip().startswith(LAW_METADATA_TIERS):
            metadata_errors.append(f"{f}:{law_id} 引用层级不在 核心级/家族级/场景级")
say(not metadata_errors, f"Laws 元信息 schema（异常 {len(metadata_errors)}）", '; '.join(metadata_errors[:5]))

# ---- 4 frontmatter ----
no_fm, no_layer, no_alias = [], [], []
for f in files:
    t = read(f)
    parts = t.split('---')
    if not t.startswith('---') or len(parts) < 3: no_fm.append(f); continue
    if 'abstraction_layer' not in parts[1]: no_layer.append(f)
    if (os.path.basename(f) in ('00_INDEX.md', '00_PROTOCOL.md')) and 'aliases:' not in parts[1]: no_alias.append(f)
say(not no_fm, f"frontmatter 存在性（缺 {len(no_fm)}）", ', '.join(no_fm[:5]))
say(not no_layer, f"abstraction_layer 覆盖（缺 {len(no_layer)}）", ', '.join(no_layer[:5]))
say(not no_alias, f"INDEX aliases（缺 {len(no_alias)}）", ', '.join(no_alias[:5]))

# ---- 5 决策系统 ID 一致性 ----
canon_file = os.path.join(KB, 'agent-decision-system', '04_LAW-INVARIANTS.md')
det_file = os.path.join(KB, 'agent-decision-system', '03_ANTIPATTERN-DETECTORS.md')
canon = {}
for path in (canon_file, det_file):
    if os.path.exists(path):
        for m in re.finditer(r'^## ((?:LAW|ANTI)-\d{2}) · (.+?)（', open(path, encoding='utf-8').read(), re.M):
            canon[m.group(1)] = m.group(2)
KEYS = {'LAW-01': ['验证'], 'LAW-02': ['参数', '事实', '来源', '幻觉', '证据'], 'LAW-03': ['分布', '校准'],
 'LAW-04': ['古德哈特', '指标', '对齐'], 'LAW-05': ['指令', '权限', '注入', '三重奏', '安全', '攻击面'],
 'LAW-06': ['误差', '累积', '恢复', '检查点', '失败'], 'LAW-07': ['上下文', '状态'],
 'LAW-08': ['信任', '可靠性'], 'LAW-09': ['可逆', '后果', '恢复', '风险', '审慎', '审批'], 'LAW-10': ['简单', '规模不经济', '用对工具', '机会成本', '边际'],
 'LAW-11': ['确定性'], 'LAW-12': ['判断', '责任', '委托'], 'LAW-13': ['信息守恒', '垃圾', '数据质量'],
 'ANTI-01': ['静默'], 'ANTI-02': ['信任'], 'ANTI-03': ['刷分', '分数', '古德哈特', 'enchmark'],
 'ANTI-04': ['自动化', '自主性错配'], 'ANTI-05': ['评测', 'ibe', '评估'], 'ANTI-06': ['Agent', '过度设计', '单体'],
 'ANTI-07': ['多 Agent', '多Agent'], 'ANTI-08': ['记忆', '倾倒', '污染', '历史'], 'ANTI-09': ['反思'],
 'ANTI-10': ['盲信'], 'ANTI-11': ['谄媚', '长期', '满意'], 'ANTI-12': ['恢复', '循环', '出口', '幂等', '重试']}
idpat = re.compile(r'((?:LAW|ANTI)-\d{2})\s*[(（]([^)）]{1,60})[)）]')
reverse_law_label_re = re.compile(r'([A-Za-z0-9\u4e00-\u9fff+>\-]{2,16})\s*[(（](LAW-\d{2})[)）]')
REVERSE_LAW_LABELS = {
    '纯推理会编': {'LAW-02', 'LAW-13'},
    '模型不知': {'LAW-02', 'LAW-13'},
    '不可逆': {'LAW-09'},
}
bad_ids = []
for f in files:
    if not (f.startswith('agent-decision-system') or f.startswith('ai-engineering-case-library')): continue
    for i, line in enumerate(read(f).splitlines(), 1):
        for m in idpat.finditer(line):
            idt, note = m.group(1), m.group(2)
            if idt in KEYS and not any(k in note for k in KEYS[idt]):
                bad_ids.append(f"{f}:{i} {idt}({note[:25]})")
        for m in reverse_law_label_re.finditer(line):
            note, idt = m.group(1), m.group(2)
            allowed = REVERSE_LAW_LABELS.get(note)
            if allowed is not None and idt not in allowed:
                bad_ids.append(f"{f}:{i} {note}({idt}) 应指向 {sorted(allowed)}")
say(not bad_ids, f"决策系统 ID 标注一致性（异常 {len(bad_ids)}）", '; '.join(bad_ids[:5]))

# ---- 6 ADS Markdown ↔ machine YAML 同步 ----
compiler_script = os.path.join(KB, '_tools', 'compile_decision_system.py')
if os.path.exists(compiler_script):
    proc = subprocess.run(
        [sys.executable, compiler_script, '--check', KB],
        capture_output=True,
        text=True,
        check=False,
    )
    compiler_output = (proc.stdout or '') + (proc.stderr or '')
    compiler_lines = [line for line in compiler_output.splitlines() if line.strip()]
    say(proc.returncode == 0, 'ADS Markdown ↔ machine YAML 同步', '; '.join(compiler_lines[:5]))
else:
    say(False, 'ADS Markdown ↔ machine YAML 同步', '_tools/compile_decision_system.py 不存在')

# ---- 7 ADS ↔ Case Library cross-reference guard ----
crossref_script = os.path.join(KB, '_tools', 'check_ads_case_crossrefs.py')
crossref_detail = ''
if os.path.exists(crossref_script):
    proc = subprocess.run(
        [sys.executable, crossref_script, KB],
        capture_output=True,
        text=True,
        check=False,
    )
    crossref_output = (proc.stdout or '') + (proc.stderr or '')
    if proc.returncode == 0:
        summary_lines = [
            line for line in crossref_output.splitlines()
            if line.startswith('summary_') or 'heading 级具体 ID 链接' in line or '可直达案例入口' in line
        ]
        crossref_detail = '; '.join(summary_lines[:4])
    else:
        failure_lines = [
            line for line in crossref_output.splitlines()
            if line.startswith('❌') or line.startswith('- ')
        ]
        crossref_detail = '; '.join(failure_lines[:5]) or crossref_output.strip()[:300]
    say(proc.returncode == 0, 'ADS ↔ Case Library cross-reference guard', crossref_detail)
else:
    say(False, 'ADS ↔ Case Library cross-reference guard', '_tools/check_ads_case_crossrefs.py 不存在')

# ---- 6 自描述数字 ----
readme = read('README.md') if 'README.md' in files else ''
m = re.search(r'十(.)本书[^，]*，(\d+) 个文件', readme)
issues = []
if m:
    n_claim = {'二': 12, '一': 11, '三': 13, '四': 14, '五': 15}.get(m.group(1))
    if n_claim != BOOK_COUNT_EXPECT: issues.append(f"README 书数 {n_claim} ≠ 预期 {BOOK_COUNT_EXPECT}")
    if int(m.group(2)) != len(files): issues.append(f"README 文件数 {m.group(2)} ≠ 实际 {len(files)}")
else:
    issues.append('README 未找到自描述句')
for kw in ['102 个文件', '102 文件', '十一本书', '11 本书', '共十一本', '十二本书', '131 个文件', '共十二本', '12 本书', '十三本书', '共十三本', '13 本书', '147 文件', '150 个文件', '十四本书', '共十四本', '171 个文件']:
    hits = [f for f in files if kw in read(f)]
    if hits: issues.append(f"过时口径 '{kw}' 残留于 {hits[:3]}")
say(not issues, f"自描述一致性（实际 {len(files)} 个 md 文件）", '; '.join(issues))

# ---- 6b Laws 裸锚跨文件 ----
import glob as _glob
_bad_anchors = []
for _f in [f for f in files if f.startswith('laws-of-ai-engineering/') and re.match(r'laws-of-ai-engineering/\\d{2}_', f)]:
    _t = strip_code(read(_f))
    _own = set(int(m) for m in re.findall(r'^## Law (\\d+) — ', _t, re.M))
    for _m in re.finditer(r'\\[\\[#Law (\\d+)', _t):
        if int(_m.group(1)) not in _own:
            _bad_anchors.append(f"{_f}: [[#Law {_m.group(1)}")
say(not _bad_anchors, f"Laws 裸锚跨文件（{len(_bad_anchors)} 处）", '; '.join(_bad_anchors[:5]))

# ---- 7 环境泄漏 ----
LEAK = ['user_wellbeing', 'product-management:', '[[docx', '[[skill-creator', '[[wikilink']
leaks = [(f, kw) for f in files for kw in LEAK if kw in read(f)]
say(not leaks, f"环境泄漏关键词（{len(leaks)} 处）", '; '.join(f"{a}:{b}" for a, b in leaks[:5]))

print('\n' + ('体检通过 ✅' if not FAIL else '存在失败项 ❌'))
sys.exit(FAIL)
