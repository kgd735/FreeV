# 每日新免费 VPN 检索 — 2026-11-23 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（Zori VPN）；无新增关停；YAML 由 42 条 → 43 条；页面同步已触发（artifact.edit 进行中），git 已推送（cd1a13b）**。

## 新增收录

1. **Zori VPN**（https://zorivpn.xyz，运营方 KYTTARA, LLC，美国拉斯维加斯）
   - 2026 年 11 月上架 Google Play（v1.0.3 于 11 月 4 日，v1.0.7 于 11 月 8 日）；安装量约 1.2 万（11 月 10 日）→ 约 7 万（11 月 20–22 日 AppBrain 各国新榜），评分 4.5–4.7 星。
   - 免费档：不限流量、不限速、不限会话时长；免注册、无需账号；无广告；无需信用卡。官网未提及付费档（截至 2026-11-23）。
   - 免费国家数未公开（可按国家/城市自选，默认自动选服）；协议未公开（自动选择，不可手动设置）；Android 8.0+（仅 ARM64）独占，暂无 iOS/桌面版。
   - 日志：VPN 活动无日志（不保留浏览记录、DNS 查询、流量内容、连接日志，含源/目的 IP 与连接时间）；应用分析与诊断默认开启且无应用内关闭开关；广告 ID 收集已停用、不卖数据；服务商为 Firebase + Cloudflare；无独立审计。
   - IP 类型：无家宽/住宅 IP 功能，机房 IP（推定），residential_ip: false。
   - 去重：entries、removed、discontinued 中均无此服务。
   - 来源：https://zorivpn.xyz/、https://zorivpn.xyz/en/privacy/、https://www.appbrain.com/app/zori-vpn-no-account-needed/com.zori.vpn、https://play.google.com/store/apps/details?id=com.zori.vpn

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库；ghacks / betanews / makeuseof / techno360 等多篇 11 月 21–23 日转载均为同一消息，无新变更。
2. GoVPN 2.0：已在库；官网博文（2026-11-16 更新）无新增变更。
3. Proton VPN Free：已在库；FrankVPN 2026-11-15 与 crashtestlover 2026-11-19 核查一致（不限量、1 台、10 国）。
4. Gizmodo 免费 VPN 榜单（2026-11-20 左右更新）：Proton / Windscribe / PrivadoVPN / hide.me / TunnelBear / Hotspot Shield 均已在库，免费档口径与库内一致，无变更。top10vpn / vpnoverview / vpnalert / savozi 榜单同理，均为已入库服务。
5. UnblockMeVPN：已在库；buildvoyage 2026-11-22 产品页为同一服务（免费洛杉矶节点、无卡），无新变更。
6. Atlas VPN：已在 discontinued（2024-04-24 关停）；2026-11-14/16 文章为旧闻回顾，无新增变更。
7. Samsung Max：已在 discontinued（2026-06-15 关停）；Toolradar 替代榜单无新增变更。
8. ClearVPN 免费档：官网支持页称 2024 年 3 月起取消免费档、仅留付费 Premium（3 天试用）。该变更发生在 2024 年，不在本次 24–48h 窗口内；ClearVPN 从未入库，是否记入 discontinued 交周检决定。
9. Surfshark 免费 Public DNS 将于 2026-11-24 关停（2026-11-20 宣布）：免费 DNS 服务，非 VPN 免费档；Surfshark 不在库内（无免费 VPN 档），不改库。
10. F-Secure FREEDOME VPN 逐步停用（Win/Mac 支持止于 2026-09-11，Android/iOS 止于 2027-03）：付费产品线合并，非免费档变更；FREEDOME 从未入库，不改库。
11. VPN Monster：acciyo 2026-11-22 文章称该服务似已停运（无明确停运日期、无官网/应用更新）。该服务从未入库、无免费档可考证据，不改库；列为周检候选观察。
12. VPN Gate 安卓客户端更新（2026-11-17/20）：仅常规版本更新，VPN Gate 条目已在库，无免费档变更。
13. VPN - Super Unlimited Proxy（v2.36.0，2026-11-03）：仅常规版本更新；官网 vpnsuper.com 已知，继续列为周检候选，本次不入库。
14. VPN Proxy Master（v2.7.8，2026-11-11/12）/ PandaVPN Lite（v10.1.0，2026-11-21/22）：仅常规版本更新，继续列为周检候选，暂不入库。
15. ZeroPing VPN（com.zero.ping.vpn，Star Core Studio）：v1.0.58 更新于 2026-11-16，免费广告支持路线、可选 Premium；本次检索仍未找到可核实的官网与隐私政策页（搜索结果混入无关的 "Zero" 隐私政策）。按既往标准（官网可核实前暂不入库），继续列为周检候选。
16. Anomi VPN（removed，2026-11-09）：本次复查——官网 anomivpn.com 仍无法访问（curl https:000），无服务恢复的有效证据。仍在 removed，不恢复入库。

## 同步

- YAML 已改动：node scripts/build.js 校验通过（43 entries，43 active，7 residential）；export-page-sync.js 已生成同步快照。
- Muse artifact 网页：artifact.edit 已触发（slug: mian-fei-vpn-shu-ju-ku），构建已完成并通过核实（页面 DATA 数组 43 条，Zori 卡片字段逐项取自 YAML；家宽 5 家确认 + 2 家部分、停服 6 条、移除 Anomi 1 条均一致）。**注意：构建成功但未自动发布——公开链接目前仍显示上一版（42 条），需用户批准新的 artifact.share 才会更新。**
- Git 仓库：sync.sh 已执行，提交 cd1a13b「更新数据库：新增 Zori VPN（2026-11-23，免费不限量、免注册，Android）」，已推送到 origin main（eadbbeb..cd1a13b）。
- 公开页面链接：https://muse.ai/s/mian-fei-vpn-shu-ju-ku-xhxd6xe0uxbxsp1n/524jt68zSApSIH5MC2nGlPSbeJuZFtOcaKCX54ZOr1s（待本次构建完成后显示 43 条版）

## 结论

- free-vpn-db.yaml：entries 42 → 43 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 6 条；家宽 IP 仍为 7 家。
- 有新增收录，按任务要求汇报：新增 Zori VPN（免费不限量、免注册、无广告，Android 独占），页面与仓库同步完成（页面构建待回执）。
- 下一次检索：明日 2026-11-24（free-vpn-db-daily-discovery）。
