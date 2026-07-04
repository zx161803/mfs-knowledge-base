#!/usr/bin/env python3
"""拉 KB-SEO-GEO/sources/README.md 里所有源头 URL，并发验证可达性。

输出：mark-down 表格
"""
import json, subprocess, re, sys, os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

SOURCES_MD = os.path.join(os.path.dirname(__file__), "..", "sources", "README.md")


def parse_urls(md_text: str):
    urls = []
    for m in re.finditer(r"\| (https?://[^ |\s]+) \|", md_text):
        urls.append(m.group(1))
    return list(dict.fromkeys(urls))


def check_url(url: str) -> tuple:
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", "6",
             "-H", "User-Agent: kb-seo-geo/1.0",
             "-o", "/dev/null",
             "-w", "%{http_code}|%{size_download}|%{url_effective}|%{time_total}",
             url],
            capture_output=True, text=True, timeout=8
        )
        parts = r.stdout.strip().split("|")
        if len(parts) != 4:
            return (url, "ERROR", "0", url, "9999ms")
        code, size, final, t = parts
        return (url, code, size, final, f"{float(t)*1000:.0f}ms")
    except subprocess.TimeoutExpired:
        return (url, "TIMEOUT", "0", url, "6000ms")
    except Exception as e:
        return (url, f"ERROR:{e}"[:30], "0", url, "0ms")


def main():
    md_path = os.path.abspath(SOURCES_MD)
    if not os.path.exists(md_path):
        print("❌ 找不到 sources/README.md")
        sys.exit(1)
    md = open(md_path).read()
    urls = parse_urls(md)
    print(f"📋 共 {len(urls)} 条源头 URL 待并发验证（worker=8, timeout=6s）")
    print()
    print("| URL | HTTP | size | time | final |")
    print("|---|---:|---:|---:|---|")
    rows = [None] * len(urls)
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(check_url, u): i for i, u in enumerate(urls)}
        for f in as_completed(futures):
            i = futures[f]
            rows[i] = f.result()
    pass_cnt = fail_cnt = timeout_cnt = 0
    for row in rows:
        url, code, size, final, t = row
        marker = "✅" if code.startswith("2") else ("↩️" if code.startswith("3") else "❌")
        if code.startswith("2"):
            pass_cnt += 1
        elif code.startswith("3"):
            pass_cnt += 1
        elif "TIMEOUT" in code:
            timeout_cnt += 1
            fail_cnt += 1
        else:
            fail_cnt += 1
        print(f"| {url[:55]} | {code} | {size} | {t} | {final[:50]} | {marker}")
    print()
    print(f"## Sources 验证 {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print(f"- 总数: {len(urls)}")
    print(f"- ✅ 通过 (2xx/3xx): {pass_cnt - timeout_cnt}")
    print(f"- ❌ 失败: {fail_cnt - timeout_cnt}")
    print(f"- ⏱ TIMEOUT (走 V2 才能验): {timeout_cnt}")


if __name__ == "__main__":
    main()
