# 免费 VPN 数据库

30 个仍在提供免费档的 VPN + 4 个已下线/取消免费档的记录。调研日期：2026-11-04；Avast VPN Free 于 2026-11-07 新增入库；OkayFreedom VPN 于 2026-11-08 新增入库。

- 机器可读数据：`free-vpn-db.yaml`（每月定时任务复核更新）
- 可浏览页面：见聊天中的数据库页面
- 官网可达性检测：`node scripts/check-urls.js`

## 一句话结论

- **28/30** 家的免费档在 2026 年 11 月确认仍然有效；Anomi VPN 存疑（Chrome MV2 下架后无更新），另有 2 家在 2025–2026 取消了免费服务。
- **有家宽（住宅）IP 的只有 5 家**：URnetwork、Urban VPN、tuxlerVPN、Hola VPN、StarVPN（StarVPN 住宅 IP 为付费档功能，免费档 IP 类型未证实；VPN Gate 部分节点是志愿者家宽）。
- 免费 ≠ 无代价：P2P 类（Urban/tuxler/Hola）会把你的设备当作别人的出口；VPN Gate 官方明示记录连接日志至少 3 个月。

## 家宽 IP 一览

| 名称 | 免费额度 | 家宽 IP | 代价/备注 |
|---|---|---|---|
| URnetwork | 30 GiB/天 | ✅ 真实住宅出口，90+ 国家 | 无需注册；做出口可赚代币（2026-10 起改 SN25α 结算） |
| Urban VPN | 桌面不限量 | ✅ P2P 住宅 | 你的设备会被别人当出口；日志记录严重；Chrome 插件曾被曝偷 AI 聊天记录 |
| tuxlerVPN | 不限流量 | ✅ P2P 住宅 | 免费版必须共享自己的 IP/带宽（仅付费可关闭） |
| Hola VPN | 不限流量（限时） | ✅ P2P 住宅 | 桌面端会被当作出口（约 100MB/天）；浏览器插件不在 P2P 池 |
| StarVPN | 100 GB/月 | ✅ 住宅 ISP IP（付费档；免费档未证实） | 免注册；"永久免费"说法仍有效（Play v2.45, 2026-10-20），"90 天/账号"说法未证实（或为另一个同名 App） |
| VPN Gate | 不限量 | ⚠️ 部分 | 志愿者节点混杂家宽/VPS；官方记录连接日志 ≥3 个月 |

## 免费档速览（无家宽 IP 的主流选择）

| 名称 | 免费额度 | 注册要求 | 日志/审计 |
|---|---|---|---|
| Proton VPN | 不限量，10 国，1 设备 | 需邮箱 | 无日志，Securitum 年审（2026 年 6 月第 5 次） |
| Windscribe | 10 GB/月（验证邮箱；不验证 2GB） | 可选 | 无日志声称；无独立审计 |
| hide.me | 不限量，7 国，1 设备 | 无需注册 | 零日志经 Securitum 评审 |
| Avast VPN Free | 不限量（官方法语页另一版本称 500GB/月，待澄清），自选 3 地区（锁定不可换），无限设备 | 需 Avast 账号 | 无日志声称，未审计（VerSprite 年审首份报告预计 2026-11）；2024 年 FTC 曾因出售浏览数据罚 1650 万美元；印度不可用 |
| OkayFreedom VPN | 最高 30 GB/月（看广告赚流量，每条 250 MB，每天最多 4 条，未用流量可累积；Windows 免费档 2 GB/月），Android 13+ | 无需注册 | 声称无活动日志（连接记录保留 90 天），未审计；德国 Steganos（自 1997 年） |
| X-VPN | 不限量，15+ 国 | 无需注册 | 零日志，ISAE 3000 审计由 Deloitte 新加坡于 2026-02-28 完成（6 月公布）；运营主体迁新加坡 |
| Cloudflare WARP | 不限量（无选地区） | 无需注册 | 1.1.1.1 隐私政策经 KPMG 审计（2019） |
| Opera 浏览器 VPN | 不限量（仅浏览器） | 无需注册 | 无日志，Deloitte 审计（2024） |
| TunnelBear | 2 GB/月（2026 年起不可选服务器） | 需邮箱 | 无日志，Cure53 年审 |
| PrivadoVPN | 10 GB/月后降速（需每月在 app 内续期），1 设备 | 需邮箱 | 无日志声称，未审计；2026-05 起由冰岛 Privado Networks ehf. 运营 |
| Lantern | 512 MB/天 | 无需注册 | 无审计；开源 |
| Psiphon | 不限量（约 2 Mbps） | 无需注册 | 明示非隐私产品，会记录敏感数据 |
| Planet VPN | 不限量，5–6 国，10 设备 | 无需注册 | 无日志声称，未审计（有说保留连接日志） |
| Speedify | 2 GB/月，5 设备 | 无需注册 | 无日志声称，未审计 |
| Avira Phantom | 500 MB/月（注册 1 GB） | 可选 | 无日志声称，未审计 |
| Hotspot Shield | 桌面 500MB/天；手机看广告不限量 | 无需注册 | 非无日志（记录匿名域名+设备 ID 用于营销） |
| Betternet | 桌面 500MB/天；手机看广告不限量 | 无需注册 | 记录 IP 地址 |
| Turbo VPN | 500MB/天（多数 2026 评测确认；少数仍称不限量），3 地区 | 无需注册 | 隐私存疑（可能给广告商数据） |
| VPNBook | 不限量（公开共用账号） | 无需注册 | 保留部分数据 |
| Freegate | 不限量（无付费档） | 无需注册 | 反审查工具，非隐私产品 |
| UltraSurf | 不限量（仅美国） | 无需注册 | 非无日志（保留 30 天） |
| Riseup VPN | 不限量（捐赠维持） | 无需注册 | 声称不记 IP，未审计 |
| CalyxVPN | 不限量（非营利） | 无需注册 | 声称无日志，未审计 |
| Anomi VPN | 500MB/天（Chrome 插件）| — | ⚠️ 2026 年是否还能用无法证实 |

