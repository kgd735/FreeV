# 每日新免费 VPN 检索 — 2026-11-09 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（GoVPN）；无新关停记录；现有条目无实质变更**。

## 新增收录

### GoVPN（govpn.space；2026-11-02 推出 2.0 重制版）
- 去重：库内无 GoVPN 条目；removed 仅 Anomi VPN（2026-11-09 移除，官网 DNS 无法解析），discontinued 无记录。→ 可入库。
- 核实（2026-11-09，官网实抓）：
  - 官网：https://www.govpn.space；博客 https://www.govpn.space/blog/govpn-2-launch（2026-11-02，2.0 向 iOS/Android 推出，免费档保留）
  - 免费档：$0/forever；Play 商店描述称不限流量/不限时；免费 = 部分服务器位置、标准速度、含广告；免注册、无需信用卡
  - 免费国家数：部分位置（数量未披露）；完整 50+ 国家为 Premium（$4.99/月，$39.99/年）
  - 设备数：未明示（多设备列为 Premium 功能，暂记 1）
  - 协议：OpenVPN + AES-256；自称 300+ 服务器、500K+ 用户、4.8 星
  - IP 类型：机房 IP（residential_ip: false；自有服务器，无住宅/P2P 功能）
  - 日志/审计：官网自称严格无日志，**无独立审计**；运营方 Nextgen Networks Slt Limited（司法辖区未披露）；Google Play 应用 com.free.vpn.turbo.fast.secure.govpn，约 20 万条评价，4.5 星，2026-09-18 更新
  - 平台：Android、iOS（仅移动端）
  - 来源：官网 + 2.0 博客 + Google Play 官方上架描述
- 变更：YAML entries 29 → 30（id: govpn，last_verified 2026-11-09）。注：今晨每周复核（run-2026-11-09.md）已将 Anomi VPN 移入 removed，故入库前基数为 29。

## 检查到的候选（均排除）

1. NovaRoute VPN（AppBrain，2026-10 上线 Google Play）：VPN 访问需订阅，仅 3 天免费试用，无永久免费档。→ 不收录。
2. Free mVPN（Iliad，2026-10-15 新闻稿）：法国 Free 电信手机套餐内置 VPN，非独立免费档。→ 不收录。
3. NymVPN v2026.8（2026-11-08）：Linux 分流与 Android 广告拦截功能更新，付费服务，无免费档。→ 不收录。
4. Ninja VPN（bessy 2026-11-05 更新）：俄罗斯/伊朗/中国停服为 2026-09-12 事件，窗口之外；仍列入监控候选。→ 不收录。
5. Avast VPN Free：已在库中；Techno360 2026-11-05 实测与库内记录一致（法国 11-04 推出、3 个自选地区锁定、印度不可用、500GB vs 不限量冲突待澄清）。→ 无变更，留待每周复核。
6. Proton VPN（privacyaffairs 2026-11-07 更新评测）：免费档不限量、1 设备、10 国，与库内一致。→ 无变更。
7. Problembo "VPN Access is being discontinued"（2026-11-02）：Telegram 机器人售卖的付费 VPN 接入停售，非免费档，昨日运行已记录。→ 不作变更。
8. F-Secure FREEDOME（付费产品逐步停服，Win/Mac 支持至 2026-09-11）：非免费档。→ 不作变更。
9. Samsung Max（2026-06-15 关停）、Atlas VPN（2024-04-24 关停）、Google One VPN（2024-06 关停）：均已在 discontinued。→ 不作变更。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- TunnelBear 免费档服务器选择：库内记录 2026 年起免费档取消手动选服（自动分配）；Cybernews 2026-10-28 更新文章称 TunnelBear 是唯一不限制免费用户服务器数量的免费 VPN。两者冲突，需复核官网确认。
- Hide.me 免费地点：Gizmodo 与 vpnalert 列出的 8 个免费地点中含新加坡而非芬兰；库内为 FI/FR/DE/NL/CH/UK/US。需复核。

## 同步

- Muse artifact 网页（mian-fei-vpn-shu-ju-ku）：已触发 artifact.edit 同步（快照 notes/db-sync.md，30 条）；构建结果待 handoff 回报。
- Git 仓库：sync.sh 已提交并推送到 origin main（commit 324d2f8，05397ed..324d2f8）。注：提交信息中 `$0` 被 shell 展开为 `/bin/bash`（"免费档 /bin/bash/forever"），仅提交信息文字瑕疵，YAML 内容无误，未改写历史。

## 结论

- free-vpn-db.yaml：29 → 30 条 entries；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 4 条。
- 下一次检索：明日 2026-11-10（free-vpn-db-daily-discovery）。
- 大复核候选：Firefox 免费内置 VPN、EVPN、Touch VPN、ZoogVPN、BearVPN、Ninja VPN。

## Artifact 同步结果（handoff 回报）
- 构建成功并通过核验：页面 DATA 数组 30 条，与 YAML 一致；GoVPN 已按 YAML 原值补入，家宽 4+2、停服表 6 行一致。
- 注意：构建已完成，但公开链接仍展示旧版（current_build_published=false）；公开链接需用户明确要求重新分享才会更新，卡片内打开的页面为最新版。
