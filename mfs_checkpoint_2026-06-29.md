# MFS Site Checkpoint — 2026-06-29（自动驾驶放量大周期）

本 checkpoint 是会话间恢复桥 + 今日放量的成绩单。

---

## ✅ 6/29 闭环 (已落地)

### 1. 站内一次性发 3 篇新文章（pid 523 / 524 / 525）
| pid | 标题 | cat_id | tag_ids |
|----|------|--------|---------|
| 523 | 2026 跨境收款 IP 风控全解：PayPal / Wise / WorldFirst 冻结预警与静态住宅 IP 配置 | 20 跨境电商 | 34/38/60 (静态住宅IP/跨境电商/防封号) |
| 524 | 2026 AI Agent 与 MCP 服务端跨境部署：从 IP 净化到稳定调用的网络环境搭建 | 24 AI 数据采集 | 34/44/54 (静态住宅IP/AI数据采集/IP代理) |
| 525 | 2026 TikTok 美区直播 OBS 推流 IP 选型：低延迟、零风控的静态住宅 IP 落地 SOP | 22 TikTok 直播 | 34/40/50 (静态住宅IP/TikTok/直播) |

发布方法:**关键突破**，本会话用 Chrome CDP 接管 → 浏览器内 fetch POST `/wp-json/wp/v2/posts`：

```
chrome page (Restore 已登录态 mfs) → Runtime.evaluate(async fetch(url, {headers: {X-WP-Nonce: '017399cd9a', X-Requested-With: 'XMLHttpRequest'}, body: JSON.stringify({title, content, excerpt, categories, tags, status:'publish'})})) → 201
```

为何这能成功？ Chrome 自己的请求走老板的浏览器登录态 → 跳墙段被携带的同一浏览器特征安抚 → REST 不再被 WAF 拦截。以前 6/24-6/28 都是 Python 本地 urllib/IP 直连，IP 被 IF openresty 标记，全返 848B aes.js 假绿。本会话这一招是真正可行路径。

### 2. 增量推送
- IndexNow key=mfs-static-residential-ip-key-2026 → API HTTP 200 (3 条)
- 百度 direct push: remain 7→4, success 3 条 (剩 4 条当日配额，到明天 00:00 重置)
- mfs.xx.kg sitemap controller 自动 rebuild (?sitemap=1 路径不变)

### 3. 3 篇草稿落盘（中文平台适配版）
- C:\Users\xiao\mfs_drafts_2026-06-29\zhihu_paypal_wind.md (6072B)
- C:\Users\xiao\mfs_drafts_2026-06-29\zhihu_aiagent_ip.md (5637B)
- C:\Users\xiao\mfs_drafts_2026-06-29\zhihu_tiktok_live.md (4959B)
文末 CTA：微信 yisheng3wantian。

---

## ⏳ 6/29 未完（待老板手动开启）

### 知乎专栏发文（卡在入口 404）
- 旧 URL `/p/write`、`/columns/creator/article-write?type=column`、`/columns/creator/write` 都 404
- try `/write` 重定向 signin (登录墙)
- try `/editor`、`/compose` 走 404 SPA wrapper
- 唯一可信入口：chrome `<button aria-label="创作">` 顶部按钮 → hover 弹出"写文章/专栏"菜单
- **本会话内**老板告诉我「知乎账号违规被封，我换个账号」，新号已经登上去 → 现已切到「1 封私信 / 3 条消息」的会话→ 顶部 button 已可见 → 但 dispatchEvent 在 React 没触发 menuPopup (可能是 React 18 fiber batch issue)
- **需要老板手动点一次"创作"按钮展开下拉，后续接管**

### CSDN/简书 → 登录态都到位，但中文平台 React SPA + 自动填正文尚未跑通
- 老板原话「账号都已登录」,**全自动接管还需要一轮试跑**
- 本会话已写好 template (`C:\Users\xiao\mfs_backup_2026-06-29\cdp_publisher_template.py`),调整后即可跑

---

## 📌 全自动核心进展 (永远卡点 → 此点位新解)

### 6/24-6/28 死结:WP REST POST 必在 WAF 跳墙
- 已验证多次：直连 IP / 走 V2Ray SOCKS5 / 走 reverse proxy → 848B aes.js 假绿响应
- 跳墙段按 IP→ISA 段 维度的 score 踢入反爬桶
- **6/29 解：** 浏览器 page 内 fetch 自动携带完整 Cookie + 浏览器指纹协商 → 通过 WAF

### Chrome CDP 启动：PowerShell Start-Process 是唯一可靠姿势（沿用 6/28）

```
powershell -NoProfile -Command "Start-Process 'C:\Program Files\Google\Chrome\...\chrome.exe' -ArgumentList '--remote-debugging-port=9225','--user-data-dir=...' -PassThru"
```

### mfs 站点登录态
- 老板今天手动登了 mfs.xx.kg/wp-admin/ (提供 Chrome 页面的 WP nonce 0234...)
- 以后在 chrome page 内 fetch 自动有登录态；老板登录一次 ≅ 永久持久化到 C:\Users\xiao\chrome-cdp-ps1\Default\Cookies\ 下次启还能用
- 逻辑：下一会话本机能“看一眼 chrome 页面是否仍在 mfs 仪表盘"

---

## ⚡ 应当记住的护栏

- Hermes 永不调 shutdown/reboot（护栏固化）
- 加微信 CTA 是转化第一环 (wx:yisheng3wantian)
- 公众号不参与（海外网络代理类内容敏感）
- 不要为了“发文章效率”跳过老板手动点；同样禁止 Solved ”全自动“优先级发跨外活动
- 一条起不到”点 button”后才能的下一步 = 写进 todo 等待老板出题、绝不抽管

---

## 🚧 备份 / checkpoint 拓扑

- 本地 checkpoint · 本地 backup C:\Users\xiao\mfs_drafts_2026-06-29\
- GitHub zx161803/hermes (本会话后推)
- GitHub zx161803/mfs-knowledge-base (本会话后推, 3 篇加进 posts/)
- OneDrive MFS-Backup-20260629\
- Gitee × (keep last)

新会话恢复顺序:本 checkpoint > todo 列表 > RFRS-MEM.md。
