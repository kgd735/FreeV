# 每日新免费 VPN 检索 — 2026-11-25 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（XXLink Free VPN）；无新增关停；YAML 由 44 条 → 45 条；页面同步已触发（artifact.edit 进行中，待构建回执核实），git 已推送（ad1a93c）**。

## 新增收录

1. **XXLink Free VPN**（https://xxlink.net，运营方/管辖地未披露）
   - 官网于 2026-11-22 发布（Windows 客户端页标注 Published: 2026-11-22）；本次检索新发现，此前各轮未提及。
   - 免费档：1 GB / 7 天，速度上限 10 Mbps，免费线路；需创建账号（邮箱；未验证且无活动的账号 24 小时后自动删除），无需信用卡。
   - 地区：官网列出 6 个地区（东京、新加坡、香港、洛杉矶、法兰克福、都柏林），免费线路是否覆盖全部未明确说明。
   - 协议：官网未披露；平台：Windows、Android（v1.1.1）。
   - 日志：**非无日志**——隐私政策异常透明：服务器日志保留 IP 地址且无固定过期时间；用量记录（流量、时间、地区）90 天后删除；滥用调查功能（可记录连接目标地址/端口/协议+账号）目前已关闭，但 2026-08-22 之前曾记录连接目标+账号标识；不卖个人信息；无独立审计。
   - IP 类型：无家宽/住宅 IP 功能，机房 IP（推定），residential_ip: false。
   - 去重：entries、removed、discontinued 中均无此服务。
   - 来源：https://xxlink.net/、https://xxlink.net/privacy

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库；sawahits（2026-11-24）等新转载均为同一消息，无新变更。
2. GoVPN 2.0：已在库；免费档不变，无变更。
3. Proton VPN Free：已在库；crashtestlover 2026-11-19 核查一致（不限量、1 台、10 国），无变更。
4. X-VPN Free：已在库；toolgpa 2026-11-12 核查一致（不限量、26 地区、免注册），无变更。
5. hide.me Free：已在库；Gizmodo 2026-11-19 iPhone 榜单称免费 8 地（FI/FR/DE/NL/CH/UK/US），与库内 8 地口径一致，无变更。
6. Windscribe / PrivadoVPN / TunnelBear / Hotspot Shield：已在库；Gizmodo 2026-11-19/20 榜单（5 天前更新）数据与库内一致，无变更。
7. Surfshark 免费 Public DNS 将于 2026-11-24 关停（2026-11-20 宣布，TechRadar 原报）：免费 DNS 服务，非 VPN 免费档；Surfshark 不在库内（无免费 VPN 档），不改库。注：关停日已过（2026-11-24），与昨日记录一致。
8. Samsung Max：已在 discontinued（2026-06-15 关停）；11 月 18 日更新称 One UI 9 开始移除该应用，仅为清理残留，无新增变更。
9. Atlas VPN：已在 discontinued（2024-04-24 关停）；11 月 14/16 日文章为旧闻回顾，无新增变更。
10. ZenMate：2023 年并入 CyberGhost，付费应用已停；官网仍链接免费浏览器扩展。CyberGhost 免费浏览器扩展已在库；ZenMate 不再是独立免费 VPN 服务，不另入库。
11. F-Secure FREEDOME VPN 逐步停用（Win/Mac 支持止于 2026-09-11，Android/iOS 止于 2027-03）：付费产品线合并，非免费档变更；FREEDOME 从未入库，不改库。
12. VPN Monster：acciyo 文章（1 天前更新）仍称似已停运，无明确停运日期、无官网/应用更新。该服务从未入库、无免费档可考证据，不改库；继续列为周检候选观察。
13. Vulcain VPN（vulcainvpn.com，法国个体经营者 Pierre Libran / Galerne Studio，2026-10/11 上线，Product Hunt 2026-11-23）：官网与条款已核实——仅提供按周/月/年付费通行证，免费仅为不定期的免费试用（无需支付方式，试用结束即停用，不转订阅），无永久免费档；不入库。列为周检候选观察（若日后推出永久免费档再评估）。
14. EasyGuard VPN（Product Hunt 2026-11-23）：仅见付费年费优惠（$14.99/年），无免费档证据；不入库。
15. Expat Link VPN（Product Hunt 2026-11-06）：仅 12 小时免费试用，无需信用卡；试用非免费档，不入库。
16. Oxyn VPN（Product Hunt 2026-11-17）：15 天免费试用，无需信用卡；试用非免费档，不入库。
17. LinkItVPN：2026-11-15 至 30 免费送一个月活动（付费用户赠送），非免费档；不入库。
18. Pangolin：开源自托管 ZTNA/远程访问平台，非面向消费者的免费 VPN 档；不入库。
19. VibeVPN（vibevpn.me，TurboByte LTD，Product Hunt 2026-11-11）：官网已实测（2026-11-25）——整站为付费订阅营销页（30 天退款保证、订阅制），无任何免费档额度/国家数/设备数说明；App Store 称“免费开始”但仅列 Premium 订阅价。免费档细节仍无法核实，且官网宣称“独立审计”“法庭验证的零知识”却未具名审计方，存疑；本次仍不入库，继续列为周检候选。
20. Lunari（com.lunari.informa，Android VPN 应用，2026-11 上线，约 3.2k 安装，免费含广告，2026-11-10/11 更新）：无可核实的 VPN 专用官网与隐私政策（lunari.com 隐私政策属于另一家 Lunari Entertainment LLC 咖啡连锁应用）；Play 列表开发商为西安某教育培训公司，数据安全声明称收集设备 ID、数据未加密、不可删除；免费档额度/国家数均无可核实来源。按既往标准（ZeroPing 前例）暂不入库，列为周检候选观察。
21. BBVPN – Super Unlimited VPN / Free VPN by Free VPN .org / VPN – Super Unlimited Proxy / VPN Proxy Master / PandaVPN Lite / iTop VPN：均为老服务或常规版本更新，本次窗口内无免费档变更；继续列为周检候选。
22. Anomi VPN（removed，2026-11-09）：本次复查——curl 连接失败（000），DNS 可解析但无应用层响应，无服务恢复的有效证据。仍在 removed，不恢复入库。
23. AdGuard VPN Free / Bitdefender 免费档 / Browsec Free / VeePN 免费浏览器扩展：长期免费档，本次窗口内无新信息；继续列为周检候选评估。

