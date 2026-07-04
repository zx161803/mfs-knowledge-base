# monperrus/crawler-user-agents · AI bot UA 清单

> **官方**：https://github.com/monperrus/crawler-user-agents
> **star**：1380 · **last push**：2026-07-02 · **license**：MIT
> **维护**：Nicolas Monperrus（学术 / 工具型）
> **状态**：✅ 行业**唯一权威** UA 库

---

## 三种使用方式

### 1. JSON 文件直读

```bash
curl -s https://raw.githubusercontent.com/monperrus/crawler-user-agents/main/crawler-user-agents.json | python -c "import sys, json; data=json.load(sys.stdin); [print(c['pattern']) for c in data if 'pattern' in c]"
```

### 2. PyPI 包

```bash
pip install crawler-user-agents
```

```python
from crawler_user_agents import bots
for bot in bots:
    print(bot['pattern'], '|', bot.get('operator', '?'), '|', bot.get('description', '?')[:80])
```

### 3. npm 包

```bash
npm install crawler-user-agents
```

```js
const crawlers = require('crawler-user-agents');
console.log(crawlers.filter(c => c.pattern.includes('GPTBot')));
```

---

## 内容（1228 bots 总览，2026-07 抽样）

| Bot | 模式 | 操作者 |
|---|---|---|
| GPTBot | `GPTBot` | OpenAI |
| ChatGPT-User | `ChatGPT-User` | OpenAI |
| OAI-SearchBot | `OAI-SearchBot` | OpenAI |
| ClaudeBot | `ClaudeBot` | Anthropic |
| Claude-User | `Claude-User` | Anthropic |
| Claude-SearchBot | `Claude-SearchBot` | Anthropic |
| anthropic-ai | `anthropic-ai` | Anthropic |
| claude-web | `claude-web` | Anthropic |
| PerplexityBot | `PerplexityBot` | Perplexity |
| Perplexity-User | `Perplexity-User` | Perplexity |
| Applebot | `Applebot` | Apple |
| Applebot-Extended | `Applebot-Extended` | Apple |
| Meta-ExternalAgent | `Meta-ExternalAgent` | Meta |
| Meta-ExternalFetcher | `Meta-ExternalFetcher` | Meta |
| Bytespider | `Bytespider` | ByteDance |
| CCBot | `CCBot/2.0` | Common Crawl |
| Google-Extended | `Google-Extended` | Google |
| DuckDuckBot | `DuckDuckBot` | DuckDuckGo |
| YandexBot | `YandexBot` | Yandex |
| SemrushBot | `SemrushBot` | Semrush |
| AhrefsBot | `AhrefsBot` | Ahrefs |
| MJ12bot | `MJ12bot` | Majestic |

---

## mfs.xx.kg 用法

### 1. 生成 robots.txt 放行 AI

```python
import json, urllib.request
data = json.loads(urllib.request.urlopen(
    'https://raw.githubusercontent.com/monperrus/crawler-user-agents/main/crawler-user-agents.json').read())

AI_BOTS = ['GPTBot', 'ChatGPT-User', 'OAI-SearchBot', 
           'ClaudeBot', 'Claude-User', 'Claude-SearchBot',
           'anthropic-ai', 'claude-web',
           'PerplexityBot', 'Perplexity-User',
           'Applebot', 'Applebot-Extended',
           'Meta-ExternalAgent', 'Meta-ExternalFetcher',
           'Google-Extended', 'CCBot', 'DuckDuckBot']

with open('robots.txt', 'w') as f:
    f.write('# mfs.xx.kg robots.txt\n\nUser-agent: *\nAllow: /\n\n')
    for bot in AI_BOTS:
        f.write(f'User-agent: {bot}\nAllow: /\n\n')
```

### 2. 服务端日志审计（awk 一行）

```bash
# 看哪种爬虫来得最多
awk '{print $NF}' /var/log/mfs-xx-kg.com.access.log | grep -E 'GPTBot|ClaudeBot|PerplexityBot|Bytespider' | sort | uniq -c | sort -rn | head
```

### 3. mfs 当前 robots.txt 复盘

mfs 6/24 已加 9 个 AI 爬虫 — `sources/posts/mfs-robots-may-2026.md` 留有这 9 个清单。

---

## ⚠️ 别忘了：定期跑

7/4 实测：**mfs 装了 9 个 AI bot 放行**，但**跨 profile cookies 复制失效**导致 GEO query 验证 0/25。

- 跑 6/24 之前：放行 = 允许爬
- 跑 6/24 之后：放行 = 允许爬 + 允许 AI fetch（query）
- 7/4 实测：**query 时要登录态**才回
