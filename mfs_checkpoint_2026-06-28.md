# MFS Site Checkpoint — 2026-06-28

本 checkpoint 是会话间恢复桥。下次新建会话,先读这一篇就能 80% 上下文接上。

---

## ⚠️ 6/28 升级内容 (与 6/27 相比变了什么)

### 1. 浏览器自动化路由: 本机 4 路矩阵已固化 (6/28 实测闭环)
- HP g4 老集显 D3D11 永久坏 (DXGI 0x887A0004) — 6/27 已记账, 6/28 升级
- **4 路矩阵** (6/28 已实测全跑通):
  | 路径 | screenshot | DOM/JS | logged-in Chrome | 本机验证 |
  |---|---|---|---|---|
  | browser_* 工具组 | ✅ | ✅ | ❌ | ❌ 10061 拒连, 不用 |
  | computer_use (som/vision) | ❌ D3D11 坏 | ✅ via UIA | ✅ | ❌ screenshots 返空 |
  | mcp_cua_driver_* (ax mode) | ❌ | ✅ via element_index | ✅ | ✅ 19 元素拍平, 点 [4] 重新加载成功 |
  | **Python websockets + CDP** | ✅ CDP 引擎, 不走 D3D11 | ✅ Runtime.evaluate | ✅ 同一 Chrome 实例 | ✅ example.com 截图 10,392B PNG OK |
- **本机唯一稳路径: Python websockets + CDP** (skill: `software-development/browser-automation/SKILL.md` 的 `scripts/cdp_client.py`)
- 6/28 已 patch 到 `computer-use/SKILL.md` "Local-capability matrix" + `chrome-cdp-self-start/SKILL.md` Pitfall 20 (D3D11) / 21 (launch_app 污染) / 22 (browser_* 10061)

### 2. Chrome CDP 启动新姿势 (6/28 实测)
- ❌ cmd //c "start /b ..." / bare chrome.exe / cmd //c '"path"' 都 MSYS bash 转义坏
- ✅ **唯一靠谱**: `powershell -NoProfile -Command "Start-Process chrome.exe -ArgumentList '--remote-debugging-port=9225','--user-data-dir=C:\Users\xiao\chrome-cdp-ps1','--no-first-run','--no-default-browser-check','about:blank' -PassThru"`
- 已踩 1 次: 启动里裸 `cmd //c '"C:\Program Files\..." '` = `'"C:\Program Files\Google\Chrome\..."' is not recognized` 错误
- 端口选择避开 9222 (老板经常用) / 9223 (冲突) — 默认用 9225

### 3. mcp_cua_driver_launch_app 实战教训 (新增)
- `additional_arguments=["--no-sandbox", ...]` 启副 Chrome 会污染用户主 Chrome 实例
- 触发症状: "使用了不受支持的命令行 --no-sandbox" 警告 + 7-8 子进程残留 + 9222/9223 占住
- **清理**: `cmd //c "taskkill /F /IM chrome.exe /T"` (杀全部 8 个相关进程)
- **不再用 `mcp_cua_driver_launch_app` 当 CDP 入口**, 用 `Win+R` + `chrome-cdp-self-start` Step 1
- 已 patch 到 `chrome-cdp-self-start/SKILL.md` Pitfall 21

### 4. 官方 skills vs 本地对齐 (6/28 验证, 无版本过期)
- 官方 18 个根目录, 本地装齐 17 个 (`index-cache` 是聚合目录不算)
- 72 个 manifest 子 skill 全部对齐官方
- 11 个本地独有 (mfs-* / seo-geo-lead-generation / wordpress-taxonomy-seo 等) 都是 6/24+ 自写
- **结论: 全部技能最新, 无需升级任何官方 skill**

---

## 🟢 站点 / 后台 / 凭据 / 流程 (6/27 仍有效, 6/28 维持)

### 站点
- mfs.xx.kg · WP 6.9.4 · IF LiteSpeed
- 文章总数: 33 篇 (6/27 从 40 删冗重复 → 33)
- 7 分类 (cat_id 20/22/24/26/28/30/32), 14 标签 (tag_id 真映射 34-60 步进 2)

