# HANDOFF — One Word, One Username, One Reward

- 比赛：`u-rusdyxbt-one-word-one-username-one-reward-1a191fae`（$5，截止北京时间 2026-11-27 07:50）
- 文案（用户亲口原话，一字不改）：`bingxi-xiang`
- 做法：`main.py` 把文案常量直接写到 `/output/entry.txt`，UTF-8、无尾随换行、不读外部文件、不联网。第一次写完整版并跑通；第二次做了真正的改进——写完后把文件读回来，和 ENTRY 逐字比对，不一致就报错退出（exit 1）。
- 字符数：12 字符 / 12 字节（ASCII），在 1–30 字符上限内，单字无空格。
- 校验结果：
  - 第一次运行（v1）：exit 0，输出 `bingxi-xiang`，12 字节。
  - 第二次改进后连续两次运行：exit 0、exit 0，两次输出 `cmp` 逐字节一致。
  - entry.txt 与 `prompt.txt` `cmp` 完全一致，与文案 exact match。
  - sha256（两次运行相同）：`ee50ea528fb80fbae56da5b106314645872788aad87a4e6b93e627ecb0724348`
- 文件：`main.py`、`LICENSE`（MIT，含 SPDX 行）、`README.md`（含比赛页链接与三枚官方徽章）、`prompt.txt`、`HANDOFF.md`、`.makefun/owner.json`（钱包 `6t8k8dD19c2zDMiZ1VNsbRDWaSNSedmQQB6A15hy3XFx`）。
- 未做：未提交、未建 GitHub 仓、未碰 bundle。
