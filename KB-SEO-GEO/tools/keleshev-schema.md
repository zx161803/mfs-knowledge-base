# keleshev/schema · Python 数据轻量验证

> **官方**：https://github.com/keleshev/schema
> **star**：2945 · **last push**：2026-06-20 · **license**：MIT
> **维护**：Vladimir Keleshev · **状态**：✅ 长期稳定

---

## 安装

```bash
pip install schema
```

## 示例

```python
from schema import Schema, And, Or, Use

User = Schema({
    "name": And(str, len),
    "age": And(int, lambda n: 0 < n < 150),
    "email": And(str, Use(lambda s: s.lower()), regex(r"[^@]+@[^@]+\.[^@]+")),
    "role": Or("admin", "user", "guest")
})

User.validate({
    "name": "魔法使",
    "age": 30,
    "email": "ZHX@163.COM",
    "role": "admin"
})
# → email 被 Use 改 zhx@163.com
```

## mfs.xx.kg 用法

### 用 1：sitemap URL 验证

```python
from schema import Schema, SchemaError

Url = Schema({
    "loc": lambda s: s.startswith("https://mfs.xx.kg/"),
    "lastmod": str  # ISO 8601, 用 jsonschema 进一步验证
})

try:
    Url.validate({"loc": "https://mfs.xx.kg/article-1/", "lastmod": "2026-07-04"})
    print("✅ OK")
except SchemaError as e:
    print(f"❌ {e}")
```

### 用 2：API 提交前 basic check

```python
Article = Schema({
    "title": And(str, len),
    "content": And(str, len),
    "tags": And(list, len)  # 至少 1 个
})
```

## 与 jsonschema 互补

| 类型 | 选哪个 |
|---|---|
| 内层结构 / 配置 | keleshev/schema |
| 复杂 / 需要引用 / draft 7 | jsonschema |
| 用户输入 form | jsonschema |
| 临时聚合 / 性能关键 | keleshev/schema |

**mfs 默认组合**：jsonschema 验证 schema.org、keleshev 验证中转结构。