### 关键账号 (统一密码 161803zxZX%%)
- WP 后台: zx161803 / 161803zxZX%%
- 邮箱: zx161803@163.com / gmail / outlook
- GitHub: ed25519 SSH key (Title: Hermes-auto-backup-2026), 实私有仓 `zx161803/hermes`
- Gitee: HTTPS + wincred (`zx161803/mfs-knowledge-base`)
- 微信: yisheng3wantian (国内有效客户接触路径)
- V2Ray: socks5://127.0.0.1:10808

### WP REST 5 件套 header (6/27 升级)
1. `User-Agent: Mozilla/5.0 ...`
2. `Referer: https://mfs.xx.kg/wp-admin/` ← 关键
3. `Content-Type: application/json; charset=UTF-8`
4. `X-WP-Nonce: <nonce>` (同 jar 拿)
5. `X-Requested-With: XMLHttpRequest` ← 6/27 新增
- toNumbers( 出现 = WAF 跳墙 = 假成功

### 百度 push direct
- token=1sAWZyGQSKyWK7Ol
- POST http://data.zz.baidu.com/urls?site=mfs.xx.kg&token=<token> + body=URL text/plain
- 返 {remain, success} — 配额 10/天

### IndexNow
- 免 token, POST api.indexnow.org/indexnow?key=...

---

## 📂 当前 backup 拓扑 (6/28 计划精简)

### 保留
- `C:\Users\xiao\mfs_remote_hermes\` — 本地 GitHub mirror (最后 commit 83f5cc5 v9, 6/27 21:16)
- `C:\Users\xiao\mfs_backup_2026-06-27\` — 最后一份结构化 backup (含 RFRS-MEM.md + checkpoints + skills)
- `C:\Users\xiao\OneDrive\Documents\MFS-Backup-20260627-144044\` + `MFS-Backup-20260627-evening\` — 6/27 最新 2 份
- 新增: `C:\Users\xiao\mfs_backup_2026-06-28\` — 含今天新 patch 的 skills + 6/28 checkpoint

### 删除 (与 6/27 backup 内容重复, 老的本地 dir/zip)
- `mfs_backup_2026-06-22`, `-06-23`, `-06-23-v2`, `-06-24`, `-06-24-v2`, `-06-25` (本地)
- 对应 zip
- OneDrive 早于 6/27 的 `MFS-Project-Backup-2026-06-23/24-v2/25` + 6-26 backup
- `mfs_backup_full_20260627-143956.zip` (142MB, 大且带 sp59327.exe 进程内)

### 推送渠道 (6/28 重推)
- 本地: `C:\Users\xiao\mfs_remote_hermes\` (commit + push)
- GitHub: `zx161803/hermes` (ed25519 SSH)
- Gitee: `zx161803/mfs-knowledge-base` (HTTPS + wincred)
- OneDrive: 把新 backup 同步过去

---

## 🚧 已知失能 / 永久护栏

### D3D11 永久坏
- 见 `software-development/vision-via-bypass-no-d3d11/SKILL.md` 4 路绕过路径

### vision_analyze 6/27 outage
- agent 不可改 config.yaml, 必须用户手改 `auxiliary.vision.model=<具体模型>`
- 6/28 vision_analyze 仍可用 (PNG 读 ok), 间歇性失败

### browser_* 工具组本机不可用
- 10061 拒连, fallback 见 6/28 不项 #1 矩阵

### Polylang 永不能动
- 跟 connect-polylang-elementor 互依赖
- 切换器乱也永不进 Polylang UI

### Hermes cron 不耐 shutdown
- 桌面 Hermes cron tick 不耐关机 / 息屏 / 退出 Hermes
- 持久化任务走 Windows Task Scheduler

### Hermes 永不调 shutdown / reboot
- 老板明示, 6/28 已写硬护栏

---

## 🔧 6/28 新记忆要点 (Hermes memory 系统)
- 本机浏览器 4 路优先级表
- PowerShell Start-Process 是唯一 CDP 启动路径
- HP g4 D3D11 永久坏, screenshot 走 CDP 不走 cua-driver/computer_use
- 官方 skills 已对齐, 无升级需求
