# mfs.xx.kg 应用建议清单（2026-07-04 21:30）

> **老板授权**：去网上找权威文档 + GitHub 工具，把 SEO 和 GEO 效果提高
> **基础盘**：mfs.xx.kg WP 站，40 篇已发文章，5 个板块各自不同进度（L5/L3/L1）
> **新建**：`C:\Users\xiao\KB-SEO-GEO\`（本知识库）+ `C:\Users\xiao\mfs_seo_geo_kb\`（mfs 真实状态板）

---

## P0（本周必做 · 4 项）

### 1. 部署 /llms.txt（4h 工作量）

**依据**：Sources D（llms.txt 标准）+ Tools llms-txt-ecosystem.md

**步骤**：
1. `pip install llms-txt` + `npm install -g @dotenvx/llmstxt`
2. 跑 `python scripts/extract_mds.py` 从 mfs 40 篇 WP REST 抽出 10-15 篇 markdown
3. dotenvx/llmstxt 转 sitemap → llms.txt
4. FTP 上传到 `mfs.xx.kg/llms.txt`
5. robots.txt 加 `Sitemap: https://mfs.xx.kg/llms.txt`

**验收**：5 引擎 query 提及 mfs.xx.kg

### 2. 补放 OAI-SearchBot / Claude-SearchBot（30 分钟）

**依据**：Tools crawler-user-agents.md

**当前 mfs robots.txt**（6/24 写）：
```
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
User-agent: Claude-User  
User-agent: anthropic-ai
User-agent: claude-web
User-agent: PerplexityBot
User-agent: Applebot-Extended
User-agent: Meta-ExternalAgent
Allow: /

User-agent: CCBot
Allow: /
```

**缺**：OAI-SearchBot（OpenAI search indexing）+ Claude-SearchBot（Anthropic search）

**修复**：`cd /d C:\Users\xiao && python update_mfs_robots.py`（脚本生成 12 个 AI bot 完整版）

### 3. 跑 linkinator 死链审计（首次 4h，之后周 1h）

**依据**：Tools linkinator.md

**步骤**：
1. `npm install -g linkinator`
2. 写 `linkinator.config.json`（跳过 wp-admin / wp-login）
3. 跑 `linkinator https://mfs.xx.kg -f json -o mfs-broken-2026-07-04.json`
4. 修复死链 → 重新跑 → 输出 0
5. 设 cron：每周日 03:00 跑

### 4. 跑 ngstcf/ai-seo-auditor GEO/AEO 11 项审计（2h 测试）

**依据**：Tools ngstcf-ai-seo-auditor.md

**步骤**：
1. git clone 仓库
2. 配 .env（OPENAI_API_KEY 可选）
3. `python -m auditor.cli --url https://mfs.xx.kg`
4. 报告存 `mfs-geo-audit-2026-07-04.json`
5. 对照 11 项打分，把分数写进本文件 7/11 周更新

---

## P1（下周做 · 3 项）

### 5. mfs SEO 文章结构统一化（4h）

**依据**：Sources A Google SC SEO Starter Guide + Tools sethblack-python-seo-analyzer.md

**mfs 当前**：40 篇 pid 标题/desc/字数差异大
**修法**：跑 seo-analyzer + 按 Google SC 规约统一 title 50-60 / desc 120-160 / h1 仅 1

### 6. 跑 python-jsonschema 合规性验证（6h）

**依据**：Sources C Schema.org + Tools python-jsonschema.md

**步骤**：
1. `pip install jsonschema`
2. 写 `mfs-article.schema.json`（按 Article 完整规则）
3. `python scripts/validate_mfs_schemas.py`
4. 把每篇文章 WP REST 的 `content.rendered` 切片 → 提取 JSON-LD → jsonschema.validate
5. 输出每篇分数 + 失败项

### 7. mfs 5 平台验证 HTML 补传（老板 5 分钟 × 5 项）

**依据**：Sources F 中文搜索

| 平台 | 验证 HTML | 老板操作 |
|---|---|---|
| Baidu | baidu_verify_*.html | 站长后台下载 → FTP 上传 public_html/ |
| Google | google*.html | Search Console 后台下载 → FTP 上传 |
| Bing | BingSiteAuth.xml | WM 后台下载 → FTP 上传 |
| Yandex | yandex_*.html | Yandex WM 后台下载 → FTP 上传 |
| 360 | so*.html | 360 站长后台下载 → FTP 上传 |

**5 平台验证 HTML 现全部 404**（Baiduspider UA 实测 7/4）→ 补传后信任度立刻 +1

---

## P2（持续 · 4 项）

### 8. 每月跑 ngstcf 审计，把分数升
### 9. 每月生成新 llms.txt（文章变多后）
### 10. mfs sitemap 加 Wikidata / Wikipedia 链接
### 11. mfs 主页加入 llms.txt、ai.json 元数据

---

## ⚠️ 老板明示要注意

1. **5 引擎 GEO query 0/25**（7/4 实测） — 不是工具问题，**必须老板主 chrome 真实登录态**
2. **百度换空间 trust 重置**（6/16 起 0 索引） — 至少 3 个月才回 L3
3. **schema.org 文档国内不通** — 评估要不要把 KB-SEO-GEO 推到云服务器

---

## 📈 预期效果（4 周后）

| 板块 | 当前 | 4 周后 | 关键依赖 |
|---|---|---|---|
| 站内内容 | L5 | L5 | - |
| SEO 索引（提交端） | L5 | L5 | - |
| SEO 索引（收录端） | L3 | L4 | P0-3 + P1-7 |
| 中文 4 平台 | L3 | L4 | 7 月动作 |
| GEO 反向引用 | L3 | L4 | P0-1 (llms.txt) |
| 海外双仓 | L5 | L5 | - |
