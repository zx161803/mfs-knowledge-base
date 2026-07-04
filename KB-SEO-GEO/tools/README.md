# GitHub 工具清单（已实测可用）

> **建库时间**：2026-07-04 21:30
> **更新周期**：每日由 `scripts/fetch_repos.py` 拉 star / last commit
> **准入标准**：star ≥ 100 或 last commit ≤ 60 天 + 描述清晰 + 可 npm/pip/clone 直接跑

---

## ✅ 入库 9 个（按推荐顺序排序）

| # | 仓库 | star | last push | 用途 | 适合 mfs 哪部分 |
|---|---|---|---|---|---|
| 1 | [python-jsonschema/jsonschema](tools/python-jsonschema.md) | 4956 | 2026-06-29 | JSON Schema 标准验证 | schema-org 验证 |
| 2 | [keleshev/schema](tools/keleshev-schema.md) | 2945 | 2026-06-20 | 轻量 Python 数据验证 | URL/sitemap 结构 |
| 3 | [AnswerDotAI/llms-txt](tools/answerdotai-llms-txt.md) | 2491 | 2026-06-09 | llms.txt 标准仓 + spec | GEO 必装 |
| 4 | [sethblack/python-seo-analyzer](tools/python-seo-analyzer.md) | 1460 | 2026-06-30 | 站点结构审计 | 站内技术 SEO |
| 5 | [monperrus/crawler-user-agents](tools/crawler-user-agents.md) | 1380 | 2026-07-02 | AI bot UA 清单 | 放行参考 |
| 6 | [JustinBeckwith/linkinator](tools/linkinator.md) | 1228 | 2026-07-03 | Broken link checker | 死链审计 |
| 7 | [json-schema-org/JSON-Schema-Test-Suite](tools/python-jsonschema.md#test-suite) | 731 | 2026-07-01 | JSON Schema 测试套 | 合规性 |
| 8 | [dotenvx/llmstxt](tools/llms-txt-ecosystem.md) | 145 | 2026-03-05 | sitemap→llms.txt 转换器 | GEO 自动生成 |
| 9 | [apify/actor-llmstxt-generator](tools/llms-txt-ecosystem.md#apify) | 31 | 2026-05-25 | Apify actor llms.txt | 备用 |
| 10 | [ngstcf/ai-seo-auditor](tools/ngstcf-ai-seo-auditor.md) | 8 | 2026-05-13 | GEO/AEO 11 项审计 | 适配 2025/2026 |

## ❌ 不入库（实测不达标）

| 仓库 | star | 原因 |
|---|---|---|
| seanhecking/seo-scripts | 0 | 太小 |
| TryGeoSuite/llms-txt-generator | 2 | 太小 |
| donofden/python-validate-json-schema | 6 | 6 年没动 |
| johnnyreilly/schemar | 5 | 1.5 年没动 |

---

## 🔧 实操脚本（已就绪在 `tools/cloned/` 或 PyPI）

```bash
# 1. schema 验证
pip install jsonschema
python -c "import jsonschema, json; jsonschema.validate(json.load(open('x.json')), json.load(open('mfs-article.schema.json')))"

# 2. Python 数据验证
pip install schema
python -c "from schema import Schema; Schema({'url': str, 'lastmod': str}).validate({'url': 'x', 'lastmod': 'y'})"

# 3. llms.txt 生成（从 sitemap）
npm install -g @dotenvx/llmstxt
llmstxt https://mfs.xx.kg/sitemap.xml > llms.txt

# 4. 站点 SEO 审计
pip install git+https://github.com/sethblack/python-seo-analyzer.git
python -m seo_analyzer https://mfs.xx.kg

# 5. 链接检查
npx linkinator https://mfs.xx.kg --skip "^https://mfs.xx.kg/wp-admin/"

# 6. AI bot UA 列表（JSON）
curl https://raw.githubusercontent.com/monperrus/crawler-user-agents/main/crawler-user-agents.json
```

---

## 🔄 自动化计划

`scripts/fetch_repos.py` 每日：
1. 拉这 11 个 repo 的 GitHub API 元数据
2. 比对 last commit，距上次 > 30 天 → 标 `[STALE]`
3. 比对 star 升降 → 写 changelog
4. 触发 webhook 到 Telegram（可选）

## 🚧 后续规划

- 入库 SEO 监测：lighthouse-ci、WebPageTest
- 入库 SEO 桌面工具：screaming-frog 开源替代
- 入库 sitemap 校验：lxml-based 国产工具

---

## ⚠️ 真假坑提醒

| 项目 | 真假 |
|---|---|
| ngstcf/ai-seo-auditor 8 star | **真的小项目**——但 2026-05-13 还有 commit，跟得上 GEO 节奏 |
| JustinBeckwith/linkinator 1228 star | **真的**——Google 出品，立场中立 |
| monperrus/crawler-user-agents 1380 star | **真的**——业界标准 AI bot UA 库 |
| dotenvx/llmstxt 145 star | 确实不大但是 dotenvx 官方维护 |

**结论**：star 数对工具质量有参考，但不是绝对。`last commit + active maintainer + 设计合理` 三件套更靠谱。
