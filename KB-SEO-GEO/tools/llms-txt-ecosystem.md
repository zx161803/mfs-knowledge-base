# llms.txt 生态工具集

> **背景**：llms.txt 标准由 [AnswerDotAI](https://github.com/AnswerDotAI/llms-txt) 2024-09 提出（Jeremy Howard 等）
> 详情：见 `sources/geo-and-ai.md` + `sources/posts/llms.txt-spec.md`

---

## 主仓: AnswerDotAI/llms-txt (star 2491)

**功能**：spec + 文档 + CLI 工具 `llms_txt2ctx`

```bash
pip install llmstxt
llms_txt2ctx mfs.xx.kg/llms.txt --output llms-ctx.txt
```

## 转换工具：dotenvx/llmstxt (star 145)

**功能**：sitemap.xml → llms.txt 转换器（最实用！）

```bash
npm install -g @dotenvx/llmstxt
llmstxt https://mfs.xx.kg/?sitemap=post > llms.txt
```

**输出示例**（mfs 实测）：
```markdown
# mfs.xx.kg · 跨境 IP 代理五大场景

> 跨境电商 / TikTok 直播 / AI 数据采集 / 静态住宅 IP / GEO 推荐
  5 大业务领域的技术方案 + 微信 yisheng3wantian

## Articles

- [IPv4 双栈 vs IPv6 单栈 选型](https://mfs.xx.kg/ipv4-vs-ipv6/): 比较两者在国内使用场景
- [...]()
```

## Apify actor 备用（31 star）

**功能**：云端爬整个站，再自动组装 llms.txt

```bash
apify call apify/actor-llmstxt-generator --input '{"url": "https://mfs.xx.kg"}'
```

## mfs.xx.kg 落地路径（建议）

| 步骤 | 工具 | 命令 |
|---|---|---|
| 1. 在 `/?sitemap=post` 拉 URL 列表 | curl + jq | `curl "https://mfs.xx.kg/?sitemap=post" \| grep -oE "https://[^<]+" \| sort -u` |
| 2. 抽样 5-10 篇 .md 版 | x-shoot | 见 `scripts/extract_mds.py` |
| 3. 拼装 llms.txt | dotenvx/llmstxt | `llmstxt post-urls.txt > llms.txt` |
| 4. FTP 上传 | curl + Baiduspider UA | `curl -T llms.txt ftp://if0_41891898@mfs.xx.kg/public_html/llms.txt` |
| 5. 加 sitemap robots.txt 告知 | patch | `Sitemap: https://mfs.xx.kg/llms.txt` |
| 6. 24h 后重跑 GEO query 验证 | Python+CDP | 见 `mfs-geo-counter-attack` skill |

## 接入 mfs.xx.kg 的预计工作量

- 首次：6 步（含生成 + 测试），约 2 小时
- 后续：每月重跑一次（加新文章后）
- 效果预期：从 L3 → L4，半个月能看到 AI 引擎开始引用
