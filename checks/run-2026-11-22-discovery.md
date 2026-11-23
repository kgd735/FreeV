# 每日新免费 VPN 检索 — 2026-11-22 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**无新增收录；无新增关停；YAML 未改动（仍为 41 条）；无需同步（页面与 git 均跳过）**。

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库；ghacks / betanews / makeuseof 等多篇 11 月 21–22 日转载均为同一消息，无新变更。
2. GoVPN 2.0：已在库；官网博文（2026-11-15 更新）无新增变更。
3. Proton VPN Free：已在库；FrankVPN 2026-11-15 核查一致（不限量、1 台、10 国含 SG；移动端访客模式，桌面端访客模式在 2026-10-21 路线图中有规划、无日期）。
4. Gizmodo 免费 Chrome 扩展榜单（2026-11-21 更新）：Proton / Windscribe / CyberGhost 均已在库，免费档口径与库内一致，无变更。
5. Atlas VPN：已在 discontinued（2024-04-24 关停）；2026-11-14/16 文章为旧闻回顾，无新增变更。
6. Samsung Max：已在 discontinued（2026-06-15 关停）；Toolradar 替代榜单无新增变更。
7. ClearVPN 免费档：官网支持页称 2024 年 3 月起取消免费档、仅留付费 Premium（3 天试用）。该变更发生在 2024 年，不在本次 24–48h 窗口内；ClearVPN 从未入库，列为周检候选，决定是否记入 discontinued（来源：https://support.clearvpn.com/hc/en-us/articles/360010638200-Why-can-t-I-access-my-free-version-of-ClearVPN）。
8. Surfshark 免费 Public DNS 将于 2026-11-24 关停（2026-11-20 宣布，11 月 21 日亦有报道）：免费 DNS 服务，非 VPN 免费档；Surfshark 不在库内（无免费 VPN 档），不改库。
9. ZenMate 免费浏览器扩展：zenmate.com 仍链接免费 Chrome 扩展（Kape 旗下，与已在库的 CyberGhost 免费扩展同类）；付费应用已于 2023 年并入 CyberGhost。单独建条目会重复，继续列为周检候选，本次不入库（来源：https://reviewedbypro.com/zenmate-vpn，2026-11-14 核查）。
10. VPN Gate 安卓客户端更新（2026-11-17/20）：仅常规版本更新，VPN Gate 条目已在库，无免费档变更。
11. VPN.lat / VPN - Super Unlimited Proxy / VPN - Net Speed Optimizer / VPN Proxy Shield：均为安卓免费 VPN 应用的常规版本更新（11 月 10–14 日），无新上线事件；无可核实的官网与隐私政策，继续列为周检候选，暂不入库。
12. ZeroPing VPN（com.zero.ping.vpn，Star Core Studio）：2026 年 8 月上线，AppBrain 显示 19 万安装、近 30 天新增约 14 万，v1.0.58 更新于 2026-11-16，免费广告支持路线、可选 Premium。本次检索未找到可核实的官网与隐私政策页（搜索结果混入同开发商另一产品 Star VPN / vpn131.com，勿混淆；亦与已在库的 StarVPN / starvpn.com 无关）。按既往标准（官网可核实前暂不入库），继续列为周检候选，重点观察其官网与隐私政策是否出现。
13. Free VPN by Free VPN .org（org.freevpn）：无 24–48h 内新信息；广告换时长模型细节仍未明确，继续列为周检候选，暂不入库。
14. SuperVPN Free VPN Client：仅常规版本更新，继续列为周检候选。
15. Anomi VPN（removed，2026-11-09）：本次复查——官网 anomivpn.com 仍无法访问（curl https:000），无服务恢复的有效证据。仍在 removed，不恢复入库。
16. PandaVPN Lite（com.pandavpnfree.androidproxy）：官网 pandavpn.com 本次 curl 仍超时未达（https:000），无恢复证据；继续列为周检候选，暂不入库。

## 新列入周检候选

- **EonVPN（eonvpn.com）**：Windows 专属免费 VPN，官网可达（curl 200，2026-11-22）。自称终身免费、无需信用卡、需创建免费账号、9 国 / 40+ 服务器（官网博客 2026-10/11 文章）；官网博客称服务“使用用户一小部分带宽供企业流量使用”（Hola/Urban VPN 式带宽共享模式，住宅 IP 归属与日志政策须重点核实）；自称严格无日志、无独立审计证据；流量额度与协议未明。服务至少自 2023 年已存在，非 24–48h 内新上线，故本次不直接入库，交周检做完整核实（隐私政策页、额度、协议、运营方/管辖区）再决定。
  来源：https://eonvpn.com/blog/discord-unblocked/、https://eonvpn.com/blog/vpn-for-spotify/、https://sourceforge.net/software/vpn/free-version/

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- Windscribe 10 GB 条件：antivirusprotection.org 2026-11-07 称需确认邮箱且订阅推广邮件；库内仅写“确认邮箱”。周检时核对官网帮助中心（自 2026-11-18 延续）。
- Firefox 内置 VPN：2027-02-01 00:00 UTC 恢复 50 GB/月已确认；待 2027-02 复核确认实际恢复情况。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。
- ZoogVPN：免费地点数以官网免费档页 5 国为准；若后续官网改回 3 国，以最新官网为准。
- UnblockMeVPN：免费访问为酌情提供、随时可取消；若官网撤下免费档页或停止免费节点，按关停处理。免费档设备数与流量额度官网未说明，复核时留意官网是否补充。
- ClearVPN 免费档取消（2024-03）是否记入 discontinued，周检决定。
- 大复核候选：EVPN、Touch VPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Shmel VPN、ZeroPing VPN、TipTop VPN、Aloha Browser、TrendVPN、Russian VPN / MEDVET VPN、USA VPN、TapTap VPN、ZenMate 免费扩展、TeknoVPN、PandaVPN Lite、Free VPN by Free VPN .org、SuperVPN Free VPN Client、EonVPN。

## 同步

- YAML 未改动：未运行 export-page-sync.js，未触发 artifact.edit，未运行 sync.sh（无变更自动跳过）。
- 公开页面链接仍显示 41 条版（2026-11-21 同步版）：https://muse.ai/s/mian-fei-vpn-shu-ju-ku-xhxd6xe0uxbxsp1n/524jt68zSApSIH5MC2nGlPSbeJuZFtOcaKCX54ZOr1s

## 结论

- free-vpn-db.yaml：entries 仍为 41 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 5 条；家宽 IP 仍为 6 家。
- 无新增收录、无新增关停，按任务要求保持安静，不向用户汇报。
- 下一次检索：明日 2026-11-23（free-vpn-db-daily-discovery）。
