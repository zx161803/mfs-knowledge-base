# python-jsonschema · JSON Schema 标准验证库

> **官方**：https://github.com/python-jsonschema/jsonschema
> **star**：4956 · **last push**：2026-06-29 · **license**：MIT
> **维护**：Julian Berman + 团队 · **状态**：✅ **活跃生产级**

---

## 1 分钟安装

```bash
pip install jsonschema
```

Python ≥ 3.8 都行；mfs 主机 Python 3.11 ✅

## 5 行代码示例

```python
import json, jsonschema

# 1. 写 schema
schema = {
    "type": "object",
    "required": ["headline", "author", "datePublished"],
    "properties": {
        "headline": {"type": "string", "minLength": 5, "maxLength": 110},
        "author": {
            "type": "object",
            "required": ["name"],
            "properties": {"name": {"type": "string"}}
        },
        "datePublished": {"type": "string", "format": "date-time"},
        "@type": {"enum": ["Article", "NewsArticle", "BlogPosting"]}
    }
}

# 2. 准备 payload（mfs 文章的 schema.org JSON-LD 切下的东西）
payload = {
    "@type": "Article",
    "headline": "亚马逊多店铺防关联 IP 配置",
    "author": {"name": "魔法师"},
    "datePublished": "2026-06-24T08:00:00+08:00"
}

# 3. 验证
jsonschema.validate(payload, schema)   # 通过 = 无异常
```

## mfs.xx.kg 用法

### 用 1：每篇文章 PATCH 后验

```bash
# 假设 mfs 已有 7 类 schema 已落 WP REST，本文作为 sanity check
python scripts/validate_mfs_schemas.py
```

### 用 2：CI 集成

`.github/workflows/validate.yml`:
```yaml
- uses: actions/checkout@v3
- run: pip install jsonschema
- run: python scripts/validate_all.py
```

## 进阶：FormatChecker

内建支持 `format: uri / date-time / email / ipv4 / ipv6 / uuid` 7 种格式；可注册自定义的 `format_checker` 把"看起来对但其实错"的问题暴露。

## 与 [keleshev/schema](keleshev-schema.md) 对比

| 维度 | jsonschema | keleshev |
|---|---|---|
| 体积 | 大（多 draft） | 轻量 |
| 学习曲线 | 陡（要先懂 draft 4/6/7/2020-12） | 平缓 |
| 适合 | HTTP API validation / 配置 | 内嵌数据 |
| mfs 用 | JSON-LD schema 验证 | 快速埋点 |

**建议**：mfs 站上 **两个都装**—— jsonschema 验严格外发 schema，keleshev/schema 验内部临时结构。
