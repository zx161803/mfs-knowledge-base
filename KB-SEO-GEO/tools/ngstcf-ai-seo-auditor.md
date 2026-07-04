# ngstcf/ai-seo-auditor · GEO/AEO 审计工具

> **官方**：https://github.com/ngstcf/ai-seo-auditor
> **star**：8 · **last push**：2026-05-13 · **license**：MIT
> **状态**：🌱 **新兴小众**,但适配 2025/2026 GEO/AEO 视角

---

## 背景

2025 年后所有 SEO 工具都补"AI 时代视角"，这个项目是少数专注 GEO（Generative Engine Optimization）+ AEO（Answer Engine Optimization）+ AI Discovery Files（llms.txt/llms-full.txt/ai.json）的开源工具。

## 11 项审计维度

1. **AI Discovery Files** — llms.txt / llms-full.txt / ai.json 是否部署
2. **Structured Data** — Article / Organization / FAQ / HowTo / Product 5 类
3. **AI Crawler Permissions** — robots.txt 是否放行主流 AI bot
4. **E-E-A-T Signals** — 作者 / 联系 / 来源 / 时间戳
5. **Content Freshness** — lastmod 频率 / 内容更新周期
6. **FAQ Markup** — FAQPage schema + 真实问答段落
7. **Comparison Tables** — 比较页 schema + 表格 HTML
8. **Multi-modal Coverage** — 图片 alt / 视频 transcript
9. **Topical Authority** — 主题 cluster / 内部链接结构
10. **Citation Accuracy** — 引用 / 来源链真实性
11. **Reputation Signals** — Wikipedia / Wikidata / 社交平台

## 安装

```bash
git clone https://github.com/ngstcf/ai-seo-auditor
cd ai-seo-auditor
pip install -r requirements.txt
```

## 用法

```bash
# 1. 设置 API key（可选，用于 LLM-powered 分析）
echo "OPENAI_API_KEY=sk-..." > .env

# 2. 命令行审计
python -m auditor.cli --url https://mfs.xx.kg

# 3. 输出报告
# → 11 项分类、分数、修复建议
```

## mfs.xx.kg 现状对照（7/4 实测）

| 维度 | mfs 状态 | 修复路径 |
|---|---|---|
| 1. AI Discovery Files | ❌ 缺 | 见 `tools/llms-txt-ecosystem.md` |
| 2. Structured Data | ✅ 5 类 | 补 BreadcrumbList + WebSite |
| 3. AI Crawler Permissions | ✅ 9 个放行 | 补 OAI-SearchBot + Claude-SearchBot |
| 4. E-E-A-T | 🟡 部分（trust block） | 加 About 作者个人信息 |
| 5. Content Freshness | ✅ | 已 lastmod 维护 |
| 6. FAQ Markup | ✅ 5 篇 | 扩到全部 40 篇 |
| 7. Comparison Tables | 🟡 部分（IP 类型对比） | 补 schema/Product |
| 8. Multi-modal | 🟡 图片 alt + 视频缺 | 加 alt + 录短视频 |
| 9. Topical Authority | 🟡 7 分类 + 14 标签 | 强化 internal linking |
| 10. Citation Accuracy | ✅ 已加源链 | - |
| 11. Reputation Signals | ❌ 缺 | 加 Wikidata entry |

## 8 star 的真真假假

- ✅ **真小**：star 8 确实少
- ✅ **真新**：commit 2026-05-13 与 2025 GEO 标准同步
- ✅ **真适配 2026**：项目文档明确说"for 2025 GEO/AEO optimization"
- ❌ **未广泛验证**：社区小，没踩完所有坑（**这是真实风险，使用前自行验收**）

## 实战路径

老板启用本工具做 mfs 站的真实 baseline：
1. 先跑一次，把报告存 `applied-to-mfs/2026-07-04-audit-raw.json`
2. 把 11 项分数写进 `applied-to-mfs/2026-07-04-recommendations.md`
3. 每两周再跑一次，比对分数上升
