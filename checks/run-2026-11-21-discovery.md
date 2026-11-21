# 每日新免费 VPN 检索 — 2026-11-21 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（UnblockMeVPN）；无新增关停；YAML 由 40 条增至 41 条；git 已推送；artifact 页面同步已触发，待构建回执确认**。

## 新增收录

### UnblockMeVPN（id: unblockmevpn）— 2026-11-21 入库
- 官网：https://www.unblockmevpn.com（免费档页 https://www.unblockmevpn.com/free-usa-vpn-no-credit-card.html，发布于 2026-11-12；本次 browser.open 抓取 2026-11-21 02:49 UTC；curl 首页 200）
- 免费档：1 个免费节点（美国洛杉矶，Sharktech 机房）；无需信用卡；需创建账号（邮箱，或账号号+恢复密钥，无需邮箱）；流量额度官网未说明（仅公平使用）；设备数未说明（付费档 5 台）
- IP 类型：datacenter（Sharktech 机房 IP，无家宽/住宅 IP 功能）
- 协议：OpenVPN（per buildvoyage 技术栈列表）
- 日志：**非 no-logs**——隐私政策（2026-10-19 更新）明确服务器诊断日志可能含源/目的地址与端口、时间戳、连接标识符，可关联账号/设备；保留于服务器日志，无统一固定保留期；无独立审计；运营方 POD RV LLC（美国夏威夷檀香山）
- 平台：Windows、macOS、iOS、Android
- 重要限制：免费访问为酌情提供（discretionary），可能随时变更、限流、暂停或取消（官网免费档页 + ToS 2026-07-12 均有声明）；已记入 change_log
- 来源：https://www.unblockmevpn.com/free-usa-vpn-no-credit-card.html、https://www.unblockmevpn.com/privacy.html、https://www.unblockmevpn.com/terms.html、https://appbreakup.com/apps/unblockmevpn（2026-11-15 核实）、https://buildvoyage.com/products/unblockmevpn（发布 2026-11-15）

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库；本周内多篇报道均为同一消息的转载，无新变更。
2. GoVPN 2.0：已在库；官网博文（2026-11-15 更新）无新增变更。
3. Proton VPN / Windscribe / PrivadoVPN / hide.me / TunnelBear / Hotspot Shield：Gizmodo、Toolradar（2026-11-20 更新）榜单均与库内一致；hide.me 免费地点数冲突（Toolradar 称 8 地含新加坡 vs 库内 7 国、新加坡付费）——2026-11-16 已核实以官网为准，不改库。
4. Surfshark 免费 Public DNS 将于 2026-11-24 关停（2026-11-20 宣布，引用率低）：免费 DNS 服务，非 VPN 免费档；Surfshark 不在库内（无免费 VPN 档），不改库。
5. Samsung Max：已在 discontinued（2026-06-15 关停）；2026-11-18 消息仅为 One UI 9 开始移除已停服应用，无新增变更。
6. Atlas VPN：已在 discontinued（2024-04-24 关停）；2026-11-14 文章为旧闻回顾，无新增变更。
7. F-Secure FREEDOME 逐步停服（Win/Mac 支持 2026-09-11 结束，Android/iOS 2027-03）：付费 VPN，无免费档，不在库内，不改库。
8. MillenVPN OpenConnect 部分服务器 2026-11-25 停服：付费服务个别节点调整，非免费档关停；不改库。
9. LetsVPN：中国大陆服务 2026-04-28 曾暂停后 5 月恢复，10 月上海报告可用；付费服务、非免费档关停，与本库无关；不改库。
10. Free VPN by Free VPN .org（org.freevpn）：官网 https://freevpnapp.org 本次抓取 2026-11-21 02:49 UTC；Trust Center（2026-10-15 复核）确认出版方 Free VPN LLC、无日志声明、无需账号、看广告换 VPN 时长（移动端），平台 iPhone/Android/Windows/Mac/Apple TV/Linux，80M+ 下载、自 2015 年上线。但免费档时长/流量模型（每广告换多少分钟、日上限）仍未在官网或 Trust Center 明确，继续列为周检候选，暂不入库。
11. ZenMate 免费浏览器扩展：与 CyberGhost 免费扩展条目（已在库）同属 Kape 免费浏览器代理，单独建条目会重复，继续列为周检候选，本次不入库。
12. SuperVPN Free VPN Client：多年老牌免费应用，仅常规版本更新；继续列为周检候选，本次不入库。
13. Anomi VPN（removed，2026-11-09）：本次复查——官网 anomivpn.com 仍无法访问（curl https:000），无服务恢复的有效证据。仍在 removed，不恢复入库。
14. PandaVPN Lite（com.pandavpnfree.androidproxy）：官网 pandavpn.com 本次 curl 仍超时未达（https:000），无恢复证据；继续列为周检候选，暂不入库。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- Windscribe 10 GB 条件：antivirusprotection.org 2026-11-07 称需确认邮箱且订阅推广邮件；库内仅写“确认邮箱”。周检时核对官网帮助中心（自 2026-11-18 延续）。
- Firefox 内置 VPN：2027-02-01 00:00 UTC 恢复 50 GB/月已确认；待 2027-02 复核确认实际恢复情况。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。
- ZoogVPN：免费地点数以官网免费档页 5 国为准；若后续官网改回 3 国，以最新官网为准。
- UnblockMeVPN：免费访问为酌情提供、随时可取消；若官网撤下免费档页或停止免费节点，按关停处理。免费档设备数与流量额度官网未说明，复核时留意官网是否补充。
- 大复核候选：EVPN、Touch VPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Shmel VPN、ZeroPing VPN、TipTop VPN、Aloha Browser、TrendVPN、Russian VPN / MEDVET VPN、USA VPN、TapTap VPN、ZenMate 免费扩展、TeknoVPN、PandaVPN Lite、Free VPN by Free VPN .org、SuperVPN Free VPN Client。

## 同步

- YAML 已改动（+1 条）：已运行 export-page-sync.js 生成快照（41 条）；artifact.edit 已触发（slug: mian-fei-vpn-shu-ju-ku），构建成功回执：页面内嵌 DATA 共 41 条、家宽 4 条 + 部分 2 条、UnblockMeVPN 条目字段逐字取自快照与 YAML（含“免费访问属酌情提供、可随时终止”与“并非无日志”两项说明），页面 JS 通过语法校验，停服 5 条、移除 1 条未变，验证通过。
- 注意：构建成功但 `current_build_published: false`——公开链接仍显示上一版（40 条），需用户明确要求重新分享才会更新；Muse 内打开的页面已是 41 条新版。
- Git：bash sync.sh 已执行，提交 1b145b6，已推送到 origin main（GitHub kgd735/FreeV）。
- 公开页面链接：https://muse.ai/s/mian-fei-vpn-shu-ju-ku-xhxd6xe0uxbxsp1n/524jt68zSApSIH5MC2nGlPSbeJuZFtOcaKCX54ZOr1s

## 结论

- free-vpn-db.yaml：entries 40 → 41 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 5 条；家宽 IP 仍为 6 家。
- 新增收录 UnblockMeVPN，按任务要求向用户汇报；页面与仓库同步完成（页面构建验证通过；公开链接仍显示上一版 40 条，待用户要求重新分享时再更新）。
- 下一次检索：明日 2026-11-22（free-vpn-db-daily-discovery）。
