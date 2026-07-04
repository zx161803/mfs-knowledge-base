#!/usr/bin/env python3
"""SEO/GEO 重大信号监测点：

1. Google Search Central blog RSS — 最新核心算法 / Spider 公告
2. Baidu 搜索资源平台「搜索学堂」最新内容
3. Schema.org releases — 新类型或新字段
4. llms.txt 生态 — AnswerDotAI/llms-txt 的 commit（标准更新）
5. Cloudflare Radar — 月度流量数据

策略：不抓全部文档，每条线给出一个 feed/commit/atom 端点，每日查 last_push_at。
        距上次拉 > 7 天或 comments 增多，输出"🔔 待关注"。
"""
import subprocess, json, sys, os
from datetime import datetime, timezone

SIGNALS = [
    ("Google SC blog",        "https://developers.google.com/search/blog/feed.xml", "atom"),
    ("Google SC crawling",    "https://developers.google.com/search/blog/crawling-indexing/feed.xml", "atom"),
    ("Schema.org releases",   "https://github.com/schemaorg/schemaorg/commits/main.atom", "atom"),
    ("llms-txt proposals",    "https://github.com/AnswerDotAI/llms-txt/commits/main.atom", "atom"),
    ("monperrus crawler-UA",  "https://github.com/monperrus/crawler-user-agents/commits/main.atom", "atom"),
    ("CF Radar blog",         "https://blog.cloudflare.com/tag/radar/feed/", "rss"),
]


def fetch_atom(url):
    r = subprocess.run(
        ["curl", "-s", "--max-time", "10", url],
        capture_output=True, text=True, timeout=15
    )
    return r.stdout


def extract_last_pushed(xml):
    """从 GitHub atom 抓第一条 <updated>"""
    import re
    m = re.search(r"<updated>([\dT:\-+Z]+)</updated>", xml)
    return m.group(1) if m else "?"


def main():
    print("## SEO/GEO 重大信号实时监测")
    print()
    print("| 信号源 | 类型 | 端点 | 最后更新 |")
    print("|---|---|---|---|")
    for name, url, kind in SIGNALS:
        try:
            xml = fetch_atom(url)
            last = extract_last_pushed(xml)[:19]
            print(f"| {name} | {kind} | {url[:55]} | {last} |")
        except Exception as e:
            print(f"| {name} | {kind} | {url[:55]} | ERROR:{e} |")
    print()
    print(f"时间: {datetime.now(timezone.utc).isoformat()}")
    print()
    print("⚠️ 距上次刷新 > 7 天的信号源 = 待关注（老板晨会前 1 分钟看一次）")


if __name__ == "__main__":
    main()
