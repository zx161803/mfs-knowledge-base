# IndexNow（sources/posts 单篇）

## 协议
提出方：Microsoft + Yandex
引入时间：2021-10
现参与：Bing / Yandex / DuckDuckGo / Seznam / Apple（在收）

## 工作流程

```
1. 站长在 site root 放 Key file
   → <random32hex>.txt
   → body: <random32hex>
2. content 改后，POST URL 给 api.indexnow.org
3. 所有参与的引擎都爬这个 URL（24h 内）
```

## API 调用

```
POST https://api.indexnow.org/IndexNow
Content-Type: application/json; charset=utf-8

{
  "host": "mfs.xx.kg",
  "key": "mfs-static-residential-ip-key-2026",
  "keyLocation": "https://mfs.xx.kg/mfs-static-residential-ip-key-2026.txt",
  "urlList": [
    "https://mfs.xx.kg/article-1/",
    "https://mfs.xx.kg/article-2/"
  ]
}

→ HTTP 200: OK
→ HTTP 400: 格式错
→ HTTP 403: key 错
→ HTTP 422: URL 不属于 host
→ HTTP 429: 配额限制
```

## mfs.xx.kg 现状（7/4 实测）

- **Key file**: `https://mfs.xx.kg/mfs-static-residential-ip-key-2026.txt` ✅ 200
- **Key**: `mfs-static-residential-ip-key-2026`
- **IndexNow push**: 7/4 累计 100+ 次全部 HTTP 200
- **实际收到方**：Bing (Yandex/Seznam 在中国大陆不通)
- **效果**：bing.com 缓存 24h 内 100% 命中

## mfs 真实教训
- IndexNow 推送 **≠** Bing 收录
- 推送 = 主动告诉 Bing 去看
- 但 **信任度评估** 仍要靠其他手段
- 6/16 换空间后 mfs.bing.com 几乎 0 收录，IndexNow 1 个月没改变
- **结论**：IndexNow 是必要不充分条件

## 与 sitemap.xml 的关系
- sitemap.xml 给搜索引擎 **被动用**（爬虫发现新页）
- IndexNow 是 **主动通知**
- 两者互补，不是替代

## 推荐工具链
- `indexnowsubmit` npm — 自动提交
- python `indexnow` PyPI — 一键脚本
- WordPress 插件：`IndexNow Plugin` (Microsoft 官方)
