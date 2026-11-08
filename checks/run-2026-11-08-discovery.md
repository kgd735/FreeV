# 每日新免费 VPN 检索 — 2026-11-08 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（OkayFreedom VPN）；无新关停记录；现有条目无变更**。

## 新增收录

### OkayFreedom VPN（Steganos，2026-09 在 Google Play 上线 Android 免费应用）
- 去重：库内无 OkayFreedom 条目；removed 为空；discontinued 无记录。昨日（2026-11-07）运行已将其列为大复核候选，本次完成核实后入库。→ 可入库。
- 核实（2026-11-08）：
  - 官网：https://www.okayfreedom.com；Android 应用包名 com.steganos.freevpn，Google Play 上线 2026-09，最新版本 2026-09-16/18，约 970 次安装（AppBrain，数据更新 2026-11-03）
  - 免费档：Android 应用最高 30 GB/月——看一条奖励视频广告得 250 MB，每天最多 4 条，未用流量可跨日累积；无账号、无注册、无订阅、无需信用卡；连接时无广告；Windows 免费档为 2 GB/月（广告支持，旧有）
  - 协议：IKEv2/IPsec AES-256（Android 内置 VPN）
  - 地区：可自选国家（数量未披露）
  - IP 类型：机房 IP（residential_ip: false；Steganos 数据中心服务器）
  - 日志/审计：声称无活动日志；为计费与排障保留每连接记录（时间、时长、流量、所用服务器），最长 90 天删除；随机安装 ID，无账号关联；广告融资，收集假名化使用统计；无独立审计；德国 Steganos Software GmbH（自 1997 年）
  - 平台：Android 13+（新应用）；Windows（2 GB/月免费档）
  - 来源：Google Play 官方上架描述（厂商自述）+ https://www.appbrain.com/app/vpn-okayfreedom-secure-proxy/com.steganos.freevpn + 隐私政策 https://go.okayfreedom.com/privacy_android
- 变更：YAML entries 29 → 30（id: okayfreedom，last_verified 2026-11-08）；README.md 计数 29→30，新增速览行。

## 检查到的候选（均排除）

1. Touch VPN（Pango Group，privacyaffairs 2026-11-01 更新评测）：
   免费档长期存在（不限时、无需信用卡、Android 免账号、有广告、含广告追踪代码、扩展端 7 个免费国家），本次仅为评测更新，24–48h 内无实质变更；且与库内 Hotspot Shield / Betternet 同属 Pango/Aura 集团。→ 不收录。
2. ZoogVPN（vpnblade 2026-11-01 评测）：免费档 10 GB/月、1 设备、3–5 个地区，长期存在，非新信息；官网免费与付费额度说法不一致。→ 不收录，列入大复核候选。
3. Ninja VPN（bessy 2026-11-05 文章）：免费 Android 应用（40+ 国家、单会话最长 6 小时、广告+付费 Premium），开发商 Ninja VPN Ltd.（BVI）；2026-09-12 起在俄罗斯/伊朗/中国停服——事件在窗口之外，且为区域性停服而非免费档取消；运营主体与日志政策核实不足。→ 不收录，列入监控候选。
4. BearVPN（bearvpn.com 自有博客，2026-04/05 以来多篇文章）：移动端免费档不限量、无需注册、自动选服、50+ 地区、kill switch、分流；但证据全部来自厂商自有博客，无独立评测、审计或运营主体/司法辖区信息；服务至少自 2026-04 已存在，非 24–48h 新信息。→ 不收录，列入监控候选。
5. Avast VPN Free：已于 2026-11-07 入库；Techno360 2026-11-05 实测评测与库内记录一致（法国 11-04 推出、3 个自选地区锁定、印度不可用、500GB vs 不限量冲突待澄清）。→ 无变更。
6. ClearVPN（vpnblade 2026-11-01 评测）：永久免费档已于 2024-03 取消，现仅 3 天试用——旧闻，且从未在库中。→ 不作变更。
7. Problembo "VPN Access is being discontinued"（2026-11-02）：Telegram 机器人售卖的付费 VPN 接入停售，非免费档，且不在库中；昨日运行已记录。→ 不作变更。
8. Samsung Max（2026-06-15 关停）、Atlas VPN（2024-04-24 关停）、Google One VPN（2024-06 关停）：均已在 discontinued。→ 不作变更。

## 结论

- free-vpn-db.yaml：29 → 30 条 entries；removed 仍为空；discontinued 仍为 4 条。
- README.md：计数 29→30，新增 OkayFreedom 速览行。
- 下一次检索：明日 2026-11-09（free-vpn-db-daily-discovery）。
- 大复核候选：Firefox 免费内置 VPN、EVPN、Touch VPN、ZoogVPN、BearVPN、Ninja VPN。
- 待澄清：Avast 免费档数据上限（不限量 vs 500GB/月）与 VerSprite 首份审计报告（预计 2026-11），留待每周复核跟进。
