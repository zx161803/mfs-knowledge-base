# JustinBeckwith/linkinator · Broken link checker

> **官方**：https://github.com/JustinBeckwith/linkinator
> **作者**：Justin Beckwith (Google) · **star**：1228 · **last push**：2026-07-03
> **状态**：✅ 行业事实标准（linkinator = broken link checker 代名词）

---

## 安装

```bash
npm install -g linkinator
```

或 Docker：
```bash
docker run -it --rm -p 8080:8080 ghcr.io/JustinBeckwith/linkinator linkinator https://mfs.xx.kg
```

## 用法

```bash
# 基础
linkinator https://mfs.xx.kg --skip "^https://mfs.xx.kg/wp-admin/" --skip "^https://mfs.xx.kg/wp-login"

# 配置化
cat > linkinator.config.json << 'EOF'
{
  "recurse": true,
  "skip": [
    "^https://mfs.xx.kg/wp-admin",
    "^mailto:"
  ],
  "format": "JSON"
}
EOF

linkinator https://mfs.xx.kg
```

## mfs.xx.kg 用法

定期死链审计 → 补 mfs 文章内引用 + 401/404 → 修复 dead link → 提交新 IndexNow push

```bash
# 1. 跑（每周一次）
linkinator https://mfs.xx.kg \
  --skip "^https://mfs.xx.kg/wp-" \
  --skip "^mailto:" \
  --skip "^tel:" \
  --format json \
  --output mfs-broken-links-$(date +%F).json

# 2. 结果丢 changelog
cat > changelog/$(date +%F)-broken-links.md << EOF
# mfs 周度死链审计 $(date +%F)
（自动跑 linkinator 产物，0 broken = 通过）
EOF
```

## 配置跳过模式（关键）

mfs 跳过理由：
- `/wp-` 路径 → WAF 假绿，绝对跳过
- `/cdn-cgi/` → Cloudflare 服务路径
- `/feed/` → RSS 故意保留
- `?s=*` → WP 搜索路径（带 hash 的）

## 输出格式

- `format=JSON` → 结构化数据（CI 集成）
- `format=CSV` → 表格（Excel 友好）
- `format=pretty` → 命令行友好（默认）

## mfs 真实预测

- 第一次跑：约 5-30 个 broken link（参考 hello-biz 内大量 `#` 占位 + 老的 indexnow_key text）
- 修完后：每周稳定 0-3 个
- 完整接入：1 小时配置 + 永久收益
