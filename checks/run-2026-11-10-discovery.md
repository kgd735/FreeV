# 每日新免费 VPN 检索 — 2026-11-10 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 2 条（Vessel、Firefox 内置 VPN）；无新关停记录；现有条目无实质变更**。

## 新增收录

### 1. Vessel（vessel.anoni.net；anoni.net 社群 VPN，2026-11-07 公告发布）
- 去重：库内无 Vessel 条目；removed 仅 Anomi VPN（anomivpn.com，2026-11-09 移除）——注意 anoni.net 与 Anomi VPN 无关（域名、运营方均不同）；discontinued 无记录。→ 可入库。
- 核实（2026-11-10，官网实抓）：
  - 官网：https://vessel.anoni.net；公告 https://anoni.net/en/updates/2026/11/2026-vessel-launch/（发布 2026-11-07；首批邀请码 2026-10-28 发出，现为邀请制开放）
  - 免费档：完全免费，无需付费、无需邮箱；每账户 50 GB/月；邀请码制（发给 anoni.net 电子报订阅者；账户满 14 天且有设备连线后可再邀请）
  - 免费国家数：3 个节点城市（台北、东京、新加坡；可选中继路线「台北入口 → 任一节点」）
  - 设备数：未明示（按设备逐个建配置）
  - 协议：AmneziaWG（开源 WireGuard 分支，带流量伪装）
  - IP 类型：机房 IP（residential_ip: false；台北节点托管于 Greenhost 台北机房，东京/新加坡为其他服务商）
  - 日志/审计：自称不记录目的地与时间、DNS 解析器不记查询、节点防火墙日志已关；**无独立审计**；代码与主机配置开源于 GitHub；条款与隐私政策仍为草稿；社群志愿者运营，可能中断
  - 平台：经 AmneziaWG App 接入（桌面与手机；Windows/macOS/Linux/Android/iOS）
  - 附加功能：DNS 过滤（HaGeZi 名单 + 台湾 165 反诈名单、数位部诈骗购物网站名单；可选广告与追踪拦截）
  - 来源：官网 + 官方公告
- 变更：YAML entries 30 → 32 之一（id: vessel，last_verified 2026-11-10）。注：公告发布于 2026-11-07，昨日检索未发现，本次首次检出。

### 2. Firefox 内置 VPN（Mozilla；2026-03-24 随 Firefox 149 推出）
- 去重：库内无 Firefox/Mozilla 条目；removed/discontinued 无记录。→ 可入库。
- 说明：该服务 2026 年 3 月即已上线，本次补录属于补齐库内长期缺失的重大免费档（昨日运行已将其列为「大复核候选」）；窗口内新信息为 2026-11-03 CNET 综述、2026-11-04 WindowsForum 详解、2026-11-09/10 Gizmodo 与其余 11 月榜单的持续覆盖。
- 核实（2026-11-10，Mozilla 官方博客 + Connect 公告实抓）：
  - 官网/公告：https://blog.mozilla.org/en/firefox/built-in-vpn/；https://connect.mozilla.org/t5/discussions/introducing-firefox-s-built-in-vpn-ip-protection-now-in-the/m-p/120550
  - 免费档：50 GB/月（桌面与手机共享额度；用完暂停至下月）；需免费 Mozilla 账户；无需信用卡
  - 免费国家数：29 个上线国家（2026-07 更新）；桌面端 6 个可选位置（US、CO、DE、JP、ZA、AU）
  - 设备数：1（Mozilla 账户；桌面 + Android 共享额度）
  - 协议：经 Fastly 服务器的 TLS 加密代理——仅覆盖 Firefox 浏览器内流量，**不是全设备 VPN**（全设备版为付费 Mozilla VPN）
  - IP 类型：机房 IP（residential_ip: false；Fastly 数据中心代理 IP）
  - 日志/审计：Mozilla 称不出售浏览数据、不注入广告；代理商向 Mozilla 提供汇总用量以显示月度用量；**未找到针对该功能的独立审计**
  - 平台：Firefox 149+ 桌面（Windows/macOS/Linux）、Firefox 156+ Android；暂无 iOS
  - 来源：Mozilla 官方博客 + Connect 公告 + Gizmodo 指南
