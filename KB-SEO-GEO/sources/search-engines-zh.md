# 中文搜索引擎（sources/posts 单篇）

## 百度搜索资源平台

### 工具入口
- **普通收录**：API 提交 / 手动 / sitemap（每日配额 10w）
- **死链提交**：最多 50000 URL/文件，<10MB，识别 404
- **移动适配**：规则 / URL 对，校验 14 天
- **快速抓取**：被邀请才开通，48 小时可收录
- **站点属性**：站点 logo / 品牌展现 / 主体关联
- **站点子链**：搜索结果下方 6 个（限优质站）

### 主动推送 API
```
POST http://data.zz.baidu.com/urls?site=mfs.xx.kg&token=<your_token>
Content-Type: text/plain

URL1
URL2
...

→ {"remain":N,"success":M}
```

### 配额（mfs 现状）
- 7/4 实测：每日配额**已被平台调节**（5/10 → 2/10）
- 推送成功 = 入索引库 → 不等于被收录
- 还需 E-E-A-T + 内容质量 + 信任度

### sitemap 提交规则
- **不要**索引型 sitemap（指向另一个 sitemap）
- 推送 sitemap 文件 → 每日上限 20 条
- 已被废弃的字段：changefreq、priority

### 抓取频率（统计里看）
- 若短时间大量抓 → 适度降低（用 robots 之外的方式）
- 若几乎不抓 → 主动推送是手段之一，但**不解决信任度**
- **关键事实**：6/16 之后 mfs 0 索引的本质是换空间，**百度主动重审期间不会推全**

## Bing（MS 引擎）

### 索引量
- 用 Site：bings 查，site:mfs.xx.kg
- mfs 7/4 实测：**0**（与 Google 同步）
- Bing 的 "主动推送" 算正常（GSC 等价）

### IndexNow
- 所有新 URL 提交一次 → Bing + Yandex + DuckDuckGo + ... 
- 24h 自动同步
- Key file 必须放在 site root

## 搜狗

- 站长平台：https://www.sogou.com/docs/help/webmasters.htm
- 跟百度规则类似
- 中文搜索里流量比较小，权重低

## 360 搜索

- 站长：https://www.so.com/help/
- API 端点老旧，但仍可用
- 流量占比小，权重低

## 神马（移动搜索）

- shenma.sm.cn
- 移动搜索为主，PC 流量小

---

## ⚠️ mfs 真实教训（7/4 21:30）

老板原话："我之前换过空间，所以从那以后就没有爬虫了"
- **真问题**：不是工具问题，是**站点信任度问题**
- 换空间后所有引擎重估信信任，**trust reset**
- 6/16 起百度 0 索引 → 不补救就永远 L3
- **补救路径**（已映射到 `applied-to-mfs/`）：
  1. 申请百度站长平台 VIP 邀请（`优质内容` / `合规站点`）
  2. 大量推送历史 URL（每月跑一次 api push）
  3. 站外反向链接（知乎/CSDN/简书 footer 链接）
  4. 至少 3 个月才有效
  5. 期间不可拔 mfs 站点 → 一拔重置
