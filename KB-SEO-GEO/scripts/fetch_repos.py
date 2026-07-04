#!/usr/bin/env python3
"""拉 KB-SEO-GEO/tools/README.md 里所有 GitHub 仓库,获取 star + last push。

输出：mark-down 表格
"""
import json, subprocess, re, sys, os
from datetime import datetime, timezone

TOOLS_MD = os.path.join(os.path.dirname(__file__), "..", "tools", "README.md")


def parse_repos(md_text: str):
    """提取 [owner/repo](tools/owner-repo.md) 形式。
    表格形如：| 2 | [python-jsonschema/jsonschema](tools/python-jsonschema.md) | star | last_push |
    """
    # 这种格式匹配：| [org/repo](tools/...) |
    repos = []
    for m in re.finditer(r"\[([\w-]+/[\w.-]+)\]\(tools/", md_text):
        repos.append(m.group(1))
    return list(dict.fromkeys(repos))


def fetch_repo(repo: str):
    try:
        r = subprocess.run(
            ["curl", "-s", "--max-time", "8",
             "-H", "User-Agent: kb-seo-geo/1.0",
             f"https://api.github.com/repos/{repo}"],
            capture_output=True, text=True, timeout=10
        )
        d = json.loads(r.stdout) if r.stdout.strip() else {}
        return {
            "stars": d.get("stargazers_count", "?"),
            "pushed_at": (d.get("pushed_at") or "?")[:10],
            "archived": d.get("archived", False),
            "license": (d.get("license") or {}).get("spdx_id", "?") if isinstance(d.get("license"), dict) else "?",
            "open_issues": d.get("open_issues_count", "?"),
        }
    except Exception as e:
        return {"stars": "?", "pushed_at": "?", "archived": False, "license": "?", "open_issues": "?", "error": str(e)}


def main():
    md_path = os.path.abspath(TOOLS_MD)
    if not os.path.exists(md_path):
        print("❌ 找不到 tools/README.md")
        sys.exit(1)
    md = open(md_path).read()
    repos = parse_repos(md)
    print(f"📦 共 {len(repos)} 个仓库待查")
    print()
    print("| 仓库 | star | last_push | license | issues | archived |")
    print("|---|---:|---|---|---:|---|")
    stale = []
    for repo in repos:
        info = fetch_repo(repo)
        marker = ""
        if info.get("archived"):
            marker = " 🗑️"
        if info["pushed_at"] != "?" and info["pushed_at"] < "2026-05-01":
            marker += " ⚠️STALE"
            stale.append((repo, info["pushed_at"]))
        print(f"| {repo} | {info['stars']} | {info['pushed_at']} | {info['license']} | {info['open_issues']} |{marker}|")
    print()
    print(f"## Repos 拉取 {len(repos)} 个")
    print(f"- 时间: {datetime.now(timezone.utc).isoformat()}")
    print(f"- ⚠️STALE: {len(stale)} (last push > 2026-05-01)")
    if stale:
        for repo, date in stale:
            print(f"  - {repo}: last push {date}")


if __name__ == "__main__":
    main()