- 变更：YAML entries 30 → 32 之二（id: firefox-vpn，last_verified 2026-11-10）。

## 检查到的候选（均排除 / 无变更）

1. GoVPN 2.0：昨日刚入库；无新动态。→ 无变更。
2. Vivaldi + Proton VPN 集成：2026-11-10 出现的 thevergetoday 文章为 2025 年 3 月桌面集成的旧闻复述；真实新动态是 2026-10 Android snapshot 加入 Proton VPN（Vivaldi 官方帮助页已上线）。属 Proton 免费档的分发扩展，免费档条款本身无变化。→ Proton 条目不作变更。
3. StarVPN 2.46（2026-11-04）：版本更新而已，免费档（100GB/月、免注册）与库内一致。→ 无变更。
4. Opera 免费 VPN 自动开启公共 Wi-Fi 功能（2026-09-24）：功能更新，免费档不限量不变；库内已有该记录。→ 无变更。
5. Ninja VPN（bessy 2026-11-05 更新）：免费 Android 应用（免注册、不限量、广告、单会话 6 小时），但 2026-09-12 起已在俄/伊/中停服；无独立官网（仅 Google Play 上架）。继续列为监控候选，本次不入库。
6. LetsVPN 在中国停服（letsvpnshutdown.com）：付费 VPN，未入库，与免费档无关。→ 不作变更。
7. Problembo「VPN Access 停售」（2026-11-02）：Telegram 机器人售卖的付费 VPN 接入，昨日已记录。→ 不作变更。
8. F-Secure FREEDOME 逐步停服（Win/Mac 支持至 2026-09-11，Android/iOS 至 2027-03）：付费产品，非免费档。→ 不作变更。
9. Samsung Max（2026-06-15 关停）、Atlas VPN（2024-04-24）、Google One VPN（2024-06）：均已在 discontinued。→ 不作变更。
10. CyberGhost 免费浏览器扩展（vpnalert 2026-11 榜单提及：Chrome/Firefox 扩展，US/DE/NL/RO，免注册）：浏览器代理形态，尚未核对官方页面。列为每周复核候选，本次不入库。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- TunnelBear 免费档服务器选择：库内记录 2026 年起免费档取消手动选服（自动分配）；Cybernews 2026-10-28 更新文章称 TunnelBear 是唯一不限制免费用户服务器数量的免费 VPN。两者冲突，需复核官网确认。（自 2026-11-09 延续）
- Hide.me 免费地点：vpnalert 列出的 8 个免费地点中含新加坡而非芬兰；库内为 FI/FR/DE/NL/CH/UK/US。需复核。（自 2026-11-09 延续）
- PrivadoVPN 免费额度：库内为 10 GB/月全速后降速；fojilo 2026-11-01 文章称免费档仅 2 GB/月。两者冲突，需复核官网确认。（新增）
- CyberGhost 免费浏览器扩展：核对官方免费扩展条款（国家数、是否需账户、是否为代理）后决定是否入库。（新增）

## 同步

- Muse artifact 网页（mian-fei-vpn-shu-ju-ku）：已触发 artifact.edit 同步（快照 notes/db-sync.md，32 条）。
- Git 仓库：sync.sh 已提交并推送到 origin main。

## Artifact 同步结果（handoff 回报）
- 构建成功并通过核验：页面 DATA 数组 32 条，与 YAML 一致；Vessel 与 Firefox 内置 VPN 卡片均在位，额度/节点/协议/日志/来源均按 YAML 原值抄录；无删除、无新增停服（removed 仍 Anomi 1 条、discontinued 仍 4 条）；家宽统计不变（4 家 + 部分 2 家）；三项来源冲突（TunnelBear 选服、hide.me 免费地点、PrivadoVPN 额度）已加入「尚未核实」区；2026-11-09 变更记录完整保留。
- 注意：构建已完成，但公开链接仍展示旧版（current_build_published=false）；公开链接需用户明确要求重新分享才会更新，卡片内打开的页面为最新版。

## 结论

- free-vpn-db.yaml：30 → 32 条 entries；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 4 条。
- 下一次检索：明日 2026-11-11（free-vpn-db-daily-discovery）。
- 大复核候选：EVPN、Touch VPN、ZoogVPN、BearVPN、Ninja VPN、CyberGhost 免费浏览器扩展。
