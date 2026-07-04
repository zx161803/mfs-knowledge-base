# 每日凌晨 02:00 自动跑（Windows Task Scheduler）
# 任务名：KB-SEO-GEO Daily Refresh
# 触发：每天 02:00
# 用户：当前用户（无需管理员）
# 命令：powershell -ExecutionPolicy Bypass -File C:\Users\xiao\KB-SEO-GEO\scripts\daily_refresh.ps1
#
# 跳过 Hermes cron 风险：Hermes cron 在关机时丢 fire，Windows 任务计划不丢。

$ErrorActionPreference = "Stop"
Set-Location "C:\Users\xiao\KB-SEO-GEO"

$Today = Get-Date -Format "yyyy-MM-dd"
$LogFile = "changelog\$Today.md"
$RunStamp = Get-Date -Format "yyyy-MM-ddTHH:mm:sszzz"

# 1. 拉 sources 验证状态
Write-Host "[1/3] 验证 sources 链接..."
python scripts/fetch_sources.py 2>&1 | Tee-Object -FilePath $LogFile -Append

# 2. 拉 GitHub repos 元数据
Write-Host "[2/3] 拉 GitHub repos 元数据..."
python scripts/fetch_repos.py 2>&1 | Tee-Object -FilePath $LogFile -Append

# 3. 建议改动（如果 sources 有大更新）
Write-Host "[3/3] 检查 SEO 行业重大变化..."
python scripts/check_signals.py 2>&1 | Tee-Object -FilePath $LogFile -Append

# 4. Git commit
git add -A
$DiffStat = (git diff --cached --stat | Measure-Object -Line).Lines
if ($DiffStat -gt 2) {  # 不是只有 indexnow_key 那种小变
    git commit -m "kb: daily refresh $Today"
    Write-Host "✅ committed"
} else {
    Write-Host "无差异（all same），跳过 commit"
}

Write-Host "🌅 KB-SEO-GEO 刷新完成：$Today"