## 同步

- YAML 已改动：node scripts/build.js 校验通过（45 entries，45 active，7 residential）；export-page-sync.js 已生成同步快照。
- Muse artifact 网页：artifact.edit 已完成并通过核实（构建回执 2026-11-25 02:52 UTC）：页面 DATA 数组 45 条，XXLink 卡片字段逐项与 YAML 一致；家宽确认 5 家 + 部分 2 家、停服 6 条、移除 Anomi 1 条均一致。**注意：构建成功但未自动发布——公开链接目前仍显示上一版（44 条），需用户批准新的 artifact.share 才会更新。**
- Git 仓库：sync.sh 已执行，提交 ad1a93c「更新数据库：新增 XXLink Free VPN（2026-11-25，免费 1GB/7天、6 个地区、需邮箱注册，Windows/Android）」，已推送到 origin main（13d931b..ad1a93c）。
- 公开页面链接：https://muse.ai/s/mian-fei-vpn-shu-ju-ku-xhxd6xe0uxbxsp1n/524jt68zSApSIH5MC2nGlPSbeJuZFtOcaKCX54ZOr1s（注：上一轮构建成功后公开链接仍显示旧版，需用户批准新的 artifact.share 才会更新，本轮同理）

## 结论

- free-vpn-db.yaml：entries 44 → 45 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 6 条；家宽 IP 仍为 7 家。
- 有新增收录，按任务要求汇报：新增 XXLink Free VPN（免费 1 GB/7 天、10 Mbps、6 个地区、需邮箱注册无需信用卡，Windows/Android；注意：非无日志——服务器日志保留 IP 无固定过期时间），页面同步进行中、仓库已推送。
- 下一次检索：明日 2026-11-26（free-vpn-db-daily-discovery）。
