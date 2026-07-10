## What changed

-

## Change type

- [ ] Knowledge content / book chapter
- [ ] Governance / audit / maintenance docs
- [ ] Tooling / validation scripts
- [ ] ADS / Case Library cross-reference
- [ ] Law reference / citation system
- [ ] Other:

## Canonical-layer risk

- [ ] Does not touch canonical definitions
- [ ] Touches Constitution / Laws / ADS invariants / ADS anti-pattern detectors
- [ ] Unsure, reviewer should check

## Validation

Paste exact commands and key output:

```text
验证命令:
返回结果:
证据路径:
```

## Obsidian compatibility checklist

- [ ] 正文 Wiki-links 未被批量转换；公共导航页使用双兼容的相对 Markdown 链接
- [ ] README / 总图 / 学习路径 / 使用路径中的相对链接已通过体检
- [ ] No broad directory rename or file move unless this PR is explicitly about that
- [ ] If file counts changed, README / graph self-description was updated
- [ ] If ADS changed, `_tools/compile_decision_system.py` was run
- [ ] If ADS ↔ Case Library routes changed, `_tools/check_ads_case_crossrefs.py` was run
