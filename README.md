# 免费 VPN 数据库

有免费档的 VPN 信息库，数据全部维护在 `free-vpn-db.yaml` 中；`index.html` 打开时加载该文件并自动渲染成可搜索、可筛选的页面。

## 数据库文件格式

`free-vpn-db.yaml` 是唯一事实来源。顶层字段：

| 字段 | 说明 |
|---|---|
| `schema_version` | 数据格式版本 |
| `last_full_review` | 最近一次全面复核日期 |
| `entries` | 仍在提供免费档的 VPN 条目 |
| `removed` | 已确认无效后删除的条目（墓碑记录，含删除日期、原因、证据） |
| `discontinued` | 已下线或取消免费档的服务记录 |

每条 `entries` 的字段：

```yaml
- id: urnetwork                  # 唯一标识（小写 + 连字符）
  name: URnetwork
  official_url: https://ur.io
  status: active                 # active（已核实）/ uncertain（未核实）
  free_tier:
    data_cap: "30 GiB/day"       # 免费额度（"unlimited" = 不限量）
    devices: "2 concurrent clients"
    countries: "90+ countries"
    signup: "no email required"  # 注册要求
    card_required: false         # 是否需要信用卡
  residential_ip:
    has: true                    # true=有住宅 IP / false=机房 IP / partial=部分是 / unknown=未知
    note: "…"                    # 说明
  ip_type: "residential / P2P"
  protocols: ["WireGuard"]
  logging: "…"                   # 日志政策与审计情况
  platforms: ["Android", "iOS", "Windows"]
  last_verified: "2026-11-04"    # 最近核验日期
  change_log: "…"                # 可选：变更记录
  sources: ["https://…"]         # 可选：信息来源
```

删除条目时不要直接丢弃：移到 `removed` 列表，记录 `removed_date`、`reason`、`evidence`。

## 使用

环境：Node.js ≥ 20，首次使用先安装依赖：

```bash
npm install
```

| 命令 | 作用 |
|---|---|
| `node scripts/build.js` | 校验数据库格式，确保页面运行所需文件就位 |
| `node scripts/check-urls.js --output ./checks` | 检测所有官网 URL 可达性，输出 JSON 报告（403 或连接失败不等于下线，需结合搜索判断） |
| `node scripts/export-page-sync.js` | 把数据库导出为 Markdown 快照，供 Muse 聊天内的数据库页面同步使用 |
| `bash sync.sh "提交信息"` | 一键同步：校验 + 提交 + 推送到远程仓库（无变更时自动跳过） |

维护节奏：每周复核一次全部条目（官网可达性 + 免费档变更），确认无效的按 `removed` 规则删除；每日检索新增免费 VPN，入库前比对 `removed`/`discontinued`，按信息新旧日期避免重复添加已确认无效的服务（除非有更新的证据表明其恢复有效）。

## 部署

页面是纯静态文件，无后端。部署时把仓库根目录放到任意静态托管（GitHub Pages / Cloudflare Pages / Nginx），或只拷这几个文件：`index.html`、`app.js`、`vendor/`、`free-vpn-db.yaml`。

页面打开时由 `app.js` 加载同目录的 `free-vpn-db.yaml` 并用 js-yaml 解析渲染，数据库文件一变，刷新页面即自动更新。`vendor/js-yaml.min.js` 是浏览器端 YAML 解析器（随仓库提供，无需联网加载）。

注意：直接双击打开 `index.html`（file:// 协议）时浏览器会拦截读取数据库文件，页面会提示加载失败。本地预览请用 HTTP 服务：

```bash
npx --yes http-server . -p 8000   # 然后访问 http://localhost:8000
```

远程仓库：`git@github.com:kgd735/FreeV.git`（GitHub；deploy key 在 `/home/hatch/.ssh/vpn_db_push_deploy`，不要删除）。