## 已下线 / 取消免费档

| 名称 | 变化 | 时间 |
|---|---|---|
| Samsung Max VPN | 整个服务关停（5000 万+ 用户） | 2026-06-15 |
| Kaspersky VPN | 多数国家取消免费版，仅剩 7 天试用 | ~2026-04 |
| Atlas VPN | 服务关停 | 2024-04-24 |
| Google One VPN | 服务关停 | 2024-06 |

## 字段说明

`residential_ip.has`: `true`（有住宅 IP 出口）/ `false`（机房/代理 IP）/ `partial`（部分是）/ `unknown`（无法证实）。

## 更新机制

- **每周一复核**：检测官网可达性 → 搜索免费档变更 → 更新条目；确认无效的条目从列表删除，记入 `removed`（墓碑记录：删除日期、原因、证据来源）。
- **每日检索**：搜索新免费 VPN → 核实后入库；入库前比对 `removed`/`discontinued`，按信息新旧日期避免重复添加已确认无效的服务——除非有更新的证据表明其恢复有效。
- 有变化时在聊天中汇报；无变化时保持安静。

## 自动化流程（Node.js）

```
free-vpn-db.yaml ──▶ page/app.js（浏览器运行时 fetch + js-yaml 解析渲染）
                    └─▶ scripts/build.js ──▶ 同步 page/free-vpn-db.yaml（页面运行时加载的文件）
                    └─▶ scripts/export-page-sync.js ──▶ Muse artifact 页面同步快照
                    └─▶ sync.sh ──▶ git commit + push 到 origin main
```

- **数据库是唯一事实来源**：所有展示（README 表格、静态页、Muse artifact 页）都从 `free-vpn-db.yaml` 生成。
- **页面自动更新**：`page/index.html` 不内嵌数据，打开时由 `page/app.js` 加载同目录的 `page/free-vpn-db.yaml` 并用 js-yaml 解析渲染。数据库文件一变，刷新页面即自动更新，无需重新生成 HTML（`scripts/build.js` 负责把根目录的 YAML 同步到 `page/`）。
- **`sync.sh` 一键同步**（无变更时自动跳过）：
  ```bash
  bash sync.sh "更新数据库：新增 Avast VPN Free"
  ```
- **定时任务已接线**：每周复核（`free-vpn-db-monthly-check`）与每日检索（`free-vpn-db-daily-discovery`）在改动 YAML 后自动执行上述同步（重建 artifact 页面 + `sync.sh` 提交推送）。
- **远程仓库**：`ssh://git@gits.d35.kdns.fr:2222/kuangdash/FreeVPN.git`（Gitea，直连 2222 端口；deploy key 在 `/home/hatch/.ssh/vpn_db_push_deploy`，不要删除）。
- **环境要求**：Node.js ≥ 20；首次使用先 `npm install`（安装 js-yaml）。

## 部署静态页

页面是纯静态文件（`page/index.html` + `page/app.js` + `page/vendor/js-yaml.min.js` + `page/free-vpn-db.yaml`），无后端。部署时把整个 `page/` 目录放到任意静态托管（GitHub Pages / Cloudflare Pages / Nginx），不要只拷单个 HTML 文件——页面运行时要加载同目录的 `free-vpn-db.yaml`。

```bash
# 数据更新后同步并推送（会自动同步 page/free-vpn-db.yaml）
bash sync.sh "更新数据库"
```

注意：直接双击打开 `page/index.html`（file:// 协议）时浏览器会拦截 fetch，页面会提示加载失败。本地预览请用 HTTP 服务，例如：

```bash
npx --yes http-server page -p 8000   # 然后访问 http://localhost:8000
```

## 页面结构

- `page/index.html`：页面骨架（样式、搜索框、筛选按钮、空容器）。
- `page/app.js`：运行时逻辑——fetch `free-vpn-db.yaml` → js-yaml 解析 → 渲染统计、卡片、下线/墓碑表格；搜索与筛选在浏览器本地完成。
- `page/vendor/js-yaml.min.js`：浏览器端 YAML 解析器（js-yaml 官方构建，随仓库提供，无需联网加载）。
- `page/free-vpn-db.yaml`：由 `scripts/build.js` 从根目录同步而来，页面运行时加载的就是它。

另有 `scripts/export-page-sync.js`：把 YAML 导出为 Markdown 快照，供 Muse 聊天内的数据库页面（artifact）同步使用，与本页加载逻辑互不依赖。
