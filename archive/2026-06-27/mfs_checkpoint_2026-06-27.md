# MFS Site Checkpoint — 2026-06-27

本 checkpoint 是会话间恢复桥。下次新建会话,先读这一篇就能 80% 上下文接上。

---

## ⚠️ 当前 6/27 已知失能 / 临场护栏

### 1. D3D11 fail (严重但已查清根因)
- HP Pavilion g4 + Intel HD Graphics 3000 (VEN_8086&DEV_0116&SUBSYS_166E103C)
- 当前驱动 Intel 9.17.10.4459 (2016-05-19 HP OEM 版,**9 年未升**)
- HD 3000 物理上**不支持 D3D11 Feature Level 11_0** → 0x887A0004 (DXGI_ERROR_UNSUPPORTED)
- **HP 已退役 g4 系列** (官网 selfservice 页面明示 "There is no software or drivers available for your product")
- 6/27 尝试 sp59327 (2015-12 HP SoftPaq, 143MB): 解压失败, InstallShield 弹"系统不达最低要求"
- **结论: 永久不可修** — 旧硬件 + HP 子系统已 deprecate
- 本机 vision 重建路径死!

### 2. vision_analyze provider outage (6/27 新发现)
- vision_analyze 三次连续返空 "ChatCompletion(id='', choices=[], created=0, model=''...)"
- **与 6/24 "You forgot to attach" 不同**: 6/24=adapter bug, 6/27=provider outage
- 修复在 `auxiliary.vision.model=''` (config.yaml line 187) — 空 model 不被路由
- **agent 不可改 config.yaml** — 必须用户手改
- 6/27 测试用图: `C:\Users\xiao\AppData\Roaming\Hermes\composer-images\composer_2026-06-27_05-11-43-657_28557b.png` (994KB PNG, 健康)

### 3. 双重失能下的 vision 类任务替代策略 (skill 已封)
- 见 `C:\Users\xiao\AppData\Local\hermes\skills\software-development\vision-via-bypass-no-d3d11\SKILL.md`
- 4 条路径: B(老板贴图) + D(手机远控应急) + 3(web_extract 文本) + 4(vision-free 工作流)
- vision-free 路径能处理 80% 今天能撞到的 vision 类 task (SERP 排名 / AI 引擎答复 / UIA 网页结构 / curl + grep)
- captcha / 视频截图那 5% 是真硬墙

---

## 🟢 站点 / 后台 / 凭据 / 流程 (今天仍然有效)

### 站点
- mfs.xx.kg · WP 6.9.4 · IF LiteSpeed
- 站点内容: 40 篇 SEO 文章, 7 分类 (cat_id 20/22/24/26/28/30/32), 14 标签 (tag_id 真映射 34-60 步进 2)

### 关键账号 (统一密码 161803zxZX%%)
- WP 后台: zx161803 / 161803zxZX%%
- 邮箱: zx161803@163.com / gmail / outlook
- GitHub: ed25519 SSH key 已配 (Title: Hermes-auto-backup-2026), 实私有仓 `zx161803/hermes`
- Gitee: HTTPS + wincred
- 微信: yisheng3wantian (国内有效客户接触路径)
- 手机: 18103217282 / 18332310663
- V2Ray: socks5://127.0.0.1:10808

