# 每日检索运行日志 — 2026-11-27

- 检索窗口：过去 24–48 小时（2026-11-25 ~ 2026-11-27）。
- 检索方式：网络搜索（新上线免费 VPN、免费档关停/取消、免费额度变更）+ Product Hunt / Nicheloom 新品。

## 新增收录（1 条，48 → 49 条）

**HotaruNet**（id: hotarunet）
- 官网：https://oneforallhub.github.io/HotaruNet/ ；GitHub：https://github.com/OneForAllHub/HotaruNet
- 免费档要点：完全免费、无广告、免账号、零配置；内置去中心化社区订阅节点，自动按实测下载速度在 VLESS REALITY / Cloudflare WARP / Hysteria 2 / XHTTP / WS+TLS 间切换；官网未声明流量上限；节点覆盖欧洲/美国/亚洲（具体数量未披露）。
- 平台：Android 7–15、Windows 10/11（便携版）。
- IP 类型：residential_ip = unknown（出口为社区节点 + Cloudflare WARP 混合，运营方与 IP 来源未披露）。
- 日志/审计：客户端自称零浏览日志、开源 GPL-3.0；无独立审计；出口节点为第三方，日志情况未知（已在条目中标注 VPN Gate 式不可信出口提示）。
- 证据日期：2026-11-21 Product Hunt 上线；v2.3.44 发布于 2026-11-24；官网与 GitHub 于 2026-11-27 核实。
- 来源：官网、GitHub、Product Hunt、LowEndTalk 帖子（见 YAML sources）。

## 候选但未收录

- **Vulcain VPN**（2026-11-19 上线）：仅 7 天免费试用，无永久免费档；付费 €1.95/周起。跳过。
- **VibeVPN**（iOS，2026-11-11 上线）：“免费开始”但无任何可核实的免费档条款（无额度、无国家数、无注册要求说明）；官网“已审计”等说法无佐证。证据不足，继续监控，不入库。
- **EasyGuard VPN**（2026-11-23 上线）：纯付费，无免费版/试用（SourceForge 对比页确认 Free Version Not Supported）。跳过。
- **Oxyn VPN**：仅 15 天免费试用，非免费档。跳过。
- **Megamesh.sh / Pangolin / TestOps Gate / vpn-tunnel-tool**：自托管工具/客户端，非 VPN 服务。跳过。
- **HotaruNet 之外的 Product Hunt 新品**：均为上述类别。

## 已入库、无实质变更

- **Firefox 内置 VPN**：11 月 10 日起假日不限量（至 2027-01-31）已于 11 月 10 日入库，本次多家媒体复述同一消息，无新变化。
- **GoVPN 2.0**（2026-11-21 发布）：官方称“免费档保持免费”，无额度变更。
- **EthicalVPN / Amnezia Free / EventVPN**：均于 2026-11-26 入库，无新动态。
- **Proton VPN Free**：免费档不变（1 设备、10 国、不限制流量）。

## 关停核查

- **Betternet**：acciyo 一篇 SEO 文称“不再免费”，与 Betternet 官网支持页（2026-10-11 读数）矛盾——免费档仍存在（500MB/天、4 个虚拟位置、1 台设备、广告支持）。该文无官网依据，不采信，条目保持 active。注：第三方聚合页称免费位置为 4 个（数据库现记 3 个），证据为二手来源，留待每周复核对照官网核实。
- **GenerousVPN**（已停运、用户迁往 Windscribe）、**Supernet VPN**（已停运）：两家均从未进入 entries/removed/discontinued；acciyo 文章未给出可靠停运日期，不新增 discontinued 记录。
- **ClearVPN / SurfEasy**：已在 discontinued，无变化。

## 同步

- YAML：校验通过（`node scripts/build.js`：49 entries，49 active，7 residential）。
- Git：`bash sync.sh` 已提交并推送到 origin main（提交 112107c「新增 HotaruNet（2026-11-27，48→49 条）」）。
- Artifact 网页（slug: mian-fei-vpn-shu-ju-ku）：artifact.edit 同步构建已完成并校验通过（49 条，HotaruNet 卡片字段与 YAML 一致）。注意：公开链接仍显示上一共享版本，新构建需用户重新批准分享后才会更新公开链接。
