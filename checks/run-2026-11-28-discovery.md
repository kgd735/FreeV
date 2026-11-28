# 每日检索运行日志 — 2026-11-28

- 检索窗口：过去 24–48 小时（2026-11-26 ~ 2026-11-28）。
- 检索方式：网络搜索（新上线免费 VPN、免费档关停/取消、免费额度变更）+ Product Hunt / Nicheloom 新品。

## 新增收录（1 条，49 → 50 条）

**SparkProxy Free VPN**（id: sparkproxy-vpn）
- 官网：https://www.sparkproxy.io/free-vpn/
- 免费档要点：完全免费、无账号、无邮箱、无需信用卡；不限流量、不限设备；80+ 国家（官方 2026-11-26 Instagram/Facebook 广告）；免费的前提是设备开启带宽共享，关闭共享则免费访问暂停。
- 平台：Windows 10/11（64 位）、Android 10+、Linux 64 位 AppImage；暂无 iOS/macOS。
- IP 类型：residential_ip = partial——混合机房 + 住宅网络，出口按可用性从两者中分配；用户设备本身也会成为其他社区成员的住宅出口（仅 80/443 端口的网页连接）。
- 关键提示：严格意义上不是完整 VPN——Windows 上是系统 HTTP/HTTPS + SOCKS5 代理，Android 用 VPN 接口设置设备代理，Linux 设置桌面代理；不路由 UDP 流量（游戏、语音通话不受保护）。
- 日志/审计：服务条款明确写明“为所有用户记录连接信息”（运营、安全监控、反滥用；可依法披露给执法部门）；无 no-logs 承诺，无独立审计。
- 证据日期：官方广告 2026-11-26；官网与服务条款于 2026-11-28 核实。
- 注意：与 Google Play 上同名的 “Spark VPN”（Megabus Group / Gravity Global）是完全不同的产品，不要混淆；SparkProxy 的付费代理免费试用需政府证件验证，与免费 VPN 无关。
- 来源：官网 free-vpn 页、服务条款、官方 Instagram/Facebook 广告（见 YAML sources）。

## 候选但未收录

- **VpnHood! CONNECT**：免费档确实存在（Android 端免费服务器，不限流量/时长/速度、无需账号，广告资助；开源，宣称已审计），但服务本身并非 24–48 小时内新上线（项目已存在多年，2026-11-26 只是 APK 镜像站的版本更新 v3.2.448）；iOS/Windows/Linux 端免费服务器需购买 Premium 码。列为周检候选，留待 2026-11-30 周检评估是否补录，本次不入库。
- **NymVPN “free pass”**（2026-11-25 v2026.16）：QR 码激活的免费通行证是限时推广（此前为 Zcash 持币者提供 1 个月免费），非永久免费档；常规仍为 7 天试用（需绑卡）+ 付费订阅。跳过，继续监控。
- **VPN.lat**（v3.9.65，2026-11-24/25 更新）、**VPN - Super Unlimited Proxy**（v2.37.0，2026-11-26/27 更新）：均为多年老牌免费应用的常规版本更新，免费档无变化；此前已列为周检候选（2026-11-13、2026-11-22 决定），本次不入库。
- **Meow - Smart VPN**（iOS TestFlight）：自带订阅的代理客户端，不提供服务器。跳过。
- **Megamesh.sh / Pangolin / TestOps Gate**：自托管工具，非 VPN 服务。跳过。
- **Saudi Arabia VPN - Proxy**（2026-11-27 更新）：通用型国家 VPN 应用，仅 APK 镜像站信息，无官网/隐私政策可核实。证据不足，继续监控。
- **SafeGhost VPN**（Instagram 广告，2026-11-27）：“$0”但附“订阅自动续费”声明，实为试用，非免费档。跳过。
- **Vulcain VPN / Oxyn VPN / MiCore VPN / VibeVPN**：均为试用、无永久免费档或证据不足，此前已跳过，无新变化。

## 已入库、无实质变更

- **Firefox 内置 VPN**：11 月 10 日起假日不限量（至 2027-01-31）已于 11 月 10 日入库，本次多家媒体复述同一消息，无新变化。
- **GoVPN 2.0**：官方称“免费档保持免费”，无额度变更。
- **EthicalVPN / Amnezia Free / EventVPN / HotaruNet**：均已入库，无新动态。
- **Proton VPN Free**：免费档不变（1 设备、10 国、不限制流量）。

## 关停核查

- **Betternet**：acciyo 同一篇 SEO 文（更新于 2026-11 月）仍称“不再免费”，无官网依据，与 Betternet 官网支持页矛盾（免费档 500MB/天仍存在）；不采信，条目保持 active。
- **Surfshark 免费公共 DNS 服务** 2026-11-24 关停：关停的是免费 DNS 解析服务，不是 VPN 免费档，与本库范围无关，不记入 discontinued。
- **Atlas VPN / Samsung Max / ClearVPN / SurfEasy**：已在 discontinued，无变化。

## 同步

- YAML：校验通过（`node scripts/build.js`：50 entries，50 active，8 residential）。
- Git：`bash sync.sh` 已提交并推送到 origin main（提交 a4b6f43「更新数据库：新增 SparkProxy Free VPN（2026-11-28，49→50 条）」）。
- Artifact 网页（slug: mian-fei-vpn-shu-ju-ku）：artifact.edit 同步构建已完成并校验通过（50 条，SparkProxy 卡片字段与 YAML 一致；家宽 true 5 家、partial 3 家；停服 6 条、移除 1 条）。注意：公开链接仍显示上一共享版本，新构建需用户重新批准分享后才会更新公开链接。

## 周检候选（累计）

- EVPN、Touch VPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Shmel VPN、ZeroPing VPN、TipTop VPN、Aloha Browser、TrendVPN、Russian VPN / MEDVET VPN、USA VPN、TapTap VPN、ZenMate 免费扩展、TeknoVPN、PandaVPN Lite、Free VPN by Free VPN .org、SuperVPN Free VPN Client、EonVPN（已入库，移除）、VpnHood! CONNECT（新增）。
