# MFS 项目 2026-06-27 完整进度报告

## 方案 B 已执行路径: Bing IndexNow + 国际 SEO

### 1. 站点状态盘点(百度资源后台)
- 索引量: 6/27 当前 = 0; 6/16 = 0; 6/03 = 1; 6 月初 = 1
- PC + 移动搜索点击量 = 0; 展现量 = 0
- 排名词 = 暂无数据
- 抓取异常 = 暂无数据
- 站点备案号: 未填写(xx.kg 二级域 = 无法 ICP 备)

### 2. 关键发现
- 老板原话: 之前网站换过空间 从那以后就没爬虫了 - IP/物理机换后 Baiduspider 停抓
- bingbot 能进 62696B 通过,IF openresty WAF 不挡爬虫, 只挡浏览器裸 GET
- 物理 robots.txt 已存在 + Accept: /

### 3. 重复清理 (执行)
WP REST DELETE 通:
- 删 6 篇重复: pid 294/295/296/298/301/302
- 删 1 篇前遗: pid 297
- 保留 5 篇: pid 305/304/303/300/299
- WP 总文章: 40 → 33

### 4. 双仓同步 (执行)
GitHub + Gitee mfs-knowledge-base commit f6f6498 + 4a10d14 push 完成

### 5. zhihu 专栏活动
- 删 pid 287 (2026-06-26 凌晨 1:57 不全版)
- 新发 pid 2054234802279167219 - 2026 跨境 IP 选型指南 SOP (1676 字)

### 6. 推送任务
- 百度主动推送 over quota 6/27 满, 6/28 重置
- IndexNow: HTTP 202 接收 34 URL

### 7. 技术突破
- chrome + CDP WS 直接接管浏览器: launch_app --remote-debugging-port=9222
- WP REST GET X-WP-Nonce + cookie auth + force=true DELETE
- mcp_cua_driver_bring_to_front 解决 OS foreground-lock

### 8. P0 / P1 / P2 待办
- P0 等老板 MSA (Microsoft 账号) 才能登 bing.com/webmasters
- P1 6/28 复查 Bing IndexNow 收录
- P1 让老板手动百度资源平台提交 sitemap
- P2 微信 CTA + 中文平台分发 (zhihu/CSDN/简书)
