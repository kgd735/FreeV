# 每日新免费 VPN 检索 — 2026-11-12 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（Ninja VPN）；discontinued 新增 1 条（SurfEasy VPN，2026-09-01 关停）；无其他实质变更**。

## 新增收录

### 1. Ninja VPN（ninjavpn.app；Ninja VPN Ltd.，英属维尔京群岛，注册号 2161939）
- 去重：库内无 Ninja VPN 条目；removed 仅 Anomi VPN；discontinued 无记录。→ 可入库。
- 说明：昨日（2026-11-11）曾因「无独立官网」暂缓入库；本次核实确认官网 ninjavpn.app 可达（模板化站点），隐私政策/服务条款均载于该站（2026-09-12 更新），且 Bessy 2026-11-11 更新文章以一手来源交叉核实。→ 本次入库。
- 核实（2026-11-12，官网 + Play 列表实抓）：
  - 官网：https://ninjavpn.app（可达；但站点内容与 Play 列表不一致：官网称 500+ 服务器、Double VPN、10 台设备、OpenVPN/IKEv2，Play 列表未提及——以列表与服务条款为准，已记入 change_log）
  - 免费档：不限量、无需注册、无试用期；连接前播短广告；单会话最长 6 小时（断开后重连）；免费 40+ 国家（付费 60+）
  - 设备数：1（仅 Android；官网称订阅可 10 台，未采信）
  - 协议：WireGuard + 自研 Stealth 混淆（自动选择）
  - IP 类型：机房 IP（residential_ip: false；无住宅/P2P 功能宣称）
  - 日志/审计：自称不记活动日志、不存 IP/邮箱/连接时间；流量与会话时长以匿名安装标识临时处理；Google AdMob 广告（可个性化）、Firebase/Google Analytics；Play 数据安全栏：收集应用活动、性能数据、设备标识，数据不可删除；**无独立审计**；BVI 管辖
  - 平台：仅 Android 8.0+（iOS/Windows/浏览器扩展仅为计划中）
  - 规模：Google Play 10M+ 安装，146K 评价，v1.4.12（2026-10-12）
  - 区域限制：2026-09-12 起开发方主动停止在俄罗斯、伊朗、中国运营（俄罗斯 Play 商店已无安装按钮）
  - 同名混淆：另有 HEROIC 的 NinjaVPN（com.appbroker.ninjavpn）、ninjavpn.org 等同名产品，本条目为 Ninja VPN Ltd.（Play id app.ninjavpn.android），已在 change_log 注明
  - 来源：官网 + Play 列表 + Bessy 2026-11-11 文章
- 变更：YAML entries 34 → 35（id: ninja-vpn，last_verified 2026-11-12）。

## 关停记录

### SurfEasy VPN（discontinued 新增）
- 变更：2026-09-01 全面关停（含免费档）；符合条件的用户免费迁移至 Norton VPN（Gen Digital 旗下）。
- 证据：thebestvpnreviews 2026-10-16 文章（引 Norton 支持站关停公告，页面最后修改 2026-07-30）。注：关停日期在本次 24–48h 窗口之外，但为库内此前未记录的免费档关停，本次补记。
- 变更：discontinued 4 → 5（id: surfeasy-vpn，date 2026-09-01）。

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN：2026-11-10 至 2027-01-31 不限量已于昨日入库（last_verified 2026-11-11）；今日多家报道（piunikaweb、makeuseof、gadgetreview）内容一致，无新增变更。
2. GoVPN 2.0：已在库（2026-11-09 入库，2026-11-02 重启）；今日搜索结果为同一篇 11 月 6 日博文，无新增变更。
3. Le VPN 16 周年：向部分客户赠送 1 个月 Personal VPN（限时促销，非永久免费档）。跳过。
4. VPNhub（Pornhub 2018 年推出）：今日搜索结果为 2018 年旧闻翻发，非 24–48h 新信息。跳过。
5. Happ - Proxy VPN（ORDANA TOV；2026-10 上线 Play；28k 安装）：仅 AppBrain/Play 信息，无官网与隐私政策可核。列为监控候选，本次不入库。
6. Berry VPN（Coin Alarm；2026-10 上线；免费不限量、30 分钟会话）：仅 AppBrain/Play 信息，无官网与隐私政策可核。列为监控候选（自 2026-11-11 延续），本次不入库。
7. Proxiten（HexaSoftware；2026-10 上线；免费 2 小时/10 GB 会话）：仅 AppBrain/Play 信息，无官网。列为监控候选，本次不入库。
8. Skyvora VPN（Averon Soft；2026-09 上线；460k 安装，免费不限量）：仅 AppBrain/Play 信息，无官网。列为监控候选，本次不入库。
9. Northline VPN（Northline Technology；2026-10 上线；2.3k 安装）：信息过少，无官网。跳过。
10. VPN Access（problembo.com；2026-11-02 停售）：Telegram 机器人售卖的付费 VPN 接入，非免费 VPN 服务。跳过。
11. Samsung Max、Atlas VPN、Google One VPN：均已在 discontinued。→ 不作变更。
12. Anomi VPN：无恢复有效的可信证据，仍在 removed。→ 不作变更。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- TunnelBear 免费档服务器选择：库内记录 2026 年起免费档取消手动选服（自动分配）；Cybernews 2026-10-28 更新文章称 TunnelBear 是唯一不限制免费用户服务器数量的免费 VPN。两者冲突，需复核官网确认。（自 2026-11-09 延续）
- Hide.me 免费地点：vpnalert 列出的 8 个免费地点中含新加坡而非芬兰；库内为 FI/FR/DE/NL/CH/UK/US。需复核。（自 2026-11-09 延续）
- PrivadoVPN 免费额度：库内为 10 GB/月全速后降速；fojilo 2026-11-01 文章称免费档仅 2 GB/月。两者冲突，需复核官网确认。（自 2026-11-10 延续）
- CyberGhost 免费浏览器扩展：核对官方免费扩展条款（国家数、是否需账户、是否为代理）后决定是否入库。（自 2026-11-10 延续）
- Firefox 内置 VPN：2027-02-01 后额度是否恢复 50 GB/月，待 2027-02 复核确认。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。

## 同步

- Git 仓库：sync.sh 执行成功，commit a853f15 已推送到 origin main（Gitea ssh://git@gits.d35.kdns.fr:2222/kuangdash/FreeVPN.git）。
- Muse artifact 网页（mian-fei-vpn-shu-ju-ku）：artifact.edit 已派发构建，待回传结果核验（页面 DATA 应为 35 条，含 Ninja VPN 卡片；discontinued 应为 5 条，含 SurfEasy VPN）。

## 结论

- free-vpn-db.yaml：34 → 35 条 entries；removed 仍为 1 条（Anomi VPN）；discontinued 4 → 5 条。
- 下一次检索：明日 2026-11-13（free-vpn-db-daily-discovery）。
- 大复核候选：EVPN、Touch VPN、ZoogVPN、BearVPN、CyberGhost 免费浏览器扩展、ZapSplit VPN、Berry VPN、XNX VPN、Happ - Proxy VPN、Proxiten、Skyvora VPN。
