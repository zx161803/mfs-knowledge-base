# 权威源头清单

> **建库时间**：2026-07-04 21:30
> **更新周期**：每日由 `scripts/daily_refresh.ps1` 自动重验状态
> **分类标准**：只接受带 `/docs/` `/schemas/` `/help/` 子路径的官方文档，不接受 SEO 营销博客

---

## 🔍 验证状态总览（7/4 21:30 实测）

| 分类 | 总数 | 200 OK | 301/302 | 403/404 | 备注 |
|---|---|---|---|---|---|
| Google Search Central | 6 | TBD | TBD | TBD | 走 V2 才能验证（直连 0/timeout） |
| Bing Webmaster | 2 | ✅ 2 | 0 | 0 | 直连可 |
| Schema.org | 3 | TBD | 0 | 0 | 走 V2 才能验证 |
| llms.txt 提案 | 1 | ✅ 1 | 0 | 0 | llmstxt.org 直连 |
| Cloudflare | 2 | ✅ 2 | 0 | 0 | developer docs 直连 |
| 百度搜索资源平台 | 2 | ✅ 2 | 0 | 0 | 直连可 |
| IndexNow | 1 | ✅ 1 | 0 | 0 | indexnow.org 直连 |
| Wikipedia / RFC | 1 | ✅ 1 | 0 | 0 | RFC9309 |
| AI 引擎官方 | 2 | 0 | 1 | 1 | OpenAI 403 + Anthropic 301 |
| Cloudflare blog | 1 | ✅ 1 | 0 | 0 | Radar data 真活 |

> TBD = 走 V2 验证才能确认，下次刷新时跑

---

## 📂 按主题分组

### A. SEO 基础（Google Search Central）

| 链接 | 主题 | 优先级 | 验证 |
|---|---|---|---|
| https://developers.google.com/search/docs | 入口 | ★★★ | V2 验证 |
| https://developers.google.com/search/docs/fundamentals/seo-starter-guide | SEO 入门 | ★★★ | V2 |
| https://developers.google.com/search/docs/crawling-indexing | 抓取与索引 | ★★★ | V2 |
| https://developers.google.com/search/docs/sitemaps/build-sitemap | sitemap 规范 | ★★ | V2 |
| https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt | robots.txt | ★★★ | V2 |
| https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data | 结构化数据 | ★★★ | V2 |
| https://developers.google.com/search/docs/appearance/structured-data/article | Article schema | ★★ | V2 |
| https://developers.google.com/search/docs/appearance/structured-data/organization | Organization | ★★ | V2 |
| https://developers.google.com/search/docs/appearance/structured-data/breadcrumb | BreadcrumbList | ★★ | V2 |
| https://developers.google.com/search/docs/guides/javascript-seo-basics | JS SEO | ★★ | V2 |
| https://developers.google.com/search/blog | 官方公告 RSS | ★★★ | V2 |
| https://support.google.com/webmasters/answer/9128668 | Search Console 入门 | ★★ | V2 |

### B. Bing Webmaster Tools

| 链接 | 主题 | 验证 |
|---|---|---|
| https://www.bing.com/webmasters/help | 入口 | ✅ 200 |
| https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a | 收录指南 | 直连 |
| https://www.bing.com/webmasters/url-submission-api | URL submission API | ✅ 200 |
| https://www.bing.com/webmasters | 后台入口 | 直连 |

### C. Schema.org 结构化数据

| 链接 | 主题 | 验证 |
|---|---|---|
| https://schema.org/docs/schemas.html | 823 types 入口 | V2 |
| https://schema.org/docs/gschemas.html | Google 扩展 | V2 |
| https://schema.org/docs/releases.html | 更新日志 | V2 |
| https://validator.schema.org/ | 验证器 | V2 |
| https://schema.org/Article | Article 详页 | V2 |
| https://schema.org/Organization | Organization | V2 |
| https://schema.org/Service | Service schema（mfs 主打） | V2 |

### D. llms.txt / AI 索引（2024-09 标准）

| 链接 | 主题 | 验证 |
|---|---|---|
| https://llmstxt.org/ | 标准提案（Jeremy Howard 2024-09） | ✅ 200 |
| https://github.com/AnswerDotAI/llms-txt | 标准仓 | 直连 |
| https://llmstxt.site | llms.txt 站点目录 | 待验 |
| https://directory.llmstxt.cloud | llms.txt 云目录 | 待验 |
| https://developers.cloudflare.com/llms.txt | Cloudflare 全文档 llms.txt | ✅ 200 |

### E. AI 爬虫 User-Agent（必须放行清单）

| 链接 | 主题 | UA 字符串 |
|---|---|---|
| https://platform.openai.com/docs/gptbot | GPTBot | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.1; +https://openai.com/gptbot)` |
| https://support.anthropic.com/en/articles/8896518 | ClaudeBot / Claude-SearchBot | `compatible; ClaudeBot/1.0; +claudebot@anthropic.com` |
| https://docs.perplexity.ai/guides/bots | PerplexityBot | `compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)` |
| https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot | DuckDuckBot | 待查 |
| https://yandex.com/support/webmaster/robot-workings/check-yandex-robots.html | Yandex | ✅ 200 |
| https://commoncrawl.org/big-picture/ | Common Crawl | 404 (移除) |
| https://support.apple.com/zh-cn/guide/safari/welcome | Applebot-Extended | 待验 |

### F. 中文搜索引擎

| 链接 | 主题 | 验证 |
|---|---|---|
| https://ziyuan.baidu.com/college/articleinfo?id=3329 | 百度资源平台使用指南 | ✅ 200 |
| https://ziyuan.baidu.com/college/articleinfo?id=3170 | 工具解读 | ✅ 200 |
| http://data.zz.baidu.com/ | 百度主动推送 API | ✅ 200 |
| https://ziyuan.baidu.com/property/index | 站点属性 | 直连 |
| https://www.sogou.com/docs/help/webmasters.htm | 搜狗站长 | ✅ 200 |
| https://www.so.com/help/help_3_2.html | 360 站长 | 待验 |

### G. IndexNow（所有 Bing/Yandex/etc 通用）

| 链接 | 主题 | 验证 |
|---|---|---|
| https://www.indexnow.org/index_now_documents_and_protocols | 协议 | ✅ 200 |
| https://api.indexnow.org/indexnow | API 端 | 400 (正常，POST-only) |
| https://www.bing.com/indexnow | Bing 端 | 待验 |
| https://yandex.com/indexnow | Yandex 端 | 待验 |

### H. Cloudflare 数据

| 链接 | 主题 | 验证 |
|---|---|---|
| https://developers.cloudflare.com/bots/concepts/bot/ | Bots 概念 | ✅ 200 |
| https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025 | 爬虫趋势报告（关键数据）| ✅ 200 |
| https://radar.cloudflare.com/year-in-review | Radar 2025 复盘 | 403 (正常, 需 JS) |

### I. 安全/标准

| 链接 | 主题 | 验证 |
|---|---|---|
| https://www.rfc-editor.org/rfc/rfc9309.html | robots.txt RFC 标准 | ✅ 200 |
| https://www.w3.org/TR/structured-data/ | W3C structured data | 待验 |

---

## 🚨 主动放弃的源头（不入库）

1. **SEO 营销博客**（searchenginejournal / moz / ahrefs / etc）：不直接说"权威规约"，资讯性质可读但不应进库
2. **ChatGPT/Claude 出的 listicle**：有 sweeping 错误（如 Bytespider 列错端点）
3. **过期的 GitHub Gist**：链接经常 404，不入库
4. **Reddit / Quara / 中型** UGC：可读不可引
