#!/usr/bin/env bash
# 免费 VPN 数据库自动化同步：YAML -> 页面 -> git 提交并推送
# 用法: bash sync.sh ["提交信息"]
# 仅当有实际变更时才提交并推送；无变更时静默退出（退出码 0）。
# 页面生成是确定性的（不含当前时间戳），数据不变则页面不变。
set -euo pipefail
cd "$(dirname "$0")"

# 1. 从 YAML 重新生成 git 仓库里的静态页面
python3 page/generate.py

# 2. 生成 Muse artifact 页面同步快照（定时任务用它重建 artifact 页面）
python3 export_page_sync.py

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
