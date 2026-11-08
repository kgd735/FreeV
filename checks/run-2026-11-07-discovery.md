# 每日新免费 VPN 检索 — 2026-11-07 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（Avast VPN Free）；现有条目小幅更新 1 处（X-VPN Talaria 协议）；无新关停记录**。

## 新增收录

### Avast VPN Free（2026-11-04 在法国推出永久免费档）
- 去重：库内无 Avast 条目；removed 为空；discontinued 无 Avast 记录。→ 可入库。
- 核实（2026-11-07）：
  - 官网：https://www.avast.com/fr-fr/free-vpn（实测可达，法语页；英语 /en-us、/en-gb、/en-in 免费页 2026-11-05 返回 404，来源 Techno360）
  - 免费档：不限量（官方法语页 FAQ；但另一版本产品页 FAQ 曾写 500 GB/月，数据上限存在冲突，待澄清）、自选 3 个地区（确认后永久锁定不可更换）、无限设备（不含智能电视）、需 Avast 账号（邮箱/Google/Apple）、无需信用卡
  - 协议：WireGuard（免费档）；kill switch 有；OpenVPN/Mimic、分流、Double VPN 为付费档
  - IP 类型：机房 IP（residential_ip: false）
  - 日志/审计：无日志声称；无已发布独立审计——Frandroid 称 Avast 已委托 VerSprite 每年审计无日志政策，首份报告预计 2026-11；FTC 2024-06 令：因通过 Jumpshot 出售浏览数据罚 1650 万美元并禁止出售数据；捷克（母公司 Gen Digital，美国）
  - 平台：Windows/macOS/Android/iOS（经 Avast One 应用；无 Linux）
  - 限制：印度不可用（CERT-In 2022 规则）；此前免费形态仅为 60 天试用或 Avast One 内 5GB/周 VPN
  - 来源：官网 + https://techno360.in/avast-free-vpn-review-india-blocked/（2026-11-05 实测评测，Frandroid 2026-11-04 首报）
- 变更：YAML entries 28 → 29（id: avast-vpn-free，last_verified 2026-11-07）；README.md 计数与速览表同步更新。

## 现有条目更新

- X-VPN：新增 Talaria 自研协议（AGPLv3 开源，免费与付费用户均可用，Win/macOS/iOS/Android），来源 X-VPN 官方 YouTube（https://www.youtube.com/watch?v=4eQ08byBkPo）。仅 protocols 与 change_log 补充，免费档本身无变化；last_verified 未改动（仍 2026-11-04）。

## 检查到的候选（均排除）

1. Firefox 免费内置 VPN（windowsforum 2026-11-04、CNET 2026-11-03 综述）：
   服务本身为 Mozilla 2026-03（Firefox 149 beta）推出的 50GB/月浏览器代理；本次报道仅为综述，无 24–48h 内实质变更。
   → 按 2026-11-05、2026-11-06 两次运行的既有决定，本次不收录，仍为下次大复核候选。
2. EVPN（evpn.com，免费 VPN，iOS TestFlight 分发，当前 9 国 10 城，目标 33 国 100 城）：
   无日志政策/审计/运营主体信息，应用仅 TestFlight，未达收录核实标准。→ 不收录，列入监控候选。
3. 新 Android 免费 VPN 应用（AppBrain 检索）：ROJA VPN（2026-10 上线）、ZapSplit VPN（2026-10 上线，免费不限量 4Mbps）、
   Skyvora VPN（2026-09 上线）、Surge Proxy（2025-05 上线）——均无官网/日志政策/协议说明，或上线时间在窗口之外。→ 均不收录。
4. LetsVPN 在中国停服（letsvpnshutdown.com，2026 年）：
   为付费服务，从未进入本库 entries/discontinued，按 Cryptostorm 惯例不记入 discontinued。→ 不作变更。
5. F-Secure FREEDOME 分阶段停服（Win/Mac 支持至 2026-09-11，Android/iOS 至 2027-03）：
   试用型产品、无永久免费档，从未在库中。→ 不作变更。
6. Problembo "VPN Access is being discontinued"（2026-11-01/02）：
   Telegram 机器人售卖的付费 VPN 接入，非免费档，且不在库中；公告时间在窗口之外。→ 不作变更。
7. Samsung Max（2026-06-15 关停）、Atlas VPN（2024-04-24 关停）、Google One VPN（2024-06 关停）：
   均已在 discontinued。→ 不作变更。

## 结论

- free-vpn-db.yaml：28 → 29 条 entries；removed 仍为空；discontinued 仍为 4 条。
- README.md：计数 28→29，新增 Avast 速览行。
- 下一次检索：明日 2026-11-08（free-vpn-db-daily-discovery）。
- 大复核候选：Firefox 免费内置 VPN、SingLinkVPN、VPN OkayFreedom（Steganos）、EVPN。
- 待澄清：Avast 免费档数据上限（不限量 vs 500GB/月）与 VerSprite 首份审计报告（预计 2026-11），留待每周复核跟进。
