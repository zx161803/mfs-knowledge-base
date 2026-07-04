# GEO + AI 爬虫（sources/posts 单篇）

## llms.txt 提案（Answer.AI 2024-09）

### 三层约定

1. **`/llms.txt`**（根路径 markdown 文件）
   - H1 项目名（必）
   - blockquote 简介（建议）
   - 自由段落（细节）
   - H2 分组 + markdown 链接（按主题分类）

2. **`{page}.md`**（每页 markdown 镜像）
   - URL append `.md` 拿 markdown 版
   - 例：`/page.html.md`
   - 默认子路径 `/index.html.md`

3. **`/llms-ctx.txt` + `/llms-ctx-full.txt`**（concatenated 版本）
   - `llms_txt2ctx` 工具生成
   - full 含 Optional 部分，ctx 不含

### 例子（FastHTML）
```markdown
# FastHTML

> FastHTML 是 python 库，把 Starlette/Uvicorn/HTMX/fastcore FT 整合到 server-rendered hypermedia

重要注意：
- 部分 API 灵感来自 FastAPI 但不兼容
- 与 JS-native web components / vanilla JS 兼容，与 React/Vue/Svelte 不兼容

## Docs

- [Quick start](https://fastht.ml/docs/tutorials/quickstart_for_web_devs.html.md)

## Examples

- [Todo app](https://github.com/AnswerDotAI/fasthtml/blob/main/examples/adv_app.py)
```

### 集成工具
- **vitepress-plugin-llms** — VitePress 自动生成
- **docusaurus-plugin-llms** — Docusaurus
- **llms-txt-php / llms_t**（dotenvx/llmstxt npm） — sitemap→llms.txt
- **Drupal LLM Support 10.3+**

## AI 爬虫 UA 完整名单（2026-05 验证）

| Bot | 公司 | User-Agent 子串 | 用途 |
|---|---|---|---|
| GPTBot | OpenAI | `GPTBot/1.1; +https://openai.com/gptbot)` | 模型训练 |
| ChatGPT-User | OpenAI | `ChatGPT-User/1.0; +https://openai.com/bot)` | 实时 fetch |
| OAI-SearchBot | OpenAI | `OAI-SearchBot/1.0` | search 索引 |
| ClaudeBot | Anthropic | `ClaudeBot/1.0; +claudebot@anthropic.com)` | 训练 |
| Claude-User | Anthropic | `Claude-User` | 实时 |
| Claude-SearchBot | Anthropic | `Claude-SearchBot` | search 索引 |
| anthropic-ai | Anthropic | `anthropic-ai/1.0` | 训练（公开爬） |
| claude-web | Anthropic | `claude-web/1.0` | web 训练 |
| PerplexityBot | Perplexity | `PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)` | 索引 |
| Perplexity-User | Perplexity | `Perplexity-User` | 实时 |
| Applebot-Extended | Apple | `Applebot-Extended/1.0` | Apple Intelligence |
| Meta-ExternalAgent | Meta | `Meta-ExternalAgent` | MetaAI |
| Bytespider | ByteDance | `Bytespider` | 训练（follower 巨多） |
| CCBot | Common Crawl | `CCBot/2.0` | 训练源 |

**robots.txt 配置原则**（mfs 路径）：
- **明确** Allow: GPTBot / ClaudeBot / Claude-SearchBot / PerplexityBot / ChatGPT-User / OAI-SearchBot / anthropic-ai / claude-web / Applebot-Extended / Meta-ExternalAgent / CCBot
- **可选** Disallow: Bytespider（如果服务器压力）

## Cloudflare 数据（2025-05）

- 全球 HTTP 流量 30% 来自 bots
- GPTBot 5%→30% 份额（一年内）
- Anthropic ClaudeBot 6%→10%（2025 早期）
- Bytespider 14.1%→2.4%（被用户喷后下降）
- Anthropic crawl-to-refer = 38000:1（38k 抓 vs 1 推荐）

## GEO vs SEO

| 维度 | SEO | GEO |
|---|---|---|
| 目标 | 排名 1-10 列表 | 被 AI 推荐 / 引用 |
| 评估 | SERP 位置 + 点击 | LLM 输出中提及 |
| 时间尺度 | 月-年 | 即时-周 |
| 技术：schema | JSON-LD | JSON-LD + llms.txt |
| 反向链接 | 关键 | 减弱（AI 训练数据不依赖新链接） |
| 内容形式 | 文 + 多媒体 | 大量问答对 + E-E-A-T 强力 |

## GEO 落地步骤（mfs 可用）

1. **结构化数据**：Schema.org Article / Organization / Service / BreadcrumbList 完整打满
2. **/llms.txt**：根路径放引导文件（H1 + 五大场景描述 + 关键文章链接）
3. **所有页面 .md 镜像**：HTML + .md 两版同步
4. **AI 爬虫白名单**：robots.txt 11 个明确 Allow
5. **站外反向引用**：在知乎/CSDN/简书发文章 footer 指向 mfs 关键页
6. **定期 query 验证**：跑 5 引擎 query 看是否真被 LLM 引用（7/3 实测 0/25 这是真实基线）

## Web Bot Auth（Google 2026 提案）

- 解决"爬虫冒充"问题
- 引入 PKI 证书让 bots 自证身份
- 仍在 W3C 草案阶段，跟进展
