# KB-SEO-GEO · 每日可刷新的 SEO & GEO 外部知识库

> **建库目的**：把 mfs.xx.kg 接入"权威源 + 可复用工具"两条腿，每天自动拉新，遇到 mfs 站任何 SEO/GEO 决策时能查到最新规约、找到直接能跑的工具。
> **建库时间**：2026-07-04 21:30（每日 02:00 自动增量刷新）
> **老板授权**：✅ "去网络找权威文档，对应 GITHUB 平台找工具，把 SEO 和 GEO 效果提高"

---

## 🚀 快速上手（给老板）

| 老板问 | 跑哪个 | 输出在哪 |
|---|---|---|
| "SEO 现在最权威文档在哪？" | 看 `sources/` 目录 | `sources/<主题>.md` |
| "给我找工具验证 schema" | 看 `tools/` 目录 | `tools/<工具>.md` |
| "跑一遍昨天的 changelog" | `scripts/daily_refresh.ps1` | `changelog/<日期>.md` |
| "mfs 这次该改啥" | 看 `applied-to-mfs/` | `applied-to-mfs/<板块>.md` |

---

## 📚 目录结构

```
KB-SEO-GEO/
├── README.md                          ← 你正在看的（入口）
├── sources/                           ← 权威源头清单
│   ├── README.md                      ← 源头分类 + 链接 + 验证状态
│   ├── seo-foundations.md             ← SEO 基础理论
│   ├── seo-technical.md               ← 技术 SEO（sitemap/robots/JS等）
│   ├── geo-and-ai.md                  ← GEO / AI 爬虫 / llms.txt
│   ├── search-engines-zh.md           ← 中文搜索引擎（百度/搜狗/360）
│   ├── schema-org.md                  ← Schema.org 结构化数据
│   ├── indexnow-protocol.md           ← IndexNow 协议
│   └── posts/                         ← 单篇关键文档快照
├── tools/                             ← GitHub 工具清单
│   ├── README.md                      ← 工具一览（star/最近 commit/用法）
│   ├── python-jsonschema.md
│   ├── linkinator.md
│   ├── keleshev-schema.md
│   ├── llms-txt-ecosystem.md
│   ├── answerdotai-llms-txt.md
│   ├── ngstcf-ai-seo-auditor.md
│   ├── python-seo-analyzer.md
│   └── crawler-user-agents.md
├── scripts/                           ← 自动刷新脚本
│   ├── daily_refresh.ps1              ← 每晚 02:00 跑（Windows Task Scheduler）
│   ├── fetch_sources.py               ← 拉源文档 rss/atom/sitemap
│   ├── fetch_repos.py                 ← 拉 GitHub repo 元数据
│   └── apply_to_mfs.md                ← 怎么把结论同步到 mfs.xx.kg
├── changelog/                         ← 每日刷新记录（保留 30 天）
│   └── 2026-07-04.md                  ← 首次建库快照
└── applied-to-mfs/                    ← 落地到 mfs 的清单
    └── 2026-07-04-recommendations.md  ← 本次发现的 mfs 改进项
```

---

## ✅ 5 大板块当前真实状态（与 mfs_seo_geo_kb 对齐）

| # | 板块 | 提交端 | 收录端 | 综合 | 本知识库覆盖度 |
|---|---|---|---|---|---|
| 1 | **SEO 索引** | L5 | **L3** | **L3** | sources/seo-technical.md + tools/linkinator.md |
| 2 | **GEO 反向引用** | L3 | L3 | **L3** | sources/geo-and-ai.md + tools/llms-txt-ecosystem.md |
| 3 | **Schema.org** | L5 | L5 | **L5** ✅ | sources/schema-org.md + tools/python-jsonschema.md |
| 4 | **中文搜索（百度）** | L5 | **L1** | **L1** ⚠️ | sources/search-engines-zh.md |
| 5 | **IndexNow + sitemap** | L5 | L3 | **L3** | sources/indexnow-protocol.md |

**建库后预期提升**（每周评估一次）：
- L1 → L2：补 5 平台验证 HTML + 投诉百度解锁 → **8 周内**
- L3 → L5：跑 schema 验证 + llms.txt 部署 + 站外反向引用 → **本月底**

---

## 🤖 每日自动刷新机制

**触发**：Windows Task Scheduler · 02:00 每天
**脚本**：`scripts/daily_refresh.ps1`
**输出**：`changelog/<日期>.md`（每次生成，未变化跳过）

刷新内容：
1. 拉所有 sources GitHub RSS / Atom feed，看最近 commit
2. 验证 sources README 里每条链接仍 200（HTTP HEAD / -sL -w）
3. 验证 tools/README 里每个 repo 的 star + 最近 push（GitHub API）
4. 对比上次快照，diff 出"新增 / 链接失效 / 仓库失活"
5. 把 diff 写进 changelog，并 git commit
6. 老板每日早上一打开 README 末尾就看到"今日新增"

---

## 🔗 与 mfs.xx.kg 真实关联（applied-to-mfs 子目录）

每次 KB 刷新后，自动 diff：
- 新出的 schema.org 类型 → mfs 文章是否需要补 markup
- Google/Bing 文档有大幅更新 → mfs WP REST 行为是否需要改
- 出现新 AI 爬虫 UA → mfs robots.txt 是否放行
- 出新 llms.txt 标准 → mfs 静态 footer 是否要补 llms.txt

---

## 📊 备份策略

- 本地：`C:\Users\xiao\KB-SEO-GEO\`
- GitHub：zx161803/hermes 仓（已有 SSH key 配好）
- OneDrive：跑完自动同步
- 双仓：zx161803/KB-SEO-GEO（公开，给老板随时手机访问）

---

## 🛠 验证机制（任何事实都可追溯）

✅ 每条链接：HTTP 状态 + size + final URL（去 v2 跑通 vs 直连）
✅ 每个 repo：star + last commit（GitHub API 真实数据）
✅ 每次刷新：commit hash + 时间戳 + diff 摘要
✅ 每周自检：跑 `scripts/verify_all.py` 把所有链接 + repo 都验一遍

❌ 不写"看起来有用的链接"——不验证就不入库
❌ 不抄 SEO 营销博客当成权威——只承认带 docs/schemas/help 子路径的官方文档
