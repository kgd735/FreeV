# 每日新免费 VPN 检索 — 2026-11-20 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（ZoogVPN Free）；无新增关停；YAML 由 39 条增至 40 条；已触发 artifact 页面同步与 git 推送**。

## 新增收录

### ZoogVPN Free（id: zoogvpn）— 2026-11-20 入库
- 官网：https://zoogvpn.com（免费档页 https://zoogvpn.com/free-vpn 本次 curl 200，browser.open 抓取 2026-11-20 02:48 UTC）
- 免费档：终身免费、10 GB/月；5 国（US、UK、NL、DE、SG）；1 台设备；需邮箱注册免费账号；无需信用卡；无广告
- IP 类型：datacenter（无家宽/住宅 IP 功能）
- 日志：no-logs 声明；无独立审计；希腊（5/9/14 眼之外）；免费档加密为 128-bit（256-bit 为 Premium）
- 协议：WireGuard、IKEv2、OpenVPN、Shadow（混淆）、Rift，含 kill switch
- 平台：Windows、macOS、iOS、iPadOS、Android、Linux、Chromebook、Kindle Fire、路由器
- 入库依据：Toolradar 2026-11-19 最佳免费 VPN 榜单列为推荐免费档；此前列为周检候选，本次官网免费档页已核实，达到收录标准（与 Berry/Skyvora/Grass 的入库路径一致）
- 冲突记录：免费地点数——旧评测/FAQ 称 3 国，当前官网免费档页列 5 国，以官网为准；另有旧评测称免费计划 14 天到期，当前官网明确写“Free for life, not a trial”，以官网为准
- 来源：https://zoogvpn.com/free-vpn、https://toolradar.com/blog/best-free-vpns、https://www.safetydetectives.com/best-vpns/zoogtv/?filter_sort=helpful、https://impulsec.com/virtual-private-network/zoog-vpn-review/

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库。伊朗地区约 24 小时临时关闭已恢复（wirebyte 2026-11-11），非关停，不改库。
2. Proton VPN：已在库；Nov 19 评测确认免费档仍为不限量、1 台、10 国自动选服，Black Friday Plus 折扣为付费促销。无免费档变更，不改库。
3. GoVPN 2.0：已在库；官网博文（2026-11-13）无新增变更。
4. Atlas VPN：已在 discontinued（2024-04-24 关停）；2026-11-14 文章为旧闻回顾，无新增变更。
5. ZenMate 免费浏览器扩展：reviewedbypro 2026-11-11 确认 zenmate.com 仍链接免费 Chrome 扩展，付费应用 2023 年已并入 CyberGhost；与 CyberGhost 免费扩展条目（已在库）同属 Kape 免费浏览器代理，单独建条目会重复，继续列为周检候选，本次不入库。
6. Free VPN by Free VPN .org（org.freevpn）：官网 https://freevpnapp.org 本次 curl 200、页面抓取 2026-11-20 02:49 UTC——免费、无账号/邮箱/信用卡、广告支持（手机端看广告换 VPN 时长）、no-logs 声明、80M+ 下载、自 2015 年上线、2026-10-15 更新，平台 iPhone/Android/Windows/Mac/Apple TV/Linux。但未核实隐私政策细节与数据/时长上限模型，继续列为周检候选，暂不入库。
7. SuperVPN Free VPN Client：多年老牌免费应用，仅常规版本更新；继续列为周检候选，本次不入库。
8. LetsVPN：中国大陆服务已于 2026-04-28 结束（付费服务、非免费档关停），与本库无关；不改库。
9. MillenVPN OpenConnect 部分服务器 2026-11-25 停服：付费服务个别节点调整，非免费档关停；不改库。
10. Anomi VPN（removed，2026-11-09）：本次复查——官网 anomivpn.com 仍无法访问（curl https:000），无服务恢复的有效证据。仍在 removed，不恢复入库。
11. PandaVPN Lite（com.pandavpnfree.androidproxy）：官网 pandavpn.com 本次 curl 仍超时未达（https:000），无恢复证据；继续列为周检候选，暂不入库。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- Windscribe 10 GB 条件：antivirusprotection.org 2026-11-07 称需确认邮箱且订阅推广邮件；库内仅写“确认邮箱”。周检时核对官网帮助中心（自 2026-11-18 延续）。
- Firefox 内置 VPN：2027-02-01 00:00 UTC 恢复 50 GB/月已确认；待 2027-02 复核确认实际恢复情况。另：Mozilla 曾在 2026 年夏季做过同类不限量推广（8 月 31 日结束、9 月恢复 50 GB），属季节性促销模式。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。
- ZoogVPN：免费地点数以官网免费档页 5 国为准；若后续官网改回 3 国，以最新官网为准。
- 大复核候选：EVPN、Touch VPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Shmel VPN、ZeroPing VPN、TipTop VPN、Aloha Browser、TrendVPN、Russian VPN / MEDVET VPN、USA VPN、TapTap VPN、ZenMate 免费扩展、TeknoVPN、PandaVPN Lite、Free VPN by Free VPN .org、SuperVPN Free VPN Client。

## 同步

- YAML 已改动（+1 条）：已运行 export-page-sync.js 生成快照（40 条）；artifact.edit 已触发（slug: mian-fei-vpn-shu-ju-ku），构建成功回执：页面内嵌 DATA 共 40 条、家宽 4 条 + 部分 2 条、ZoogVPN 条目字段逐字取自快照与 YAML（含两项冲突口径说明），页面 JS 通过语法校验，停服 5 条、移除 1 条未变，验证通过。
- 注意：构建成功但 `current_build_published: false`——公开链接仍显示上一版（39 条），需用户明确要求重新分享才会更新；Muse 内打开的页面已是 40 条新版。
- Git：bash sync.sh 已执行，提交 6a1c262，已推送到 origin main（GitHub kgd735/FreeV）。
- 公开页面链接：https://muse.ai/s/mian-fei-vpn-shu-ju-ku-xhxd6xe0uxbxsp1n/524jt68zSApSIH5MC2nGlPSbeJuZFtOcaKCX54ZOr1s

## 结论

- free-vpn-db.yaml：entries 39 → 40 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 5 条；家宽 IP 仍为 6 家。
- 新增收录 ZoogVPN Free，按任务要求向用户汇报；页面与仓库同步完成情况待 artifact 构建回执后确认。
- 下一次检索：明日 2026-11-21（free-vpn-db-daily-discovery）。
