# mfs.xx.kg 全局审视 · 第一面 :站内质量扫描

> 时间:2026-06-29 · 执行:小柔 · 方法:Chrome CDP 接管老板已登 Chrome + WP REST 直读 + 真页 DOM 事实

---

## ✅ 已确认的优势 (不浪费重做)

- **wx CTA 注入率 100%**(37/37 文章尾段都有"加微信 yisheng3wantian")
- **互链密集**(单篇站内链 53-60 条,SEO cluster 已成形)
- **meta description 写得精准**(学科词 + 数字承诺,如 "21–180 天 hold" "决策树 + 30 天 SOP")
- **高质量标题**(全部带年份 + 痛点词 + 工具名)
- **schema Organization 已生成**(虽是默认 template,不是裸 0)
- **canonical 全设**(无重复内容风险)
- **OG image 全设**(社交分享不破)
- **image alt 全设**(图片 SEO 友好)

---

## 🔴 P0 问题 — 必须今天修

### 1. **首页 H1 = 空** (SEO 重大坑)

```js
document.querySelectorAll('h1').length   // = 0 (空数组,渲染时空的是什么)
```
Elementor 模板没渲染出 H1。搜索引擎抓首页看作"无主标题"。  
**修法**:Elementor 编辑首页 → 添加 Heading widget 写 `<h1>` = 文案"海外独享静态住宅IP代理"  
**HTTP 影响**:无 H1 首页,在百度/Google 排名掉一档

### 2. **首页 wx CTA 不可见**

```js
document.body.innerText.includes('yisheng3wantian')  // = false
```
客户看到的页面**正文字里找不到微信**。只在 `<meta name=description>` 里嵌入——客户用眼看不到就只剩加 sidebar/widget。  
**修法**:Elementor 加一个 CTA widget(显眼按钮"加微信 yisheng3wantian")或界面靠底部加 visible 电话/WX 的 section

### 3. **首页 body_chars = 1343 (正文稀薄)**

vs 单篇正文 3000-9000 字。首页这么薄 = 搜索引擎认为"内容不够"  
**修法**:首页 4 个板块下加 expanded content(服务介绍、对比表、案例段、FAQ 8 条)

### 4. **每篇文章 H1 = 空**

5 篇抽检全部 `h1=[]`。标题塞到 title/og 后正文无 H1  
**修法**:每篇文章正文最顶端加一个 `<h1>` 内容 = 文章 main 标题(WordPress 编辑器加 wp:heading block 选 H1,Astra/Astra 子主题会撑住)

### 5. **schema 全是默认 Organization/Person**,**没 Article + 没 FAQPage + 没 BreadcrumbList**

```js
document.querySelectorAll('script[type="application/ld+json"]')[0].textContent
// = {"@context":"https://...","@graph":[{"@type":["Organization","Person"]...}]}
```
**严重度**:GEO 时代,AEO/GEO 引擎(豆包/Kimi/ChatGPT/Perplexity)抓 schema,无 Article 字段=不被识别为"实体文章";无 FAQPage=结构化 Q&A 丢失  
**修法**:装 Rank Math 后**默认已开 Article + BreadcrumbList**——但似乎没生效(或 schema 由某个聚合层代发). 需手动在每篇 schema 末追加:

```json
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"...","acceptedAnswer":{"@type":"Answer","text":"..."}}
  ]
}
```

外加 BreadcrumbList elementor widget 或 WP 自带 breadcrumb

---

## 🟡 P1 问题 — 本周内可改善

### 6. **focus keyword 字段全部空 (37/37)**
Rank Math 没识别 topic intent意味着 sitemap 不会优先 steers topic;整站 SEO 优势发挥不出  

**修法**:批量 POST 给每篇 update meta:

```js
await fetch('/wp-json/wp/v2/posts/522', {
  method:'POST',
  headers: {'X-WP-Nonce':'<nonce>','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'},
  body: JSON.stringify({
    meta: {
      rank_math_focus_keyword: '静态住宅IP跨境收款'
    }
  })
})
```

`rank_math_title` / `rank_math_description` 也应单独设——不能全交给自动从 title/excerpt 抽

### 7. **31/37 篇 excerpt 过短 (<80 字)**

百度/Google SERP snippet 短 = 点击率低  
**修法**:批量 PATCH 写一遍:

```js
meta: {rank_math_description: '80-160 字包含关键词句'}
```

### 8. **0 个 `<details>` 块(无 FAQ 结构化外观)**

FAQ 既能拉 snippet 也能拉 GEO  
**修法**:每篇正文末插 3 条 details/summary 字段 "常见问题" (AEO/GEO 答块)

---

## 🟢 P2 问题 — 锦上添花

- 部分页 Twitter card meta 缺
- 内链可再精化(目前 50+,主要从 right sidebar widgets,关键词密度过高)
- Polylang English 版首页没扫(如果我们海外也想布局)

---

# 下一步行动 (按 ROI 排序)

| Priority | Action | Estimation | ROI |
|---|---|---|---|
| P0-1 | 首页加 H1 + Visible CTA widget + 加 2000 字 trust content | 1 个 Elementor 编辑 + 3 段 | 🟢HIGH(直接拉首页 SEO+ 客户可见 CTA) |
| P0-2 | 抽 5 篇单页顶加 H1 (pid 4/190/192/194/4 抽出来测试) | 1 小时批量 WP REST POST | 🟢HIGH |
| P0-3 | README schema 自智 + Article + FAQPage 全部添加 | 装 Rank Math PRO FTP 手动 . 或手写 JSON-LD 加到 every post | 🟢HIGH |
| P1-1 | 37 篇全 PATCH focus keyword + 写 rank_math_description | 1.5 小时脚本批量 | 🟡MED |
| P1-2 | 31 篇 excerpt 补长到 80-160 字 | 1 小时脚本 | 🟡MED |
| P1-3 | top 5 流量入页面加 FAQ details(3 条 per) | 0.5 小时 | 🟡MED |
| P2-1 | GPU views / 加载速度 / 第三方资源减摩 | 低 | 🟢LOW |

主 P0 三项估计 2-3 小时出成果。

下一步会灼烧 Gesicht 之:
- B 面:客户画像 / 转化漏斗评估(ROI 校正)
- C 面:中文平台全自动论钉(已 3 平台有 cookie,仅差 React button 手扳)
- D 面:小柔自身的认知升级(skill 狮抛、护栏) — 已随各点 patch 完成

等老板看完点选下一面或点插 任命。
