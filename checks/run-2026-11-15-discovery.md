# 每日新免费 VPN 检索 — 2026-11-15 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**无新增收录；无新增关停；YAML 未改动（entries 仍 38 条；removed 1 条；discontinued 5 条），故不触发 artifact 与 git 同步**。

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库；多家媒体 11 月 11–12 日报道与库内一致，无新增变更。注：Mozilla Connect 帖称起始日为 11 月 9 日，官方博客为 11 月 10 日——起止以官方博客为准，库内已按 11 月 10 日记录。
2. Proton VPN Free / Windscribe Free / PrivadoVPN Free：antivirusprotection.org 2026-11-07 文章与 privacyaffairs 2026-11-07 更新评测，与库内一致（Proton 不限量/1 设备/10 国；Windscribe 10 GB 需确认邮箱；Privado 10 GB/30 天/1 设备）。Windscribe“需订阅推广邮件才享 10 GB”与 Privado 免费额度冲突（fojilo 称 2 GB/月）仍为周检备注。
3. hide.me Free：savozi 2026-11-04 文章（10 月 23 日核对官网）称免费档已不限量、限速、8 个地点、无需注册——与库内“unlimited / 7 国 8 地点”一致，无变更。免费地点含新加坡还是芬兰的冲突仍在，待周检复核官网。
4. GoVPN 2.0：已在库（2026-11-09 入库）；11 月 8 日博文无新增变更。
5. Ninja VPN：已在库（2026-11-12 入库）；Bessy 2026-11-11 文章无新增内容。
6. Avast VPN Free：已在库（2026-11-09 入库）；techno360 2026-11-05 评测内容与库内一致，无新增变更。
7. Teal VPN：已在库；AppBrain 数据更新 2026-11-11（v1.2.57，10k+ 安装），免费档 500 MB/天、立陶宛 1 地，与库内一致。
8. PrivadoVPN：Play 列表 2026-11-05 更新，免费 10 GB/月，与库内一致，无变更。
9. Planet VPN：Play 列表 2026-11-03 更新，6 个地点/5 国，与库内一致，无变更。
10. ZeroPing VPN（Star Core Studio；2026-07 上线，150k 安装，v1.0.57，2026-11-12 更新）：免费含广告；仍无官网与独立隐私政策可核。继续监控（自 2026-11-13 延续）。
11. Shmel VPN & Network Tools（AZUR APPS FZ-LLC；2026-11 上架 Play，3.2k 安装，v1.1.18，2026-11-09 更新）：仍无官网与独立隐私政策可核。继续监控（自 2026-11-13 延续）。
12. TrendVPN（Teknolance；com.teknolance.trendvpn；v1.1.22，2026-11-11 更新）：免费 2 台服务器（德国、保加利亚），无限制连接；Premium 解锁 20+ 服务器。应用列表中未见官网与隐私政策链接，无法核实日志政策与运营方。**新增监控候选**，暂不入库。
13. Russian VPN / MEDVET VPN（Super IT；com.medvet.vpn.app；2026-09 上架 Play，仅 590 安装，无评分，v4.2.0，2026-11-02 更新）：官网 medvetvpn.com 与隐私政策（2026-09-24）本次已验证存在——免费服务器多国、无需注册、无广告；隐私政策称不记录浏览历史/DNS/访问站点与流量内容，但保留有限连接记录（连接/断开时间、使用服务器）；运营方为乌兹别克斯坦个体户 Super IT（Nomonov Akromjon Abdullajon ogli, YATT）。但免费档关键要素均未披露（流量额度、免费国家数、设备数），且规模极小（590 安装）、非 24–48h 内新信息（9 月上线，11 月 2 日仅常规更新）。**新增监控候选**，暂不入库；待其披露免费档细节或规模显著增长后再评估。
14. TipTop VPN：Play 列表 2026-11-05 更新；11 月 5–6 日用户评价仍称免费服务器被锁、仅剩 1 个且常无可用服务器。证据冲突，暂不入库，继续监控。
15. Happ - Proxy Utility：**下架已获独立证实**——AppBrain 2026-11-15 数据：已从 Google Play 下架（2026-11-01，v4.8.0 为最后版本，2026-10-16 更新；32M 安装，4.24 星），与 proxysvpn.com 2026-11-09 文章相互印证。Happ 从未入库（系代理配置工具类应用，非自带服务器的 VPN 服务），本次仍不作 discontinued 记录；继续监控其是否重新上架。
16. TLS Tunnel（v8.5.2，2026-11-05 更新）、VPN Super Unlimited Proxy（v2.36.0，2026-11-03 更新）：多年老牌免费应用，仅常规版本更新；仍列为周检候选，本次不入库。
17. Aloha Browser（内置免费不限量 VPN，浏览器内、无需注册）：多年老产品，非 24–48h 新信息；仍为周检候选（与已入库的 Opera 浏览器 VPN 同类）。
18. Le VPN 16 周年（2026-11-10）：一次性促销，非免费档。不作变更。
19. Samsung Max、Atlas VPN、Google One VPN、Kaspersky 免费版：均已在 discontinued。→ 不作变更。
20. Anomi VPN（removed，2026-11-09）：本次复查——DNS 现可解析（anomivpn.com → 198.18.230.80，属代理/CGNAT 段），但 HTTPS 请求仍失败（curl 返回 000，无响应），无服务恢复的有效证据。仍在 removed，不恢复入库。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- TunnelBear 免费档服务器选择：库内记录 2026 年起免费档取消手动选服（自动分配）；Cybernews 2026-10-28 更新文章称 TunnelBear 是唯一不限制免费用户服务器数量的免费 VPN。两者冲突，需复核官网确认。（自 2026-11-09 延续）
- Hide.me 免费地点：vpnalert 2026-11 月榜单列出的 8 个免费地点中含新加坡而非芬兰；库内为 FI/FR/DE/NL/CH/UK/US。需复核。（自 2026-11-09 延续）
- PrivadoVPN 免费额度：库内为 10 GB/月全速后降速；fojilo 2026-11-01 文章称免费档仅 2 GB/月。两者冲突，需复核官网确认。（自 2026-11-10 延续）
- Windscribe 10 GB 条件：antivirusprotection.org 2026-11-07 称需确认邮箱且订阅推广邮件；库内仅写“确认邮箱”。周检时核对官网帮助中心。
- Firefox 内置 VPN：2027-02-01 00:00 UTC 恢复 50 GB/月已确认；待 2027-02 复核确认实际恢复情况。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。
- 大复核候选：EVPN、Touch VPN、ZoogVPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Shmel VPN、ZeroPing VPN、TipTop VPN、Aloha Browser、TrendVPN（新增）、Russian VPN / MEDVET VPN（新增）。

## 同步

- YAML 未改动：不运行 export-page-sync.js，不触发 artifact 更新；不运行 sync.sh（无变更自动跳过）。
- Git 状态复查：本地 main 与 origin/main 已同步（远程为 GitHub git@github.com:kgd735/FreeV.git，提交 f1461c7 在列）；2026-11-14 日志中记录的 Gitea 推送失败已随当日迁移至 GitHub 解决，无待推送提交。

## 结论

- free-vpn-db.yaml：entries 仍 38 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 5 条。
- 无新增收录、无新增关停，按任务要求保持安静，不向用户汇报。
- 下一次检索：明日 2026-11-16（free-vpn-db-daily-discovery）。
