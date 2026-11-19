# 每日新免费 VPN 检索 — 2026-11-18 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**无新增收录；无新增关停；YAML 未改动（entries 仍 38 条；removed 1 条；discontinued 5 条），故不触发 artifact 与 git 同步**。

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库，无新增变更。11 月 11–12 日多篇报道（makeuseof、ghacks、badiyaa 等）均为同一消息的转载，无新内容。
2. GoVPN 2.0：已在库（2026-11-09 入库）；官网博文（govpn.space/blog/govpn-2-launch）无新增变更。
3. Avast VPN Free：已在库（2026-11-07 入库）；techno360 2026-11-05 实测与库内一致（法国上线、3 地自选、不限量、印度不可用），无新增变更。
4. X-VPN Free：已在库；AppBrain 数据 2026-11-10 更新、Android v208.5.2（2026-11-02）为常规更新，免费档 26 地不限量与库内一致，无新增变更。
5. VPN Super Unlimited Proxy（v2.36.0，2026-11-02/03 更新）：多年老牌免费应用（10 亿+下载、不限量、25+ 地、免注册），仅常规版本更新；仍列为周检候选，本次不入库。
6. VPN Master（2026-11-06 更新）：多年老应用常规更新，无官网/运营方可核信息，暂不入库。
7. ZenMate 免费浏览器扩展：reviewedbypro.com 2026-11 评测确认 ZenMate 2023 年并入 CyberGhost 后，免费 Chrome 扩展仍由 zenmate.com 链接提供；无 24–48h 内新变化。已列入周检候选（自 2026-11-13 延续），本次不入库（CyberGhost 免费扩展本身已在库）。
8. Grass VPN / Unlimited VPN Proxy Server（com.freevpn.vpngrass；A24Z AI / A24Z LTD，伦敦）：**新增周检候选**。Play/AppBrain 称免费不限量、无需注册、4 国（US/DE/FR/TR）、VLESS + Reality、广告支持、Android only、68 万安装；2026-11-01 更新 v2.2.32（在 24–48h 窗口之外）；上线于 2024-10，非新上线服务。未核实独立官网与隐私政策（仅 Play 列表宣称 no-logs、联系邮箱 info@freevpngrass.com；grass.io 为同名带宽共享产品，无关）。暂不入库，待周检核实。
9. Samsung Max：已在 discontinued（2026-06-15 关停）；toolradar 11 月文章为旧闻回顾，无新增变更。
10. Problembo “VPN Access is being discontinued”（2026-11-02）：Telegram 机器人售卖的付费 VPN 接入，非免费档服务、未入库，不作记录。
11. LetsVPN（快连）：2026-04-28 结束中国内地业务、05-15 CEO 确认不再向内地提供服务（kaitu.io 2026-11-10 更新；letsvpnshutdown.com 为同主题站点）。付费服务、未入库、非 24–48h 新信息；仅为中国内地不可用、全球服务仍在，不作 discontinued 记录。
12. F-Secure FREEDOME VPN 逐步停用（Windows/Mac 支持 2026-09-11 结束；Android/iOS 2027-03）：付费产品、未入库，无免费档，不作 discontinued 记录。
13. PandaVPN Lite（com.pandavpnfree.androidproxy）：官网 pandavpn.com 本次 curl 仍超时未达（https:000，10s），无恢复证据；用户评价与 Play 列表的免费时限说法仍冲突。继续列为周检候选，暂不入库。
14. Free VPN by Free VPN .org（org.freevpn；官网 freevpnapp.org 本次 curl 200）：广告支持、800+ 服务器、免注册、宣称 No Logs。多年老应用、常规更新，隐私政策与日志宣称未核实。继续列为周检候选，暂不入库。
15. Shmel VPN & Network Tools：仍无官网与独立隐私政策可核。继续监控（自 2026-11-13 延续）。
16. Anomi VPN（removed，2026-11-09）：本次复查——官网 anomivpn.com 仍无法访问（curl https:000，0.67s），无服务恢复的有效证据。仍在 removed，不恢复入库。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- Windscribe 10 GB 条件：antivirusprotection.org 2026-11-07 称需确认邮箱且订阅推广邮件；库内仅写“确认邮箱”。周检时核对官网帮助中心。
- Firefox 内置 VPN：2027-02-01 00:00 UTC 恢复 50 GB/月已确认；待 2027-02 复核确认实际恢复情况。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。
- 大复核候选：EVPN、Touch VPN、ZoogVPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Shmel VPN、ZeroPing VPN、TipTop VPN、Aloha Browser、TrendVPN、Russian VPN / MEDVET VPN、USA VPN、TapTap VPN、ZenMate 免费扩展、TeknoVPN、PandaVPN Lite、Free VPN by Free VPN .org、Grass VPN（新增）。

## 同步

- YAML 未改动：不运行 export-page-sync.js，不触发 artifact 更新；不运行 sync.sh（无变更自动跳过）。
- Git 状态：未改动，未执行推送；本地 main 与 origin/main 上次同步于 2026-11-16（远程为 GitHub git@github.com:kgd735/FreeV.git）。

## 结论

- free-vpn-db.yaml：entries 仍 38 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 5 条。
- 无新增收录、无新增关停，按任务要求保持安静，不向用户汇报。
- 下一次检索：明日 2026-11-19（free-vpn-db-daily-discovery）。
