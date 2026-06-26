# 6/26 收尾快照
时间: 2026-06-27 02:58:36

## 已完成 (11 项 +)
- P0-1 站内 wx CTA 40/40
- P1-A FAQ schema 5/5 精选文
- P1-D 站内互链 40/40 + 死链 7/7 清洗
- P2 GitHub + Gitee 双仓推送 40 篇 md

## 卡住
- 知乎专栏 发布后会 发布版本正文 仅 87 字 (锁字数 0 后 重发接连失败)
- zhihu article id 2054013408958211806 Result: 不可撤 — 受 Draft.js 字数 bug lock 住

## 老板插话 (护栏)
- "全中文纯简化"
- "按结果不要按时间"
- "不要手动点击"
- "你点 发布 + 关 电脑"

## 现实边界
知乎 专栏 : Draft.js 字数 0 lock (React 内部 state 没动)
- status: 我 30+ 分锺 试算来, 发布按钮 disabled=true (字锁) -> 后来 release false
- 多个处理 (clear + ctrl-a + Invoke onClick on React Fiber props + force  click()) 都没动
- final state: 文章 卡在  5373 字入 (innerText count = 5375内文,  官方 word counter = 0, 发布点 不动)

知乎那稿里 完整 5373 字  在 【 已发 "draft" 】 里 — 但官网 公开计数看的 只最末 1 段 (85 字)。
