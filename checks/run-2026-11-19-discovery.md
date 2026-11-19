# 每日新免费 VPN 检索 — 2026-11-19 (discovery run)

- 范围：过去 24–48h 与免费 VPN 相关的新信息（新上线、新增免费档、关停/取消、额度重大变更）
- 结果：**新增收录 1 条（Grass VPN）；无新增关停；YAML 由 38 条增至 39 条；已触发 artifact 页面同步与 git 推送**。

## 新增收录

### Grass VPN（id: grass-vpn）— 2026-11-19 入库
- 官网：https://freevpngrass.com（本次 curl 200；隐私政策 https://freevpngrass.com/privacy/ 可达，末次更新 2023-05-04，运营方 A24Z LTD）
- 免费档：不限量、无时间限制（免费会话 1 小时，可即时重连）；4 国（US / DE / FR / TR，可手动选或自动）；免注册、无需邮箱；无需信用卡；广告支持（Premium 去广告）
- IP 类型：datacenter（VLESS + Reality，无家宽/住宅 IP 功能）
- 日志：隐私政策称不记录可关联到用户的浏览活动，IP 仅会话期间使用、不存储；免费版广告网络收集 AAID/IDFA 与设备信息；无独立审计；运营方 A24Z LTD（伦敦，英国）
- 平台：Android 7.0+ only
- 证据：Play 列表 v2.2.32（2026-11-01 更新），69 万安装，3.89 分（1,782 评价）；2024-09 上线；近 30 天日均 800 安装
- 入库依据：2026-11-18 列为周检候选（当时无可核实官网与隐私政策）；2026-11-19 官网与隐私政策均已核实，达到收录标准（与 Berry/Skyvora 2026-11-14 的入库路径一致）
- 来源：https://freevpngrass.com/、https://freevpngrass.com/privacy/、https://www.appbrain.com/app/grass-vpn-unlimited-vpn-proxy/com.freevpn.vpngrass、https://play.google.com/store/apps/details?id=com.freevpn.vpngrass

## 检查到的候选（均排除 / 无变更）

1. Firefox 内置 VPN 不限量（2026-11-10 至 2027-01-31）：已在库。新增信息：Mozilla 曾因疑似第三方应用滥用临时关闭伊朗地区的免费 VPN 约 24 小时，现已恢复（wirebyte 2026-11-11）——临时区域性中断、已恢复，非关停，不改库。
2. GoVPN 2.0：已在库；官网博文（2026-11-13）无新增变更。
3. Atlas VPN：已在 discontinued（2024-04-24 关停）；neiro-subnetic 2026-11-14 文章为旧闻回顾，无新增变更。
4. ZenMate 免费浏览器扩展：reviewedbypro 2026-11 评测确认 zenmate.com 仍链接免费 Chrome 扩展，付费应用 2023 年已并入 CyberGhost；与 2026-11-18 结论一致，无 24–48h 内新变化。继续列为周检候选。
5. Proton VPN：新协议核心 Proton Protocols 进入 beta（2026-11-18，vpnuniverse 新闻汇总）；Black Friday Plus 75% 折扣为付费促销。均非免费档变更，不改库。
6. SuperVPN Free VPN Client（Softonic 2026-11-18 更新）：多年老牌免费应用（1 小时会话、20 天试用），仅常规版本更新；列入周检候选，本次不入库。
7. AppBrain 土耳其付费榜新面孔（Free VPN - Unlimited VPN Proxy by Free VPN LTD、VPN PRO - Unlimited Protection、Mysterium VPN）：榜单新上榜≠新服务；Mysterium 为付费去中心化 VPN，无免费档；其余两款未核实官网/运营方，暂不入库。
8. 菲律宾/RU VPN MOD APK（phcorner 2026-11-18）：盗版修改包，非正规新服务，忽略。
9. ExpressVPN 上线 Amazon Vega OS：付费服务，无关。
10. Samsung Max：已在 discontinued（2026-06-15 关停）；toolradar 11 月文章为旧闻回顾，无新增变更。
11. Anomi VPN（removed，2026-11-09）：本次复查——官网 anomivpn.com 仍无法访问（curl https:000），无服务恢复的有效证据。仍在 removed，不恢复入库。
12. PandaVPN Lite（com.pandavpnfree.androidproxy）：官网 pandavpn.com 本次 curl 仍超时未达（https:000），无恢复证据；继续列为周检候选，暂不入库。
13. Free VPN by Free VPN .org（org.freevpn）：官网 freevpnapp.org 本次 curl 200，仍在架；继续列为周检候选，暂不入库。
14. Berry VPN / Skyvora VPN / Teal VPN：官网本次 curl 均 200，与库内一致，无新增变更。

## 待每周复核跟进（非本次确认变更，仅记录冲突来源）

- Windscribe 10 GB 条件：antivirusprotection.org 2026-11-07 称需确认邮箱且订阅推广邮件；库内仅写“确认邮箱”。周检时核对官网帮助中心（自 2026-11-18 延续）。
- Firefox 内置 VPN：2027-02-01 00:00 UTC 恢复 50 GB/月已确认；待 2027-02 复核确认实际恢复情况。另：Mozilla 曾在 2026 年夏季做过同类不限量推广（8 月 31 日结束、9 月恢复 50 GB），属季节性促销模式。
- Ninja VPN：官网与 Play 列表内容不一致（服务器数/协议/设备数），下次复核时以官网隐私政策与 Play 列表为准重新核对。
- 大复核候选：EVPN、Touch VPN、ZoogVPN、BearVPN、ZapSplit VPN、XNX VPN、VPN Super Unlimited Proxy、VPN.lat、Happ - Proxy VPN、Proxiten、Shmel VPN、ZeroPing VPN、TipTop VPN、Aloha Browser、TrendVPN、Russian VPN / MEDVET VPN、USA VPN、TapTap VPN、ZenMate 免费扩展、TeknoVPN、PandaVPN Lite、Free VPN by Free VPN .org、SuperVPN Free VPN Client（新增）。

## 同步

- YAML 已改动（+1 条）：已运行 export-page-sync.js 生成快照（39 条）；artifact.edit 已触发（slug: mian-fei-vpn-shu-ju-ku），构建已成功回执：页面内嵌 DATA 共 39 条、家宽 4 条 + 部分 2 条、末条为 Grass VPN，验证通过。
- 注意：构建成功但 `current_build_published: false`——公开链接仍显示上一版（38 条），需用户明确要求重新分享才会更新；Muse 内打开的页面已是 39 条新版。
- Git：bash sync.sh 已执行，提交 37be00f（附带补交 2026-11-16/17/18 三份运行日志），已推送到 origin main（GitHub kgd735/FreeV）。
- 公开页面链接：https://muse.ai/s/mian-fei-vpn-shu-ju-ku-xhxd6xe0uxbxsp1n/524jt68zSApSIH5MC2nGlPSbeJuZFtOcaKCX54ZOr1s

## 结论

- free-vpn-db.yaml：entries 38 → 39 条；removed 仍为 1 条（Anomi VPN）；discontinued 仍为 5 条；家宽 IP 仍为 6 家。
- 新增收录 Grass VPN，按任务要求向用户汇报；页面与仓库同步完成情况待 artifact 构建回执后确认。
- 下一次检索：明日 2026-11-20（free-vpn-db-daily-discovery）。
