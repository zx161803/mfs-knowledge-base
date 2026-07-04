# AnswerDotAI/llms-txt · 标准提案仓

> **官方**：https://github.com/AnswerDotAI/llms-txt
> **star**：2491 · **last push**：2026-06-09 · **许可**：Apache 2.0
> **作者**：Jeremy Howard (fast.ai / Answer.AI 联合创始人)
> **状态**：✅ 行业事实标准

---

## 三件套

1. **`/llms.txt`**（推荐 spec）
2. **`{page}.md` 镜像**（任意路径 append `.md`）
3. **`llms-ctx.txt` / `llms-ctx-full.txt`**（生成器产物）

## Python 工具 `llms_txt2ctx`

安装：
```bash
pip install llms-txt
```

基础用法：
```bash
llms_txt2ctx https://mfs.xx.kg/llms.txt \
  --output ctx-full.txt \
  --include-optional
```

Python API：
```python
from llms_txt import parse, expand

parsed = parse(open("llms.txt").read())
ctx = expand(parsed, include_optional=True)
with open("llms-ctx-full.txt", "w") as f:
    f.write(ctx.to_text())
```

## mfs.xx.kg 后续动作（参考）

1. 创建 `https://mfs.xx.kg/llms.txt`
2. 加入 sitemap robots.txt
3. 在机器人用的 .md 镜像（每文章 1 个）
4. `llms_txt2ctx` 拼成 full ctx（让 AI 一次性看完）
5. 验证：5 引擎 query 都引用 mfs

---

## 与"robots.txt for AI" 的关系

`llms.txt` 是 **告诉 AI 内容在哪**，**不是** 阻止/放行的。
放行 AI 用 `robots.txt`（`User-agent: GPTBot Allow: /`）
用 llms.txt 引导焦点

---

## 集成（VitePress / Docusaurus / Drupal 10.3+）

- `vitepress-plugin-llms` — VitePress 自动
- `docusaurus-plugin-llms` — Docusaurus 自动
- `drupal/llm_support` — Drupal 自动
- WordPress: 没有 plugin，需要手写 — **mfs 走这条**
