# 每日新免费 VPN 检索 — 2026-11-13 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（CyberGhost 免费浏览器扩展）；Firefox 内置 VPN 额度恢复时间确认（2026-11-12 消息）；无新增关停**。

## 新增收录

### 1. CyberGhost 免费浏览器扩展（cyberghostvpn.com；罗马尼亚，Kape 旗下）
- 去重：库内无 CyberGhost 条目；removed 仅 Anomi VPN；discontinued 无记录。→ 可入库。
- 说明：自 2026-11-10 起列为周检候选；本次多方佐证已充分，决定入库。
- 核实（2026-11-13，官网 + 独立评测）：
  - 官网支持页：所有 CyberGhost 扩展均免费使用，无需 CyberGhost 账户（support.cyberghostvpn.com）
  - 官网隐私中心：免费扩展可换 RO/NL/DE/US 四国 IP，仅保护浏览器流量（cyberghostvpn.com/privacyhub/hide-my-ip-address）
  - Firefox 附加组件页：4 个位置（US/DE/NL/RO），免费；明确提示不防 WebRTC 泄漏（addons.mozilla.org）
  - TechRepublic：8 台服务器、4 个国家，免费，Chrome 扩展内无需账户
  - top10vpn（2026-09-30 更新）：永久免费（非试用），Chrome/Firefox；数据额度列为不限量；警告其为代理而非加密 VPN，实测存在真实 IP 泄漏
  - umatechnology（官网页面 2026-10-07 核查）：无需账户/邮箱；8 台服务器、4 国
  - 日志/审计：完整服务为 Deloitte 审计的严格无日志政策，季度透明度报告；扩展本身为代理
  - 免费档：不限量（top10vpn；另有一篇 2026 年综述称“limited”，未证实，已注明）；无需注册、无需信用卡；仅浏览器内
  - IP 类型：机房 IP（residential_ip: false）；注意：这是浏览器代理，不是全设备 VPN 隧道
  - 平台：Chrome / Firefox 扩展
  - 变更：YAML entries 35 → 36（id: cyberghost-extension，last_verified 2026-11-13）。

## 变更（非新增）

