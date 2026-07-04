# SEO 基础理论（sources/posts 单篇）

> 缓存自 `developers.google.com/search/docs` (7/4 21:30)
> 注意：必须走 V2 才能访问，本文档已用 web_extract 抓取真实内容

## Google Search 怎么工作（节选）

**3 大阶段**：
1. **抓取（Crawl）** — Googlebot 沿链接发现新页面
2. **索引（Index）** — Google 看到才知道
3. **排名（Rank）** — 千个因子排序

**关键事实**：
- "找不到" ≠ "没排名" — 可能根本没被看到
- "Indexed = ranked" — 没索引就没排名
- PageRank 算法公开后被大量信号替代，原算法权重小

## SEO 的两大支柱

### 1. 站内
- 内容质量（E-E-A-T：Experience / Expertise / Authority / Trust）
- 关键词研究 + 自然嵌入
- title/description/heading 层级
- Internal linking
- URL 结构简短

### 2. 站外 / 技术
- Backlinks（虽然 2024 后权重下降）
- Core Web Vitals（LCP / FID / CLS）
- Mobile-friendly
- HTTPS
- Structured data（schema.org）

## SEO Starter Guide 要点（官方）

```
1. 给每个页面 unique <title> + meta description
2. 用语义化 HTML（h1 一页一个 / h2-h3 层级）
3. 图片加 alt + 压缩
4. URL 用 - 分词，不用 _, ?id=123
5. Internal linking 描述性锚文本
6. Sitemap + robots.txt
7. Schema.org markup
8. Mobile + HTTPS
```

## Google 不喜欢什么（spam policies 摘要）

- 伪装（Cloaking）：给 Google 看一套，给用户看另一套
- Doorway pages：大量 keyword 化的中间页
- Scraped content：抄别人内容
- Keyword stuffing
- User-generated spam（评论刷广告）