### WP REST 关键参数
- 必须 4 件套 header (Mozilla UA + Referer: `https://mfs.xx.kg/wp-admin/` + Content-Type: application/json + X-WP-Nonce)
- toNumbers( 出现 = WAF 跳墙 = 假成功, 立刻报老板
- 写大 payload (>20 篇) 必须 split sandbox, 单 sandbox ~300s 超时 kill

### 百度 push direct
- token=1sAWZyGQSKyWK7Ol
- POST http://data.zz.baidu.com/urls?site=mfs.xx.kg&token=<token> + body=URL text/plain
- 返 {remain, success} — 扣配额; 配额满 (10/天) 后等次日

### IndexNow
- 免 token, 直接 POST api.indexnow.org/indexnow?key=... + URL list

### sitemap 真活路径
- `/?sitemap=1` (index) + `/?sitemap=post` (25 URLs)
- 物理 `/sitemap*.xml` 永久 301/404 (IF openresty 不认), robots.txt 已指 `/?sitemap=1`, 不要加 htaccess rewrite

---

## 📋 老板硬性偏好护栏

1. **全简体中文** — 禁用繁简混排 / 港式表达
2. **按结果不要按时间** — 优先客户转化路径 (中文平台 + wx CTA) > 索引收录 / SEO 跑分
3. **客户在国内** — wx 主接触, 不 form / email 漏斗
4. **Gitee 国内镜像** — 必须双仓发
5. **公众号不参与** — 海外网络代理类内容敏感
6. **Polylang UI 不动** (plugin 锁定依赖, 跳过)
7. **不下永不调的 shutdown/reboot** (除非老板明示) — 6/24 教训
8. **不手动 bat / 后台 click** — 自动走 API / CDP
9. **言语过重禁用** — memory / 文案不"砍 / 驳回 / 放弃"代替原文 (6/26 用"砍 SEO 提升清单"被戳)
10. **不要按"按结果"读成"立刻动"** — 涉及不可逆 / 重启 / 装驱 头先走 cost-benefit 让老板选

---

## 🚦 chrome CDP / D3D11 / 视觉 状态

- D3D11 fail (永久), cua-driver 走 ax 模式可用
- vision_analyze 本日不可用 (provider outage), 看图类需求转 vision-free 路径
- Chrome CDP 已默认自启 (proactive_cdp_launcher.bat), 不需要每次手动启
- 知乎 / CSDN / 简书 草稿已存 `C:\Users\xiao\` (3 份)

---

## 🔓 未完成 / 进行中

| 优先级 | 任务 | 状态 |
|---|---|---|
| P0 | 知乎 / CSDN / 简书 草稿发布 (老板已登 chrome 但今日未发) | 卡在 SPA / cookie |
| P0 | mfs.xx.kg 站内 CTA / 互链维护 (已 6/26 完, 6/27 0 新发) | - |
| P1 | 百度 push 配额 (6/26 已满 10, 6/27 未推) | 等次日 |
| P1 | vision 通道 (明天重启 Hermes 后测试) | 留明天 |
| P1 | D3D11 永久 degrade 接受, vision 转路径 4 | 留今天 |
| P2 | CDP 国内三大平台发布 (日 3-5 篇) | 等老板登录态 |

---

## 📂 关键文件位置

| 文件 | 用途 |
|---|---|
| `C:\Users\xiao\mfs_d3d11_repair\REPORT.md` | D3D11 修复尝试闭环报告 (3.4 KB) |
| `C:\Users\xiao\mfs_d3d11_repair\sp59327.exe` | 下载的 HP SoftPaq 备份 (143 MB) |
| `C:\Users\xiao\mfs_cta_backup_2026-06-26\` | 6/26 站内 CTA / 互链 / GitHub 双仓完整备份 |
| `C:\Users\xiao\mfs_backup_<日期>-<版本>\` | 每日本地 backup |
| `C:\Users\xiao\mfs_remote_hermes\` | GitHub (zx161803/hermes) 仓库 mirror |
| `C:\Users\xiao\OneDrive\Documents\MFS-Project-Backup-<日期>\` | OneDrive 月度 zip |
| `C:\Users\xiao\AppData\Local\hermes\skills\/` | Hermes skills (含 mfs-waf-bypass / mfs-wp-admin-hand-roll / chinese-platform-content-distribution / vision-via-bypass-no-d3d11) |
| `C:\Users\xiao\RFRS-MEM.md` | 20.4 KB 高密度参考资料 |
| `C:\Users\xiao\mfs_checkpoint_2026-06-25.md` | 前次会话桥 |
| `C:\Users\xiao\mfs_checkpoint_2026-06-26.md` | 上次会话桥 |

---

## 🔁 新会话恢复顺序

1. 读 `mfs_checkpoint_<最新日期>.md` (例如本篇)
2. 读 `RFRS-MEM.md` (网站 + 凭据细节)
3. 读 `memory` (本会话注入的最上面, 含主记忆 + 6/27 护栏)
4. 跑 `mfs_remote_hermes` 上 sync (确认备份完整)
5. 检查 `vision-via-bypass-no-d3d11` skill 是否仍有效
6. 今天的活接着推

---

## 📌 反复上当过的硬性教训

- list_windows 不显示最小化窗口 — 用 window_state 单独查那个 pid 确定真实状态
- bash 转义: `$_.X` 是路径变量, 装入 powershell 命令要 `cmd //c "powershell ..."`
- cmd codepage 936 解析 .bat 中文注释报错 → 全 ASCII
- toNumbers( 出现 = WAF 跳墙, 不是成功
- passive 老板说"你来决定 / 全权决定" = 节奏授权, 不等于跨 Q
- "你都答了" = 跨 Q 警告, 立刻停

---

checkpoint 时间: 2026-06-27 13:25
小柔 6/27 收尾完毕