### Firefox 内置 VPN：额度恢复时间确认
- 2026-11-12 betanews 消息：Mozilla 确认 50 GB/月额度于 2027-02-01 00:00 UTC 恢复，优惠结束前会提醒用户。
- 变更：change_log 中“2027-02-01 后额度状态未公布”修正为已确认恢复时间；新增 betanews 来源；last_verified 2026-11-11 → 2026-11-13。

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库；本次仅确认恢复时间（见上）。
2. GoVPN 2.0：已在库（2026-11-09 入库）；今日搜索仍为同一篇 11 月 6 日博文，无新增变更。
3. Ninja VPN：已在库（2026-11-12 入库）；Bessy 2026-11-11 文章无新增内容。
4. Proton VPN Free / Windscribe Free / PrivadoVPN Free：antivirusprotection.org 2026-11-07 文章确认三者免费档与库内一致（Proton 不限量/1 设备/10 国；Windscribe 10 GB 需确认邮箱+订阅推广邮件；Privado 10 GB/30 天、定价 FAQ 称 1 设备、免费页称不限设备——与库内冲突记录一致，fojilo 称 2 GB/月的说法仍被主流来源否定）。无变更；Windscribe“需订阅推广邮件才享 10 GB”这一条件记入周检备注。
5. Avast VPN Free：已在库（2026-11-09 入库）；techno360 2026-11-05 评测内容与库内一致，无新增变更。
6. Shmel VPN & Network Tools（AZUR APPS FZ-LLC；2026-11 上架 Play，3.2k 安装，v1.1.18，2026-11-09 更新）：Play 列表自称不记流量日志、可选分析；无官网与独立隐私政策可核。列为监控候选，本次不入库。
7. ZeroPing VPN（Star Core Studio；2026-07 上线，140k 安装，近 30 天新增 100k，v1.0.56，2026-11-06 更新）：免费含广告，Play 列表自称不存浏览/DNS/流量日志；无官网与独立隐私政策可核。列为监控候选（增长快，值得关注），本次不入库。
8. Berry VPN（Coin Alarm；2026-10 上线；1.7k 安装；免费不限量、30 分钟会话）：仍仅 AppBrain/Play 信息，无官网与隐私政策可核。列为监控候选（自 2026-11-11 延续），本次不入库。
9. Skyvora VPN（Averon Soft；2026-09 上线；免费不限量）：仍仅 AppBrain/Play 信息，无官网。列为监控候选（自 2026-11-11 延续），本次不入库。
10. Happ - Proxy VPN、Proxiten：仍无官网可核，继续监控（自 2026-11-12 延续）。
11. TipTop VPN：10 月 14 日用户评价称更新后免费服务器被锁、仅剩 1 个且常无可用服务器；11 月 5 日评价称状态不明。未入库；无官网可核，继续监控，不作变更。
12. VPN Super Unlimited Proxy（1B+ 下载）、VPN.lat（10M+ 安装，v3.9.64，2026-11-11 更新）、TLS Tunnel：均为多年老牌免费应用，非 24–48h 新信息；未入库，列为周检候选（评估是否补录）。
13. XSUsenet：Usenet 供应商已关闭，其 VPN 附加产品随之终止（usenetreviewz 2026-11-09 更新）；非独立免费 VPN 服务，库内无条目，不作 discontinued 记录。
14. Samsung Max、Atlas VPN、Google One VPN、Kaspersky 免费版：均已在 discontinued。→ 不作变更。
15. Anomi VPN：无恢复有效的可信证据，仍在 removed。→ 不作变更。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- TunnelBear 免费档服务器选择：库内记录 2026 年起免费档取消手动选服（自动分配）；Cybernews 2026-10-28 更新文章称 TunnelBear 是唯一不限制免费用户服务器数量的免费 VPN。两者冲突，需复核官网确认。（自 2026-11-09 延续）
- Hide.me 免费地点：vpnalert 列出的 8 个免费地点中含新加坡而非芬兰；库内为 FI/FR/DE/NL/CH/UK/US。需复核。（自 2026-11-09 延续）
- PrivadoVPN 免费额度：库内为 10 GB/月全速后降速；fojilo 2026-11-01 文章称免费档仅 2 GB/月。两者冲突，需复核官网确认。（自 2026-11-10 延续）
- Windscribe 10 GB 条件：antivirusprotection.org 2026-11-07 称需确认邮箱且订阅推广邮件；库内仅写“确认邮箱”。周检时核对官网帮助中心。
- Firefox 内置 VPN：2027-02-01 00:00 UTC 恢复 50 GB/月已确认（本次更新）；待 2027-02 复核确认实际恢复情况。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。
- 大复核候选：EVPN、Touch VPN、ZoogVPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Skyvora VPN、Berry VPN、Shmel VPN、ZeroPing VPN、TipTop VPN。

## 同步

- Git 仓库：sync.sh 执行成功，commit 234c093 已推送到 origin main（Gitea ssh://git@gits.d35.kdns.fr:2222/kuangdash/FreeVPN.git）。
- Muse artifact 网页（mian-fei-vpn-shu-ju-ku）：artifact.edit 构建完成并通过校验（builder 回传 2026-11-13 02:52 UTC）：页面 DATA 为 36 条，含 CyberGhost 免费浏览器扩展卡片；Firefox 条目 change_log 含 2027-02-01 恢复时间；家宽统计 4 家确认 + 2 家部分；removed 仍 1 条、discontinued 仍 5 条；页面内嵌 JS 通过 node --check。**注意：本次构建尚未发布到公开链接——公开链接仍显示上一版（35 条），需用户明确要求重新分享才会更新。**

## 结论

- free-vpn-db.yaml：35 → 36 条 entries；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 5 条。
- 下一次检索：明日 2026-11-14（free-vpn-db-daily-discovery）。
