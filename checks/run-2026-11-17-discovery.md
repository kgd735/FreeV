# 每日新免费 VPN 检索 — 2026-11-17 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**无新增收录；无新增关停；YAML 未改动（entries 仍 38 条；removed 1 条；discontinued 5 条），故不触发 artifact 与 git 同步**。

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库，无新增变更。新增细节：wirebyte 2026-11-11 报道，Mozilla 因疑似第三方应用滥用，曾短暂切断伊朗地区免费 VPN 约 24 小时调查，随后恢复——为一次性地区性短暂中断，非免费档变更，不记入 change_log（与 2026-11-16 结论一致）。
2. hide.me Free 地点冲突：vpnalert 11 月榜单、etunescafe（2026-11-12 左右更新）仍称 8 个免费地点（含新加坡）；2026-11-16 周检已按官网核实新加坡为付费档、免费为 7 国，YAML 已订正。两篇新榜单无新证据，冲突来源不变，无新增变更。
3. Proton VPN Free / Windscribe Free / PrivadoVPN Free：privacyaffairs（2026-11-07 更新）、antivirusprotection.org、savozi、etunescafe 11 月榜单与库内一致（Proton 不限量/1 设备/10 国自动选服；Windscribe 10 GB 需确认邮箱；Privado 10 GB/30 天/1 设备）。无新增变更。
4. GoVPN 2.0：已在库（2026-11-09 入库）；官网博文（govpn.space/blog/govpn-2-launch）无新增变更。
5. Ninja VPN：已在库（2026-11-12 入库）；Bessy 2026-10-27 文章无新增内容（2026-09-12 停运俄/伊/中已记入 change_log）。
6. Planet VPN / PrivadoVPN 安卓应用更新（2026-11-03 / 2026-11-05）：Play 列表内容与库内一致（Planet 6 地 5 国不限量；Privado 10 GB/月），无新增变更。
7. Samsung Max：已在 discontinued（2026-06-15 关停）；toolradar 11 月文章为旧闻回顾，无新增变更。
8. LetsVPN（快连）：2026-04-28 结束中国内地业务、05-15 CEO 确认不再向内地提供服务（kaitu.io 2026-11-10 更新）。付费服务、未入库、非 24–48h 新信息；仅为中国内地不可用、全球服务仍在，不作 discontinued 记录。
9. Problembo “VPN Access is being discontinued”（2026-11-02）：Telegram 机器人售卖的付费 VPN 接入，非免费档服务、未入库，不作记录。
10. F-Secure FREEDOME VPN 逐步停用（Windows/Mac 支持 2026-09-11 结束；Android/iOS 2027-03）：付费产品、未入库，无免费档，不作 discontinued 记录。
11. SSH Afrika（Cursus Digital；2026-11 上架 Play，220 安装，2026-11-07 更新）：VLESS / SlowDNS / SSL Tunnel 配置客户端，需自备服务器，非自带服务器的 VPN 服务——与 Happ 同类，**排除入库**，不列为监控候选。
12. Shmel VPN & Network Tools（AZUR APPS FZ-LLC；v1.1.20，2026-11-13 更新）：仍无官网与独立隐私政策可核。继续监控（自 2026-11-13 延续）。
13. VPN Super Unlimited Proxy（v2.36.0，2026-11-03 更新；vpnsuper.com 本次 curl 200）：多年老牌免费应用（10 亿+下载、不限量、25+ 地点、免注册），仅常规版本更新；仍列为周检候选，本次不入库。
14. PandaVPN Lite（com.pandavpnfree.androidproxy；v10.0.0，2026-11-11 更新）：Play 列表称“Free”标签页服务器无限期免费、无广告无付费；但多条用户评价称免费访问有时限、过期后无法使用，证据冲突；免费国家数不明（第三方研究称约 4 国）；官网 pandavpn.com 本次 curl 超时未达（https:000，6.5s），日志政策未核实。**新增周检候选**，暂不入库。更新日期亦在 24–48h 窗口之外。
15. Free VPN by Free VPN .org（org.freevpn；2026-11-04 更新；官网 freevpnapp.org 本次 curl 200）：广告支持、800+ 服务器、免注册、宣称 No Logs。多年老应用、常规更新，隐私政策与日志宣称未核实。**新增周检候选**，暂不入库。
16. VPN Master（2026-11-06 更新）、Aloha Browser v8.14.0（2026-11-13 更新）、“VPN - fast proxy + secure”（Stolitomson VPN，2026-11-06 更新）：多年老应用常规更新；Aloha 仍为周检候选；其余无官网/运营方可核信息，暂不入库。
17. ZeroPing VPN、TrendVPN、USA VPN、TapTap VPN：本窗口内无新信息，继续监控（自 2026-11-13/15 延续）。
18. Anomi VPN（removed，2026-11-09）：本次复查——DNS 现可解析至 198.18.233.87（CGNAT 段），但 HTTPS 仍失败（curl https:000，2026-11-17），无服务恢复的有效证据。仍在 removed，不恢复入库。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- Windscribe 10 GB 条件：antivirusprotection.org 2026-11-07 称需确认邮箱且订阅推广邮件；库内仅写“确认邮箱”。周检时核对官网帮助中心。
- Firefox 内置 VPN：2027-02-01 00:00 UTC 恢复 50 GB/月已确认；待 2027-02 复核确认实际恢复情况。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。
- 大复核候选：EVPN、Touch VPN、ZoogVPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Shmel VPN、ZeroPing VPN、TipTop VPN、Aloha Browser、TrendVPN、Russian VPN / MEDVET VPN、USA VPN、TapTap VPN、ZenMate 免费扩展、TeknoVPN、PandaVPN Lite（新增）、Free VPN by Free VPN .org（新增）。

## 同步

- YAML 未改动：不运行 export-page-sync.js，不触发 artifact 更新；不运行 sync.sh（无变更自动跳过）。
- Git 状态：未改动，未执行推送；本地 main 与 origin/main 上次同步于 2026-11-16（远程为 GitHub git@github.com:kgd735/FreeV.git）。

## 结论

- free-vpn-db.yaml：entries 仍 38 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 5 条。
- 无新增收录、无新增关停，按任务要求保持安静，不向用户汇报。
- 下一次检索：明日 2026-11-18（free-vpn-db-daily-discovery）。
