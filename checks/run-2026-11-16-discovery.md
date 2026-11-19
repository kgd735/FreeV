# 每日新免费 VPN 检索 — 2026-11-16 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**无新增收录；无新增关停；YAML 未改动（entries 仍 38 条；removed 1 条；discontinued 5 条），故不触发 artifact 与 git 同步**。

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库；11 月 11–12 日多家媒体（MakeUseOf、ghacks、TechBriefly、badiyaa）报道与库内一致，无新增变更。新增细节：Mozilla 11 月 11 日在 X 称发现第三方应用滥用免费 VPN，曾短暂切断访问调查后已恢复服务——为一次性短暂中断，非免费档变更，不记入 change_log。
2. Proton VPN Free / Windscribe Free / PrivadoVPN Free：antivirusprotection.org 2026-11-07 文章与库内一致（Proton 不限量/1 设备/10 国；Windscribe 10 GB 需确认邮箱并订阅推广邮件；Privado 10 GB/30 天/1 设备）。Windscribe 10 GB 需订阅推广邮件的条件与 Privado 免费额度冲突（fojilo 称 2 GB/月）已于今日周检复核解决：Privado 10 GB/月后降速已确认并记入 YAML；Windscribe 推广邮件条件仍为周检备注。
3. hide.me Free：savozi 2026-11-04 文章与 vpnalert 11 月榜单均称 8 个免费地点（含新加坡）；今日周检已复核官网确认新加坡为付费档，免费为 7 国（FI/FR/DE/NL/CH/UK/US），YAML 已订正，无新增变更。
4. TunnelBear Free：今日周检已确认免费档自动选服、2 GB/月不变，冲突已解决并记入 YAML，无新增变更。
5. GoVPN 2.0：已在库（2026-11-09 入库）；11 月 9 日博文无新增变更。
6. Ninja VPN：已在库（2026-11-12 入库）；Bessy 2026-10-27 文章（11 月 15 日复查时已见）无新增内容。
7. Avast VPN Free：已在库（2026-11-09 入库）；techno360 2026-11-05 评测内容与库内一致（法国上线、3 地自选、不限量受 Fair Usage 约束、印度不可用），无新增变更。
8. Samsung Max：已在 discontinued（2026-06-15 关停）；toolradar 11 月文章为旧闻回顾，无新增变更。
9. ZenMate：reviewedbypro 2026-11 月文章称 ZenMate 付费应用已于 2023 年 5 月并入 CyberGhost，zenmate.com 现仅为导流页，免费 Chrome 扩展仍有链接。非 24–48h 新信息（2023 年旧事），且免费扩展的免费档细节（国家数、额度、日志政策）未核实。**新增周检候选**（与已入库的 CyberGhost 免费扩展同类），暂不入库。
10. Shmel VPN & Network Tools（AZUR APPS FZ-LLC；2026-11 上架 Play，3.2k 安装，v1.1.18，2026-11-09 更新）：仍无官网与独立隐私政策可核。继续监控（自 2026-11-13 延续）。
11. ZeroPing VPN（Star Core Studio；2026-07 上线，150k 安装，v1.0.57，2026-11-12 更新）：仍无官网与独立隐私政策可核。继续监控（自 2026-11-13 延续）。
12. TrendVPN（Teknolance；com.teknolance.trendvpn；v1.1.22，2026-11-11 更新，10k+ 安装）：免费 2 台服务器（德国、保加利亚），无限制连接；Premium 解锁 20+ 服务器。应用列表中仍未见官网与隐私政策链接，无法核实日志政策与运营方。继续监控（自 2026-11-15 延续）。同开发商 TeknoVPN（640k 安装，2026-09-22 更新，免费不限量、无日志宣称）一并列为周检候选。
13. Russian VPN / MEDVET VPN（Super IT；2026-09 上架 Play，仅 590 安装，v4.2.0，2026-11-02 更新）：官网与隐私政策已验证存在，但免费档关键要素（流量额度、免费国家数、设备数）仍未披露，规模极小。继续监控（自 2026-11-15 延续）。
14. USA VPN（AltApps；vpn.usa_tap2free；v1.173，2026-11-14 更新）：免费、无需注册、无流量上限，单次免费连接 1 小时（看广告可延长），OpenVPN + Shadowsocks，隐私政策 tap2free.net 可达（本次 curl 301，有响应），宣称无日志；Play 列表更新于 2026-10-22。**新增监控候选**，暂不入库——非 24–48h 内新上线服务（老应用常规版本更新），且免费国家数、设备数未披露，安装量与运营方背景待核。
15. TapTap VPN（Safebrand Tech；2025-03 上架，16k 安装，v0.2.2，2026-11-06 更新）：免费、含广告、仅 3 台美国服务器，用户评价称连接问题较多。规模小、信息少，**新增监控候选**，暂不入库。
16. TLS Tunnel（v8.5.2，2026-11-05 更新）、VPN Super Unlimited Proxy（v2.36.0，2026-11-03 更新）、StarVPN（v2.46，2026-11-04 更新，100 GB/月免费终身，与库内一致）：多年老牌免费应用，仅常规版本更新；仍列为周检候选，本次不入库。
17. TipTop VPN：Play 列表 2026-11-05 更新；11 月 5–6 日用户评价仍称免费服务器被锁、仅剩 1 个且常无可用服务器。证据冲突，暂不入库，继续监控。
18. Happ - Proxy Utility：已从 Google Play 下架（2026-11-01），从未入库（代理配置工具类应用，非自带服务器的 VPN 服务），本次不作 discontinued 记录；继续监控其是否重新上架。
19. Aloha Browser（内置免费不限量 VPN，浏览器内、无需注册）：多年老产品，非 24–48h 新信息；仍为周检候选（与已入库的 Opera 浏览器 VPN 同类）。
20. Anomi VPN（removed，2026-11-09）：本次复查——HTTPS 请求仍失败（curl https:000，2026-11-16），无服务恢复的有效证据。仍在 removed，不恢复入库。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- Windscribe 10 GB 条件：antivirusprotection.org 2026-11-07 称需确认邮箱且订阅推广邮件；库内仅写“确认邮箱”。周检时核对官网帮助中心。
- Firefox 内置 VPN：2027-02-01 00:00 UTC 恢复 50 GB/月已确认；待 2027-02 复核确认实际恢复情况。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。
- 大复核候选：EVPN、Touch VPN、ZoogVPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Shmel VPN、ZeroPing VPN、TipTop VPN、Aloha Browser、TrendVPN、Russian VPN / MEDVET VPN、USA VPN（新增）、TapTap VPN（新增）、ZenMate 免费扩展（新增）、TeknoVPN（新增）。

## 同步

- YAML 未改动：不运行 export-page-sync.js，不触发 artifact 更新；不运行 sync.sh（无变更自动跳过）。
- Git 状态复查：本地 main 与 origin/main 已同步（远程为 GitHub git@github.com:kgd735/FreeV.git）；今日周检（review-2026-11-16.md）已将 last_full_review 与全部 38 条 last_verified 更新至 2026-11-16。

## 结论

- free-vpn-db.yaml：entries 仍 38 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 5 条。
- 无新增收录、无新增关停，按任务要求保持安静，不向用户汇报。
- 下一次检索：明日 2026-11-17（free-vpn-db-daily-discovery）。
