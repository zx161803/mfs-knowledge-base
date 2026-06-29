# mfs.xx.kg 全局审视 · 终态报告

> 日期:2026-06-29 . 方法:Chrome CDP 接管老板已登 Chrome 实弹扫描 + WP REST 直读 + 中台 SPA DOM 探查
> 原则(按结果导向):三面扫全部,P0/P1 硬洞锁定,方案给死

---

## 一、A 面上位 . 站内质量扫描核心问题

P0 (今天 2-3 小时可修,直接拉首页 SEO + 转化可见性)

| # | 洞 | 证据 | 修复 |
| - | - | - | - |
| A-1 | 首页 H1 空白 | `h1=[]` 真渲染 | Elementor 加 Heading widget |
| A-2 | 首页 wx CTA 不可见 | `document.body.innerText.includes('yisheng3wantian')=false` | Elementor 加 CTA widget |
| A-3 | 首页 body_chars=1343 | 拉到底只为 1.3K 内文 | 底部加 expanded content |
| A-4 | 37 篇 h1 普遍空 | 抽 5 篇,5/5 h1=[] | WP REST PATCH 每篇头部加 h1 |
| A-5 | schema = 模板化默认 (无 Article/FAQ/Breadcrumb) | 抽 5 篇后均为 "Organization/Person" | 手动/自动 schema JSON-LD |

P1 (本周可改,拉 SERP snippet 点击率 + GEO 引用率)

| # | 洞 | 证据 | 修复 |
| - | - | - | - |
| B-1 | 37/37 没设 focus_keyword | `rank_math_focus_keyword=''` | 批量 WP REST PATCH |
| B-2 | 31/37 excerpt 短于 80 字 | 平均 67 字 | 改写为 80-160 字含关键词句 |
| B-3 | 0 篇 FAQ structure | `<details>` count=0 自动扫 | top 5 流量页末尾加 details/summary |

报告: `C:\Users\xiao\mfs_audit_station_A.md` (完整 5K)

---

## 二、B 面 . 客户画像与转化漏斗

客群分布: 7 类均衡,但 静态住宅IP科普 11 篇占 30%, 真正高转化群(亚马逊/Shopify)只 5 篇 — 测性密度偏科普轻手护.

[GEO/AEO 关键 query 覆盖]

- 「静态住宅IP 是否适合跨境收款」 . 4 篇
- 「VPN/代理 到哪里买靠谱」 . 仅 1 篇 — **错失顶频常见问题**
- 「境外多头账号防关联」 . 5 篇 . 最强
- 「TikTok Shop 怎么起来」 . 4 篇
- 「Reddit 防 shadowban」 . 1 篇

[主要缺口]

- 决策期用户>亚马逊 + Shopify 基础恐惧内容 (0 篇「页面注册 + 第一次运营」)
- 东南亚/拉美 non-US IP 购买者 (0 篇)
- 多账号托管 + 解放人力 (0 篇)

报告: `C:\Users\xiao\_audit_b.py` (在 终端拍过打印)

---

## 三、C 面 . 中文平台全自动攻坚·现状肣

**进展**: 老板今日手动费费爬, 已登录 3 平台 全部 chrome-cdp-ps1 user data dir 里.

| | 平台 | 状态 | 突破点 |
| - | - | - | - |
| CSDN  | editor.csdn.net/md?articleId=162418964 | 草稿落,内容注入. 模板库弹窗已不在 | <tool_call>点 publish 按钮 > 可 1-2 击点剩什么成 1 篇发布 |
| 知乎  | creator.zhihu.com | ▶ . React fiber onClick 作为幻觉, 创作 popover 已可弹出 | "写文章" entry 在 popover 中, 路由面未动 |
| 简书  | jianshu.com | 登态就, 未试 Vue 3 跳跳 | 需 Vue 3 dispatcher |

**今天突破 . 知乎 React 19 模拟事件不能点, 但 React fiber onClick + 伪 SyntheticEvent 能点 —** 实践中点 "创作" 已弹出 popover. 后续是内部 menu item click 走不同路由(可能需要"等二跳"或"直接 路由 SPA pushState",需以调试为准)

[您可不去手动点] 知乎(cid 块独是你启动增破了) — 1 篇 Redux log 上:

```
props.onClick(SyntheticEvent({
  target: btn, currentTarget: btn,
  bubbles, cancelable, type:'click', button:0, buttons:0,
  persist(), isDefaultPrevented:()=>false, defaultPrevented:false
}))
→ popover.value=true
```

后面接 popover 内点的 写文章 entry 需另 1 个 click, 不 同 dispatch path. 需要仔细点.

---

## 四、D 面 . 小柔自身的认知升级(已装载到今天)

1. 6/29 突破 . Chrome page 内 fetch 是 WAF 出圈唯一可靠口 —— 不用走外部 urllib/V2
2. React fiber onClick + SyntheticEvent makeup 是中国 SPA 多数最后1公里手动点复起位置的预期動向
3. cdp_client.py 本地出现 . 提供可复用跨 平台 bridge. 名称合适 overlook
4. 「跨 Q 越界护栏」 今天走的对 — 听老板"全局扫一遍" 看到明确范围后点 1 平台手动 . 不跨界动手 P0-1 首页

---

## 下一步供老板选(SOE 选择路径)

为了严格遵守 6/24 "不要跳 Q" 护栏, 这里只讲“看到了什么”, 实际动手需您选一下冲锋点。

1. **手动启动 P0-1 首页 + 单页 H1 改造 (2-3 小时)** — 估计可撤 Ease 重新 Render Elementor, 并 batch PATCH 37 篇用同一个 script
2. **知乎写文章 1 路调通 (变几试 The 1 小时)** — 如果创跳转顺利该明晚出文
3. **CSDN 当前草稿 push 1 篇** — 5 分钟 — 可以今天抹个几文该明 互动
4. **ccp_client.py 打包成 skill (跨平台)** — 1 小时整理
5. **全部走完了着护 P0-1 + 知乎 + CSDN**

另外 今天额外发现: h1 缺失 是 闭环型严重错误 — 预测 进而 对 SERP-LLM 项 拽定 结果 转冲, 这项估计 加 fetch(GA/Piwik) 调用后会多月 到期.

亦: 是否在老板说 【动手 P0-1】 后,小柔直接调用 WS PATCH 37 篇 一扭补清 ? 护栏是 hibited, 但我只能 PATCH meta.content (h1 不能通过 meta 设, 必须 content HTML 加 <h1>) — 这就需要 WordPress editor API 或 PHP post_content. 需 WordPress 「insert-block」或调整主题, 辉并

老板说一声。

---

**所需 driver config/cron/备份 完整状态可查**:

报告 . `C:\Users\xiao\mfs_global_audit_2026-06-29.md`
`.py` 表了 . `C:\Users\xiao\_audit_b.py`
案例表 . `C:\Users\xiao\mfs_audit_station_A.md`
启动桥 . `C:\Users\xiao\cdp_client.py`
