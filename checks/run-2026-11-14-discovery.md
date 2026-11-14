# 每日新免费 VPN 检索 — 2026-11-14 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 2 条（Berry VPN、Skyvora VPN）；无新增关停；Firefox 内置 VPN 11 月 11 日短暂中断事件已记录（当日恢复，非免费档变更）**。

## 新增收录

### 1. Berry VPN（berryvpn.app；Coin Alarm）
- 去重：库内无 Berry 条目；removed 仅 Anomi VPN；discontinued 无记录。→ 可入库。
- 说明：自 2026-11-11 起列为监控候选（当时无官网与隐私政策可核）；本次官网 berryvpn.app 已可验证，阻塞解除。
- 核实（2026-11-14，官网实测 + AppBrain/Softonic）：
  - 官网首页（当日抓取）：免费永久，无需注册；30 分钟会话、可立即重连，单次看广告 +30 分钟；60 国、国家自选或 Auto；无账户、无邮箱、无需信用卡
  - 官网 FAQ 日志说明：不记录访问网站与流量内容；保留少量技术记录（会话开始时间、使用服务器）；服务器由独立网络运营商运行，对方可能保留自己的连接日志
  - Premium：$2.95 起一次性通行证（7/30/90 天或终身），USDT/USDC 加密支付，无需绑卡
  - 协议：Berry Protocol（自研，官网立陶宛节点页提及）
  - 平台：仅 Android（Windows/macOS 即将推出）；Google Play v1.3.7（2026-11-06 更新），2026-10 上架
  - IP 类型：机房 IP（residential_ip: false）；无住宅/P2P 功能
  - 日志/审计：官网 FAQ 声明不记录浏览与流量内容；无独立审计
  - 变更：YAML entries 36 → 37（id: berry-vpn，last_verified 2026-11-14）。

### 2. Skyvora VPN（skyvora.app；Averon Soft）
- 去重：库内无 Skyvora 条目；removed 仅 Anomi VPN；discontinued 无记录。→ 可入库。
- 说明：自 2026-11-11 起列为监控候选（当时无官网与隐私政策可核）；本次官网与隐私政策均已验证，阻塞解除。
- 核实（2026-11-14，官网实测 + 隐私政策 + AppBrain/Play）：
  - 官网首页（当日抓取）：免费永久，不限量、无时间限制、无需注册；广告维持免费服务器；Premium 去广告并解锁 Turbo 服务器
  - 隐私政策（skyvora.app/privacy.html，更新于 2026-11-03）：不索要身份、不记录访问网站、不出售信息；无账户故无画像；连接时 IP 对服务器可见；免费版展示 Google AdMob 广告
  - 协议：VLESS + Reality；10 Gbps 上行、BBR 拥塞控制（官网宣称）
  - 免费档：不限流量；设备数不限；9 国（NL、DE、FR、ES、US、CA、JP、HK、SG）；P2P/BitTorrent 被禁
  - 平台：仅 Android；Google Play 2026-09 上架（近期更新 2026-10-08）
  - IP 类型：机房 IP（residential_ip: false）；无住宅/P2P 功能
  - 日志/审计：隐私政策明确无日志声明；Play 数据安全页提示可能与第三方共享位置、应用活动等 2 类数据；无独立审计；运营方司法管辖区未披露
  - 变更：YAML entries 37 → 38（id: skyvora-vpn，last_verified 2026-11-14）。

## 变更（非新增）

