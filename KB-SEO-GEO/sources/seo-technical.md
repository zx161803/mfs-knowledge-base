# 技术 SEO（sources/posts 单篇）

## robots.txt 标准

**官方**：[RFC9309](https://www.rfc-editor.org/rfc/rfc9309.html)（2021-09，前身 RFC2616 / RFC7230 接轨）

### 必备规约
```
User-agent: *    ← 所有爬虫
Allow: /         ← 默认允许
Disallow: /admin/
Sitemap: https://example.com/sitemap.xml  ← 必须用绝对 URL
```

### 注意
- 路径区分大小写（默认 bot 大小写敏感，但 Googlebot 不敏感）
- Disallow 不阻止 indexing！只阻止 crawling
- 如果想阻止 indexing，用 X-Robots-Tag header 或 meta robots tag
- 空 file = 一切允许

### AI 爬虫特别配置（2026 标准）
```
User-agent: GPTBot
Allow: /  # 别 deny，否者被 ChatGPT 完全忽略

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Bytespider
Disallow: /  # 字节训练爬虫太狠，可拒绝
```

## sitemap.xml 标准

### 协议
- `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`
- 字段：`<loc>`（必）`<lastmod>` `<changefreq>` `<priority>`（可）
- 单文件最大 50000 条 / 50MB（未压缩）
- 多个 sitemap 用 sitemap_index.xml 串

### 验证步骤
```
curl -I https://example.com/sitemap.xml # 200
cat sitemap.xml | xmllint --noout -  # XML 合法
grep '<loc>' sitemap.xml | wc -l     # 条数
```

### mfs.xx.kg 现状
- 物理 `*.xml` 路径在 IF openresty 端死掉
- **真活路径**：`/?sitemap=N`（Rank Math controller）
- 已 patch 进 `mfs-seo-indexing` skill

## JS SEO（Googlebot 现状）

- Googlebot 运行无头 Chromium（200+ 渲染）
- 默认 wait 5 秒，可加 `<meta name="fragment" content="!">` 抓 raw HTML
- 反爬 JS framework 出来的页面如果块 googlebot 完全跑不通
- 推荐：SSR 或 dynamic rendering

## Core Web Vitals（已合入 Page Experience 信号）

- **LCP**（Largest Contentful Paint）：2.5s 内 good
- **INP**（Interaction to Next Paint）：2024 替代 FID，200ms 内 good
- **CLS**（Cumulative Layout Shift）：0.1 内 good

## HTTPS

- 全站 301 HTTPS
- HSTS header：`Strict-Transport-Security: max-age=31536000; includeSubDomains`
- 不要 mixed content（HTTP 子资源 + HTTPS 父页）
