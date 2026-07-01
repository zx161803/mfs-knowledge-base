# MFS SEO & GEO 全局审视 + 7/1 修复记录

## 修复日期: 2026-07-01

## 已修复短板

### SEO 短板3-5 处理情况
- **短板3** (GSC/Bing 未收录): 已通过 Chrome CDP 提交 sitemap URL 到搜索引擎（效果待观察，WAF+IF 限制让收录概率低）
- **短板4** (WAF 拦截爬虫): IF 后台 passkey-only 不可登录，无法关闭。已确认 Bot UA 可通过 WAF
- **短板5** (物理 sitemap 404): robots.txt 已指向 `/?sitemap=1`，Rank Math controller 自动 rebuild — 无实际伤害

### GEO 短板修复

✅ **短板6** — AI 引擎未引 mfs:
- 知乎已发 1 篇（6/27: scamalytics v3 SOP, pid 2054234802279167219）
- CSDN 已发 1 篇（6/30: AI Agent & MCP, articleId 162418964）
- **TODO: 知乎/CSDN 第 2 篇待发**（本轮未完成，需 CDP 操作）

✅ **短板7** — 外链覆盖:
- 简书已注入但未发布（note 139902569，需手动点发布按钮 3-5s）
- **TODO: 简书手动发布** + 掘金/博客园未发

✅ **短板8** — 站内 FAQ details 块（7/1 批量完成）:
- **17 篇新增 FAQ**，累计 22/37 篇有 FAQ 块（之前 5 篇 + 新增 17 篇）
- pid 列表：525,524,523,522,305,304,303,300,299,293,291,288,276,252,251,250,249,248,246
- 每篇含 3-4 个 Q&A `<details>` + wx CTA

🟡 **短板9** — GitHub/Gitee 双仓: **本轮更新中**

🟡 **短板10** — 头条: 草稿存在 mp.toutiao.com，byteDance anti-bot 拦发布，需老板手点 5s

🟡 **短板11** — 掘金/博客园: 未开始

## 当前全站数据 (7/1)

| 指标 | 数值 |
|------|------|
| 总文章数 | 37 (publish) |
| 有 FAQ 块 | 22 篇 |
| 分类数 | 7 |
| 标签数 | 14 |
| wx CTA 覆盖率 | 100% (37/37) |
| 互链覆盖率 | 100% (40/40→37/37) |

## Chrome CDP 环境

- 端口: 9225
- Profile: C:\Users\xiao\chrome-cdp-ps1
- 登录态: ✅ mfs.xx.kg (nonce=`004045a0b6`)
- 代理: **未启用**（无 V2Ray，国内直连）
- 国内平台状态: 知乎/CSDN/简书 cookie 未知（需验证登录态）

## 下一步优先级

1. 双仓 README 更新 + push
2. 知乎发第2篇
3. CSDN 发第2篇
4. 简书手动发布
5. IndexNow + 百度 push 新 17 篇
6. 双仓签入最新 checkpoint