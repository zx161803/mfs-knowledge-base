# sethblack/python-seo-analyzer · 站点结构审计

> **官方**：https://github.com/sethblack/python-seo-analyzer
> **star**：1460 · **last push**：2026-06-30
> **用途**：扫整站，抓 SEO 相关数据（title/description/headings/alts/word counts）

---

## 安装

```bash
pip install git+https://github.com/sethblack/python-seo-analyzer.git
```

## 用法

```bash
# CLI
seo-analyzer https://mfs.xx.kg \
  --output-format json \
  --output-file mfs-seo-report.json

# 也支持 --analyze-extra-tags / --analyze-redirects
```

## 报告字段

每 URL 给出：
- `title` + 长度
- `meta description` + 长度
- `<h1>` 个数 + 文本
- `<h2>` 列表
- `<img>` 无 alt 数
- 词数
- 内/外链数
- keyword frequency top 5

## mfs.xx.kg 用法（建议）

1. **每周一次 audit**：
```bash
seo-analyzer https://mfs.xx.kg --max-pages 50 \
  --format csv --output mfs-weekly-audit.csv
```

2. **比对上次报告**：
```python
import csv, sys
old = {row['url']: row for row in csv.DictReader(open(sys.argv[1]))}
new = {row['url']: row for row in csv.DictReader(open(sys.argv[2]))}
for url in new:
    if url in old:
        if new[url]['title'] != old[url]['title']:
            print(f"TITLE 改了：{url}")
```

3. **关键基线指标（7/4 实测预期）**：
- title 字数：50-60 = 优
- meta desc：120-160 = 优
- h1 数量：1 = 优
- 图片无 alt：0 = 优
- 词数：≥ 800 = 优（mfs 文章平均 2500 ✅）

## 与 linkinator + ngstcf 组合

| 工具 | 解决什么 |
|---|---|
| linkinator | 死链 / 4xx / 5xx |
| python-seo-analyzer | 内容结构 / SEO 关键字 |
| ngstcf/ai-seo-auditor | AI 时代 / GEO / llms.txt |
| jsonschema | 标准化 schema.org 验证 |

**4 工具一起用 = 完整 SEO 审计管线**。
