# Schema.org（sources/posts 单篇）

## 核心统计（2026-03 V30.0）
- 823 Types
- 1529 Properties
- 19 Datatypes
- 96 Enumerations

## mfs.xx.kg 现状（7/4 实测）

| Schema Type | mfs 已用 | 推荐 |
|---|---|---|
| Article | ✅ 全部文章 | ✅ |
| Organization | ✅ trust block | ✅ |
| Service | ✅ Our Services page | ✅ |
| AboutPage | ✅ About / Story | ✅ |
| BreadcrumbList | ❌ 缺 | ✅ 强烈推荐 |
| WebSite | ❌ 缺 | ✅ |
| FAQPage | ✅ 5 篇 | ✅ |
| Person | ❌ 缺 | 可选 |
| Product | ❌ 缺 | 可选（IP 代理套餐） |

## 必备 schema（Article 完整 example）

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "亚马逊多店铺防关联 IP 配置",
  "author": {
    "@type": "Person",
    "name": "魔法师",
    "url": "https://mfs.xx.kg/about/"
  },
  "datePublished": "2026-06-24T08:00:00+08:00",
  "dateModified": "2026-06-24T08:00:00+08:00",
  "description": "...",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://mfs.xx.kg/amazon-anti-assoc-ip-config/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "MFS · Static Residential IP",
    "logo": {
      "@type": "ImageObject",
      "url": "https://mfs.xx.kg/logo.png"
    }
  },
  "image": "https://mfs.xx.kg/og-default.png"
}
```

## 验证工具

### 官方
- https://validator.schema.org/ — Google Rich Results Test 集成
- https://search.google.com/test/rich-results — Google 专项

### 命令行
- **jsonschema + 自定义 schema** — 见 `tools/python-jsonschema.md`
- **schema-org-validator npm** — 自动 lint

### GitHub Action
- **johnnyreilly/schemar** — 自动跑 CI，每次改 PR 触发验证

## 写 schema 时常见错误

1. **日期格式错** — 必须 ISO 8601（含 timezone）
2. **URL 不规范** — 必须绝对 URL，不要相对路径
3. **嵌套缺失** — Article → author 不能少
4. **Property 拼错** — `datePublished` 不是 `published_date`
5. **类型混用** — `@type: ImageObject` 不能 string 当 URL

## 高级：Service schema（mfs 主打）

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "静态住宅IP 代理",
  "provider": {
    "@type": "Organization",
    "name": "MFS",
    "url": "https://mfs.xx.kg"
  },
  "areaServed": ["CN", "US", "EU", "BR"],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "IP 代理套餐",
    "itemListElement": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "美区住宅 IP"}}
    ]
  },
  "description": "...",
  "offers": {
    "@type": "Offer",
    "price": "199.00",
    "priceCurrency": "CNY"
  }
}
```
