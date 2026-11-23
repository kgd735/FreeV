# 每周免费 VPN 数据库复核 — 2026-11-23 (weekly check)

- 范围：全部 41 条 active 条目官网可达性检查 + 免费档现状核实；上次全库复核 2026-11-16。
- 结果：**有变更并已同步**。YAML：41 → 42 条；removed 仍 1 条（Anomi VPN）；discontinued 5 → 6 条；家宽 IP 6 → 7 家。

## 官网可达性（scripts/check-urls.js，checks/check-20261123-0148.json）

- 41 条中 39 条 200 OK；2 条失败，均已核实为误报：
  - Speedify：403（反爬）。官网博客 2026-11-18 更新确认免费档 5 GB/月仍在。
  - VPN Gate：fetch failed（本机网络问题）。官网实测正常（browser.open 2026-11-23 01:49 UTC），3413 台公开中继服务器在列。

## 本次变更（均已写入 YAML，last_full_review → 2026-11-23，全库 last_verified → 2026-11-23）

1. **新增 EonVPN（eonvpn.com）**——2026-11-22 每日检索列入的周检候选，本周完成核实后入库：
   - 终身免费、Windows 专属、无需信用卡、需创建免费账号；40+ 服务器、8+ 国家（US/UK/DE/CA/FR/NL/SG/AU）；v2.2、441k+ 注册用户；成立于 2022 年，美国（SourceForge 公司信息）。
   - **带宽共享模式**（官网原话：免费靠“分享一小部分带宽供企业流量使用”），Hola / Urban VPN 同类 → residential_ip: true，条目内已醒目标注。
   - 风险点：eonvpn.com 上**找不到独立隐私政策页**，无日志承诺仅见于官网 FAQ；无独立审计；协议未公开。已如实记入 logging 字段。
   - 来源：https://eonvpn.com/、https://sourceforge.net/software/product/EonVPN/、https://reviews.financesonline.com/p/eonvpn
2. **hide.me Free：免费地点 7 → 8**——官网定价页与免费页均已改为 8 locations（2026-11-23 实测）；具体国家未列出。2026-11-16 周检按评测定的 7 国口径（FI/FR/DE/NL/CH/UK/US，新加坡付费）已过时，以官网为准。
   - 来源：https://hide.me/en/pricing、https://hide.me/en/free-vpn
3. **Windscribe Free：10 GB 条件订正**——10 GB 需确认邮箱**且保持订阅推广邮件**（每月 1–2 封），退订后降回 2 GB（知识库 2025-11-05 文章；vpnclue 2026-11-12/20、cyberpresso 2026-11-04 核查一致）。官网免费页称“Not to market at you”，与知识库冲突，以知识库为准。免费国家数订正为 10（US/CA/UK/HK/FR/DE/NL/CH/NO/RO）。
   - 来源：https://vpnclue.com/vpn/windscribe/free/、https://cyberpresso.com/blog/windscribe-pricing
4. **Speedify Free：5 GB 账号条件订正**——官网博客 2026-11-18 确认 5 GB/月仍在；reviewedbypro（2026-11-11）与 vpncomparison（2026-11-03）核查官网下载页后均称无需账号即可用 5 GB，旧的“未注册 2 GB”说法现存疑，已在条目中标注为争议。
   - 来源：https://speedify.com/blog/news/introducing-free-tier/、https://reviewedbypro.com/speedify、https://www.vpncomparison.org/provider/speedify/
5. **TunnelBear Free：自动选服起始时间订正**——2026 年初 → 2025-12-03（operavpn.com 2026-11 榜单）；2 GB/月、不可手动选服不变。
6. **ClearVPN 记入 discontinued**——免费档 2024-03 取消，仅留付费 Premium（3 天试用）；此前从未入库，本周决定记入停服记录。
   - 来源：https://support.clearvpn.com/hc/en-us/articles/360010638200-Why-can-t-I-access-my-free-version-of-ClearVPN

## 核实无变更（抽查/搜索确认）

- Proton / TunnelBear / Hotspot Shield 等主流免费档与 2026-11-13–20 的多家榜单一致，无免费档变更；Proton VPN Plus 月付价 2026-11-03 由 $6.99 涨至 $9.99，属付费档，不改库。
- Avast 免费 VPN：VerSprite 无日志审计报告截至 2026-11-23 仍未发布（freedownload.co.in 2026-11-05、Gizmodo 2026-11 评测均确认未见报告），条目内“首份报告预计 2026-11”表述保留，无需改动。
- X-VPN Talaria 协议：2026-11 已有“200% 提速”营销说法，无免费档字段变更。
- Firefox 内置 VPN 不限量优惠至 2027-01-31、2027-02-01 恢复 50 GB/月：已在库，待 2027-02 复核确认实际恢复情况。
- Ninja VPN 官网与 Play 列表内容不一致：本周无新证据，下次复核再核对。
- ZoogVPN（5 国，以官网免费页为准）、UnblockMeVPN（免费档为酌情提供、随时可取消）：本周无新变化。
- Anomi VPN（removed）：2026-11-22 复查官网仍不可达，无恢复证据，不恢复入库。

## 本周决定不入库 / 不单独立条

- **ZenMate 免费浏览器扩展**：zenmate.com 仍链接免费 Chrome 扩展（Kape 旗下，与已在库 CyberGhost 免费扩展同类；付费应用已于 2023 年并入 CyberGhost）。单独建条目会重复，不入库，记录在此。
- 其余 2026-11-22 每日检索列出的候选（EVPN、Touch VPN、BearVPN、ZeroPing VPN、PandaVPN Lite 等）：无可核实的官网/隐私政策或无新上线事件，继续观察，暂不入库。

## 同步

- Muse artifact 网页：已运行 export-page-sync.js（42 条快照），artifact.edit 已触发（slug: mian-fei-vpn-shu-ju-ku），构建成功（2026-11-23 01:57 UTC 回执）：页面 DATA 数组验证通过——42 条，residential true 5 家（URnetwork、Urban VPN、tuxlerVPN、Hola、EonVPN）+ partial 2 家（StarVPN、VPN Gate），与 YAML 一致；停服表已补 ClearVPN（6 条）；五条变更已落卡；搜索/筛选/排序脚本未改动。
- **注意：公开链接尚未更新**——本次构建 current_build_published=false，公开链接仍显示上一版（41 条）。发布新版需用户批准新的 artifact.share，本次执行未调用（无显式重新分享指令）。卡片打开的是用户自己 Muse 内的新版页面；公开链接是另一份副本，需用户决定是否重新分享。
- Git：sync.sh 已执行，提交 b63258a 已推送至 origin main（kgd735/FreeV.git）。
- 公开页面链接：https://muse.ai/s/mian-fei-vpn-shu-ju-ku-xhxd6xe0uxbxsp1n/524jt68zSApSIH5MC2nGlPSbeJuZFtOcaKCX54ZOr1s（目前仍为 41 条版，待重新分享后显示 42 条版）

## 结论

- free-vpn-db.yaml：entries 42 条；removed 1 条；discontinued 6 条；家宽 IP 7 家（新增 EonVPN）。
- 下一次复核：2026-11-30（每周一）。
