# 每日新免费 VPN 检索 — 2026-11-24 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（CasperVPN）；无新增关停；YAML 由 43 条 → 44 条；页面同步已触发（artifact.edit 进行中，待构建回执核实），git 已推送（aa2e9b9）**。

## 新增收录

1. **CasperVPN**（https://caspervpn.com，运营方 App-Link Offshore S.A.L.，黎巴嫩贝鲁特，商业注册号 1808496）
   - 2026 年 11 月 23 日 Android 版上架 Google Play（iOS/iPadOS 版自 2018 年起已有）；桌面版（Mac/Windows/Linux）、Apple TV、Android TV 与浏览器扩展计划 2027 年初推出。
   - 免费档：0.5 GB/月，3 个服务器节点（未公开具体国家），无需信用卡、无需账号即可开始（设备账号；邮箱可选），每账号最多同时 3 台设备；Premium 9.99 美元/月起，订阅享 7 天试用。
   - 协议：WireGuard、OpenVPN（UDP/TCP）、IKEv2/IPSec、自研 CasperCloak；kill switch 与 Double VPN 为 Premium 功能（公司博客口径）。
   - 日志：宣称无活动日志（不存浏览活动、连接目的地、DNS 查询；自 2026 年 3 月起连接记录中不再含源 IP 与分配的 VPN IP）；但保留最小连接元数据（连接时间戳、所选服务器、协议、流量、设备标识符）；无独立审计。隐私政策 v1.12（2026-11-13 更新）已核实。
   - IP 类型：无家宽/住宅 IP 功能，机房 IP（推定），residential_ip: false。
   - 去重：entries、removed、discontinued 中均无此服务。
   - 来源：https://tbreak.com/casper-vpn-android-google-play/、https://caspervpn.com/privacy、https://caspervpn.com/blog/what-is-a-vpn-how-does-it-work、https://apps.apple.com/us/app/caspervpn-wifi-security-vpn/id1187243615

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库；Mozilla Connect 帖子（1 天前）与 ghacks/betanews 等转载均为同一消息，无新变更。（注：Connect 帖子称起始日为 11 月 9 日，Mozilla 博客与多家报道为 11 月 10 日，1 天口径差异，不改库。）
2. GoVPN 2.0（2026-11-17 博文）：已在库；免费档不变，无变更。
3. Proton VPN Free：已在库；crashtestlover 2026-11-19 与 activepieces 2026-11-20 核查一致（不限量、1 台、10 国），无变更。
4. PrivadoVPN Free：已在库；vpnclue 2026-11-23 核查一致（10GB/30 天、13 城 10 国、邮箱验证），无变更。
5. UnblockMeVPN：已在库；buildvoyage 产品页为同一服务，无新变更。
6. Surfshark 免费 Public DNS 将于 2026-11-24 关停（2026-11-20 宣布）：免费 DNS 服务，非 VPN 免费档；Surfshark 不在库内（无免费 VPN 档），不改库。
7. Samsung Max：已在 discontinued（2026-06-15 关停）；11 月 18 日更新称 One UI 9 开始移除该应用，仅为清理残留，无新增变更。
8. Atlas VPN：已在 discontinued（2024-04-24 关停）；11 月 14/16 日文章为旧闻回顾，无新增变更。
9. ZenMate：2023 年并入 CyberGhost，付费应用已停；官网仍链接免费浏览器扩展。CyberGhost 免费浏览器扩展已在库；ZenMate 不再是独立免费 VPN 服务，不另入库。
10. F-Secure FREEDOME VPN 逐步停用（Win/Mac 支持止于 2026-09-11，Android/iOS 止于 2027-03）：付费产品线合并，非免费档变更；FREEDOME 从未入库，不改库。
11. VPN Monster：acciyo 2026-11-22 文章称该服务似已停运（无明确停运日期、无官网/应用更新）。该服务从未入库、无免费档可考证据，不改库；继续列为周检候选观察。
12. BBVPN – Super Unlimited VPN（bbvpn.net，开发者 Bohdan Borkovych，乌克兰）：免费不限量、免注册、60+ 国，Premium 仅去广告；官网与隐私政策可核实。但该应用至少自 2020 年起已存在（ProPrivacy 旧报告曾检出 IPv6 泄漏），本次 24–48h 窗口内无新上线/免费档变更证据，仅为搜索新发现的旧服务，本次不入库；列为周检候选，由周检评估是否纳入。
13. Free VPN by Free VPN .org（freevpn.org，Free VPN, LLC）：免费不限量、广告支持、免注册，官网可核实；但同样为多年老服务，本次窗口内无新信息，不入库；列为周检候选。
14. VPN – Super Unlimited Proxy（vpnsuper.com）：v2.37.0 于 2026-11-23 左右发布，仅常规版本更新，无免费档变更；继续列为周检候选。
15. VibeVPN（vibevpn.me，TurboByte LTD）：iOS VPN，2026-11-11 上线 Product Hunt，「免费开始」但未找到可核实的免费档额度/国家数明细；上线已 13 天，不在本次 24–48h 窗口内，本次不入库；列为周检候选。
16. iTop VPN 8.2.0：免费档 16 台服务器、700MB/天；老服务，仅版本更新，无免费档变更，不入库。
17. VPN Proxy Master（v2.7.8）/ PandaVPN Lite（v10.1.0）：仅常规版本更新，继续列为周检候选，暂不入库。
18. ZeroPing VPN：本次检索仍未找到可核实的官网与隐私政策页，按既往标准暂不入库，继续列为周检候选。
19. Anomi VPN（removed，2026-11-09）：本次复查——官网 anomivpn.com 仍无法访问，无服务恢复的有效证据。仍在 removed，不恢复入库。
20. hide.me Free：Gizmodo 2026-11-19 榜单称免费 7 国 8 地，与库内 8 地口径一致，无变更。
21. OpenTheRank「Best Free VPNs 2026」（2026-11-23 更新，22 条）：所列均为已入库服务（Proton/Windscribe/hide.me/PrivadoVPN/TunnelBear/Calyx/Riseup/Planet VPN/AdGuard/VPN Super/WARP/Psiphon/Speedify 等）或长期免费档（Browsec、AdGuard、Bitdefender 200MB/天），无新服务、无免费档变更；AdGuard VPN Free、Bitdefender 免费档、Browsec Free、iTop VPN 列为周检候选评估。

