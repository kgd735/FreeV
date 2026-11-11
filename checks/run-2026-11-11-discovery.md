# 每日新免费 VPN 检索 — 2026-11-11 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 2 条（Teal VPN、VPN PRO 89）；现有条目 1 条实质变更（Firefox 内置 VPN 额度临时不限量）；无新关停记录**。

## 新增收录

### 1. Teal VPN（tealvpn.com；Fxolio LLC，怀俄明州；2026-10 上线 Google Play）
- 去重：库内无 Teal 条目；removed 仅 Anomi VPN；discontinued 无记录。→ 可入库。
- 核实（2026-11-11，官网实抓）：
  - 官网：https://tealvpn.com；隐私政策 https://tealvpn.com/privacy（2026-11-10 更新）；条款 https://www.tealvpn.com/terms（2026-11-01 更新）
  - 免费档：500 MB/天；免费节点仅立陶宛 1 个（Pro 增加 DE/US/JP，全站 14 个位置）；2 台设备；需登录（Google/Apple/邮箱）；无需付款信息；无广告
  - 协议：自研 Teal Secure 协议（带流量混淆）
  - IP 类型：机房 IP（residential_ip: false；托管服务商服务器）
  - 日志/审计：自称不记浏览/DNS 日志、不存连接源 IP；保留登录标识、设备公钥与用量字节数；网站用 Google Analytics/Ads 标签；**无独立审计**；透明度数据为自报；运营方 Fxolio LLC（怀俄明州，美国）
  - 平台：Android、Windows、macOS、Linux、Android TV；iOS 仍在测试，未上架 App Store
  - 规模：Google Play 约 13k 安装，v1.2.57（2026-11-01 更新）
  - 来源：官网隐私政策/条款/指南 + AppBrain
- 变更：YAML entries 32 → 34 之一（id: teal-vpn，last_verified 2026-11-11）。

### 2. VPN PRO 89（vpnpro89.com；个人运营 Frank Wadskier；补录）
- 去重：库内无 VPN PRO 89 条目；removed/discontinued 无记录。→ 可入库。
- 说明：该服务 2026-09 即已发布（Linux beta 2026-09-08、Android 稳定版 2026-10-30），本次为补录库内缺失的免费档；属捐赠资助、无付费档的特殊形态，与 Firefox 内置 VPN 昨日补录同类。
- 核实（2026-11-11，官网实抓）：
  - 官网：https://www.vpnpro89.com/en/
  - 免费档：完全免费，无付费档、无人为限额、无广告；无需账户/邮箱/信用卡；捐赠自愿，不影响功能
  - 免费国家数：未公开具体数量（节点目录按国家列出；自有节点 + 第三方社群节点）
  - 设备数：1（无账户，按安装计）
  - 协议：VLESS + XTLS-Reality（全平台）、Shadowsocks（Android）、Tor 路由；基于开源 Xray-core
  - IP 类型：机房 IP（residential_ip: false；自有托管节点；社群节点由第三方运行）
  - 日志/审计：自有节点自称不记连接/目的地/内容；社群节点日志情况未知；网站与节点目录代理保留 IP/日期/路径约 5 周；App 内无分析/广告 SDK；**无独立审计**；单一自然人运营
  - 平台：Android 8.0+（稳定版，全系统隧道）；Windows beta、Linux beta（均为本地代理模式）；macOS 仅经 MCP；无 iOS
  - 来源：官网首页
- 变更：YAML entries 32 → 34 之二（id: vpn-pro-89，last_verified 2026-11-11）。

## 现有条目实质变更

### Firefox 内置 VPN（firefox-vpn）
- 变更：Mozilla 于 2026-11-10 宣布取消免费档流量上限，2026-11-10 至 2027-01-31 期间不限量（假日推广）；需 Mozilla 账户；2027-02-01 后是否恢复 50 GB/月上限未公布。
- 证据：ghacks 2026-11-10 报道（引 Mozilla 博客公告）；technobezz、hacks.gr、ChoiceCheapies 同日报道。注：Mozilla 博客原文页本次抓取未见 11 月 10 日更新段落，以多家独立报道交叉确认。
- 附带修正：免费国家数仍为 29 个；位置选择按 Mozilla 2026-05-19 更新为「可任选已上线国家」，库内原「桌面端 6 个可选位置」说法改为该表述（与 Mozilla 原文一致）。
- 变更：data_cap、countries、change_log、last_verified 更新为 2026-11-11。

## 检查到的候选（均排除 / 无变更）

1. ZapSplit VPN（FLOWBOX LIMITED；2026-10 上线 Play；免费不限量、4 Mbps）：仅 AppBrain/Play 信息，无官网与隐私政策可核。列为监控候选，本次不入库。
2. Berry VPN（Coin Alarm；2026-10 上线；免费不限量、30 分钟会话）：仅 AppBrain/Play 信息，无官网与隐私政策可核。列为监控候选，本次不入库。
3. XNX VPN（Noventra Tech；2026-10 上线；免费，法兰克福节点）：仅 AppBrain/Play 信息，无官网。列为监控候选，本次不入库。
4. Hero VPN（R International；2026-10 上线；仅 140 安装）：信息过少，无官网。跳过。
5. VPN Master（Albonik LLC；2026-10 上线）：实为 VPN Gate 公共节点的客户端，VPN Gate 已在库。跳过。
6. TLS Tunnel：老牌配置工具（非 VPN 服务本身），非新服务。跳过。
7. Ninja VPN（bessy 2026-11-05 更新）：2026-09-12 起俄/伊/中停服，服务本身仍在；无独立官网。继续监控，本次不入库。
8. Samsung Max（2026-06-15 关停）、Atlas VPN、Google One VPN：均已在 discontinued。→ 不作变更。
9. CyberGhost 免费浏览器扩展：仍未核对官方页面，继续列为每周复核候选。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- TunnelBear 免费档服务器选择：库内记录 2026 年起免费档取消手动选服（自动分配）；Cybernews 2026-10-28 更新文章称 TunnelBear 是唯一不限制免费用户服务器数量的免费 VPN。两者冲突，需复核官网确认。（自 2026-11-09 延续）
- Hide.me 免费地点：vpnalert 列出的 8 个免费地点中含新加坡而非芬兰；库内为 FI/FR/DE/NL/CH/UK/US。需复核。（自 2026-11-09 延续）
- PrivadoVPN 免费额度：库内为 10 GB/月全速后降速；fojilo 2026-11-01 文章称免费档仅 2 GB/月。两者冲突，需复核官网确认。（自 2026-11-10 延续）
- CyberGhost 免费浏览器扩展：核对官方免费扩展条款（国家数、是否需账户、是否为代理）后决定是否入库。（自 2026-11-10 延续）
- Firefox 内置 VPN：2027-02-01 后额度是否恢复 50 GB/月，待 2027-02 复核确认。

## 同步

- Muse artifact 网页（mian-fei-vpn-shu-ju-ku）：待触发 artifact.edit 同步（快照 notes/db-sync.md，34 条）。
- Git 仓库：待运行 sync.sh 提交并推送到 origin main。

## 结论

- free-vpn-db.yaml：32 → 34 条 entries；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 4 条。
- 下一次检索：明日 2026-11-12（free-vpn-db-daily-discovery）。
- 大复核候选：EVPN、Touch VPN、ZoogVPN、BearVPN、Ninja VPN、CyberGhost 免费浏览器扩展、ZapSplit VPN、Berry VPN、XNX VPN。