### Firefox 内置 VPN：11 月 11 日短暂中断后恢复
- 2026-11-11 Mozilla 在 X 上称：发现未授权第三方应用疑似滥用免费 VPN，已临时中断访问进行调查，随后服务恢复（thetechstreetnow 2026-11-11 报道；pasqualepillitteri 同日引述）。
- 结论：一次性临时事件，当日恢复；免费档条款（2026-11-10 至 2027-01-31 不限量，2027-02-01 恢复 50 GB/月）无变化。仅记入本次运行日志，不改 YAML。

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库；本次仅记录 11 月 11 日中断事件（见上）。
2. GoVPN 2.0：已在库（2026-11-09 入库）；11 月 7 日博文无新增变更。
3. Ninja VPN：已在库（2026-11-12 入库）；Bessy 2026-11-11 文章无新增内容。
4. Avast VPN Free：已在库（2026-11-09 入库）；techno360 2026-11-05 评测内容与库内一致，无新增变更。
5. Proton VPN Free / Windscribe Free / PrivadoVPN Free：antivirusprotection.org 2026-11-07 文章与库内一致；vpnalert 2026-11 月榜单将 hide.me 免费地点列为 8 个（含新加坡而非芬兰）——与库内 FI/FR/DE/NL/CH/UK/US 的冲突仍在，待周检复核官网。Windscribe“需确认邮箱且订阅推广邮件才享 10 GB”仍为周检备注。
6. PrivadoVPN：Play 列表 2026-11-05 更新，免费 10 GB/月，与库内一致，无变更。
7. Planet VPN：Play 列表 2026-11-03 更新，6 个地点/5 国，与库内一致，无变更。
8. ZeroPing VPN（Star Core Studio；2026-07 上线，100k+ 安装，v1.0.57，2026-11-12 更新）：免费含广告；仍无官网与独立隐私政策可核。继续监控（自 2026-11-13 延续）。
9. Shmel VPN & Network Tools（AZUR APPS FZ-LLC；2026-11 上架 Play，v1.1.18，2026-11-09 更新）：仍无官网与独立隐私政策可核。继续监控（自 2026-11-13 延续）。
10. TipTop VPN：Aptoide 列表 2026-11-06 发布，官网 tiptop-vpn.com 存在；但 10 月 14 日用户评价称更新后免费服务器被锁、仅剩 1 个且常无可用服务器，11 月 5 日评价状态不明。证据冲突，暂不入库，继续监控。
11. Happ - Proxy VPN：proxysvpn.com 2026-11-09 文章称其 Google Play 页面自 2026-11-03 起返回 404（美/德/俄商店）。该来源为竞品自家网站，单一来源未独立证实；Happ 未入库，本次不作 discontinued 记录，继续监控（自 2026-11-12 延续）。
12. FreeVPN.me：PrivacyAffairs 2026-11-03 更新评测明确建议避开——无具名运营方、无隐私政策、仅阿姆斯特丹 1 台服务器、OpenVPN 证书已于 2025-07-25 过期。排除，不入库。
13. SSH Afrika（Cursus Digital；2026-11 上架 Play，220 安装）：VLESS/SlowDNS/SSL 客户端工具（需自备配置），非自带服务器的 VPN 服务。排除。
14. VPN.lat（10M+…34M 安装，v3.9.64，2026-11-11 更新）：多年老牌免费应用，非 24–48h 新信息；近期用户评价反映新版有断连 bug。仍列为周检候选（评估是否补录），本次不入库。
15. VPN Super Unlimited Proxy（1B+ 下载，v2.36.0，2026-11-03 更新）、TLS Tunnel（v8.5.2，2026-11-05 更新）：均为多年老牌免费应用，仅常规版本更新；仍列为周检候选，本次不入库。
16. Aloha Browser（Aloha Mobile；10M+ 安装，v4.20.0，2026-11-10 更新）：内置免费不限量 VPN（浏览器内、无需注册，免费用户自动连最快服务器；80+ 位置为 Premium 功能），官网 alohabrowser.com 有隐私声明与 Leviathan Security Group 安全评审提及。非 24–48h 新服务（多年老产品），本次不入库，**新增为周检候选**（与已入库的 Opera 浏览器 VPN 同类）。
17. Le VPN 16 周年（2026-11-10）：向部分客户赠送 1 个月 Personal VPN（一次性促销，非免费档）。不作变更。
18. VPN Access（problembo.com，2026-11-02 公告停售）、LetsVPN（中国服务终止）、F-Secure FREEDOME（分阶段停用）：均为付费服务停售/停服，库内无条目且非免费档变更。不作 discontinued 记录。
19. iOS 20.2 NetworkExtension 破坏第三方 VPN 的说法（vpn-security-review.contentwave.net，2026-11 月初）：iOS 20.2 并不存在（当前为 iOS 26），来源不明，疑似 AI 生成内容。忽略。
20. Samsung Max、Atlas VPN、Google One VPN、Kaspersky 免费版：均已在 discontinued。→ 不作变更。
21. Anomi VPN：无恢复有效的可信证据，仍在 removed。→ 不作变更。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- TunnelBear 免费档服务器选择：库内记录 2026 年起免费档取消手动选服（自动分配）；Cybernews 2026-10-28 更新文章称 TunnelBear 是唯一不限制免费用户服务器数量的免费 VPN。两者冲突，需复核官网确认。（自 2026-11-09 延续）
- Hide.me 免费地点：vpnalert 2026-11 月榜单列出的 8 个免费地点中含新加坡而非芬兰；库内为 FI/FR/DE/NL/CH/UK/US。需复核。（自 2026-11-09 延续）
- PrivadoVPN 免费额度：库内为 10 GB/月全速后降速；fojilo 2026-11-01 文章称免费档仅 2 GB/月。两者冲突，需复核官网确认。（自 2026-11-10 延续）
- Windscribe 10 GB 条件：antivirusprotection.org 2026-11-07 称需确认邮箱且订阅推广邮件；库内仅写“确认邮箱”。周检时核对官网帮助中心。
- Firefox 内置 VPN：2027-02-01 00:00 UTC 恢复 50 GB/月已确认；待 2027-02 复核确认实际恢复情况。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。
- 大复核候选：EVPN、Touch VPN、ZoogVPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Skyvora VPN（已入库，移除）、Berry VPN（已入库，移除）、Shmel VPN、ZeroPing VPN、TipTop VPN、Aloha Browser（新增）。

## 同步

- Git 仓库：**推送失败，未完成**。本地提交 11679e3（“更新数据库：新增 Berry VPN 与 Skyvora VPN（36→38 条）”）已生成；三次推送均失败（sync.sh 一次 + 手动 git push 两次，间隔约 1 分钟），错误均为 `kex_exchange_identification: read: Connection reset by peer / Connection reset by 198.19.0.1 port 3128`。诊断：gits.d35.kdns.fr 解析为 198.18.9.96，2222 端口 TCP 可建立但对端不发送 SSH banner即关闭；非密钥/权限问题，是出口代理或 Gitea 服务端当时的网络故障。2026-11-13 推送曾成功，属新发故障。**待下次运行或网络恢复后重试推送**（sync.sh 下次运行会自动提交本次运行日志并一并推送）。
- Muse artifact 网页（mian-fei-vpn-shu-ju-ku）：artifact.edit 构建完成并通过校验（builder 回传 2026-11-14 02:52 UTC）：页面 DATA 为 38 条，Berry 与 Skyvora 卡片完整，CyberGhost 额度口径更新为不限量；家宽统计 4 家确认 + 2 家部分；removed 仍 1 条、discontinued 仍 5 条。**注意：本次构建尚未发布到公开链接——公开链接仍显示上一版（36 条），需用户明确要求重新分享才会更新。**

## 结论

- free-vpn-db.yaml：36 → 38 条 entries；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 5 条。
- Git 推送待重试（本地提交 11679e3 已就绪，远程未更新）。
- 下一次检索：明日 2026-11-15（free-vpn-db-daily-discovery）。