## 同步

- YAML 已改动：node scripts/build.js 校验通过（44 entries，44 active，7 residential）；export-page-sync.js 已生成同步快照。
- Muse artifact 网页：artifact.edit 已完成并通过核实（构建回执 2026-11-24 02:53 UTC）：页面 DATA 数组 44 条，CasperVPN 卡片字段逐项取自 YAML；家宽确认 5 家 + 部分 2 家、停服 6 条、移除 Anomi 1 条均一致。**注意：构建成功但未自动发布——公开链接目前仍显示上一版（43 条），需用户批准新的 artifact.share 才会更新。**
- Git 仓库：sync.sh 已执行，提交 aa2e9b9「更新数据库：新增 CasperVPN（2026-11-24，免费 0.5GB/月、3 个节点、免注册，iOS/Android）」，已推送到 origin main（ee7d4e1..aa2e9b9）。
- 公开页面链接：https://muse.ai/s/mian-fei-vpn-shu-ju-ku-xhxd6xe0uxbxsp1n/524jt68zSApSIH5MC2nGlPSbeJuZFtOcaKCX54ZOr1s（待本次构建完成后显示 44 条版；注：上一轮构建成功后公开链接仍显示旧版，需用户批准新的 artifact.share 才会更新，本轮同理）

## 结论

- free-vpn-db.yaml：entries 43 → 44 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 6 条；家宽 IP 仍为 7 家。
- 有新增收录，按任务要求汇报：新增 CasperVPN（免费 0.5GB/月、3 个节点、无需信用卡与账号，iOS/Android），页面与仓库同步完成（页面构建已核实 44 条；公开链接仍显示 43 条旧版，需用户批准新的 artifact.share 才会更新）。
- 下一次检索：明日 2026-11-25（free-vpn-db-daily-discovery）。
