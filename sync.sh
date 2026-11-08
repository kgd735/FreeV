#!/usr/bin/env bash
# 免费 VPN 数据库自动化同步：YAML -> git 提交并推送
# 用法: bash sync.sh ["提交信息"]
# 仅当有实际变更时才提交并推送；无变更时静默退出（退出码 0）。
# 页面运行时直接加载根目录的 free-vpn-db.yaml 并自动渲染，数据文件更新即页面更新。
set -euo pipefail
cd "$(dirname "$0")"

# 1. 构建：校验 YAML，确保页面运行所需文件就位
node scripts/build.js

# 2. 生成 Muse artifact 页面同步快照（定时任务用它重建 artifact 页面）
node scripts/export-page-sync.js

# 3. 有变更才提交并推送
git add -A
if git diff --cached --quiet; then
  echo "no changes, nothing to commit"
  exit 0
fi

MSG="${1:-更新数据库}"
git commit -m "$MSG"
git push origin main
echo "pushed: $MSG"
