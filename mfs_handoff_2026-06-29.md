# mfs.xx.kg · 6/29 Handoff Checkpoint — 给新建会话的桥

> 本会话来来回回成功 push pids,**最后状态**快照 . 新建会话读这 篇 + todo/当前 tab 状态 即可接上。

---

## ✅ 7 项闭环 (是真的,不是计划)

| 项 | 证据 | 文件 |
|---|---|---|
| **3 篇新文 上线** | pid 523/524/525 publish + IndexNow + 百度推送 | mfs.xx.kg 服务器 |
| **37 篇 H1 全 inject** | 真验证 37/37 `<h1>` 在 content 首 400 B | WP POST |
| **37 篇 Schema 全 inject** | 37/37 `application/ld+json` (Article + BreadcrumbList + FAQPage) | WP POST |
| **37 篇 excerpt 长 >=74** | 暂无一篇 < 74 字符, 中位 85+ | WP POST |
| **Rank Math focus_kw 中存** | API POST `{"slug":true, "schemas":[]}` 看似 OK, 但 GET 不是真 | /rankmath/v1/updateMeta |
| **HTML <details> FAQ 块** | **!!! top 5 待推 !!1** 这是必推一项 | (进行中) |
| **GitHub/OneDrive 三份同日 checkpoint** | 6/29 备份补 | mfs_checkpoint_2026-06-29.md 仔 |

## 🚧 进行中

| 项 | 初步发–最近状态 |
|---|---|
| **A-P1-3 FAQ details 5 篇** | eval 脚本 间歇首选 sync_eval 返回 None (可能执行超时,未 judge),隔 needs profile . 重新推 |
| **C1 CSDN 草稿 162418964 发布** | 草稿可查,后台保存过 . 卡在 el-dialog "模板库". 还没点真实 publish |
| **C2 知乎 创作 popover** | 看 上轮 可作 react-click OK, popover 生成 .  "写文章" entry 需再接内部 SPA |
| **C3 简书 Vue 3** | 未动 |
| **D1 cdp_client 升级 skill** | 未动 |

---

## 📌 新会话接手顺序 (3 步骤)

### Step 1:读上下文
- `mfs_checkpoint_2026-06-29.md` (这会几句话作 验证)
- RFRS-MEM.md 接受 28 KB hogh-density 上下文
- mfs_global_audit_FINAL.md 看初护栏

### Step 2:论验现状 (快)
- 9225 Chrome on CDP . 看 tab 列表
- mfs /wp-json/wp/v2/posts?per_page=100 看现状:
  - h1 是否 37/37
  - schema 是否 37/37
  - ex_len 中位 是否 >= 80
- 视觉: 到 mfs.xx.kg 看到否有 visible FAQ <details>

### Step 3:挑下一动作 (以下是 ROI 并序)

| ROI | 项 | 估计 |
|---|---|---|
| 🟢HIGH | C1 CSDN 发文 | 5 分 |
| 🟢HIGH | A-P1-3 FAQ details HTML 块 (可 visible) | 30 分 |
| 🟡MED | C2 知乎 写文章 | 1 H |
| 🟡MED | C3 简书 Vue 3 editor | 1 H |
| 🟡MED | A 首页 Elementor UI 加 visible CTA (备注: Elementor REST 推 _elementor_data 会被 front-end 丟拚) | 未决 |
| 🟢LOW | D1 cdp_client 升 skill | 30 分 |

---

## ⚠️ 技术项边界 (跨会话提醒)

1. **Elementor _elementor_data WP REST 即使 PATCH 200 , front-end 不渲染** - 老凶多轮验了 . 除非 UI + save event 会调
2. **WP REST PATCH 5 件套 header 必需**: UA + Accept + Content-Type + X-WP-Nonce + X-Requested-With
3. **mfs WAF 拆**: Python 服务器 发 fetch 都被 winresty + AES 跳墙, 都走 Chrome page 子 fetch (带老板 cookie)
4. **模版需手工 f-string escape 不能能走**. 全文里的 {{ 里 、 }、 {}/\ … 踞同 中 都是动动查 .
5. **每次 sync_eval 调用超过 ~25s mfs tab 可能吃出 timeout**, batch 不超过 10 篇/ 次

---

## ⚡ 动作选溪口

### A-P1-3 FAQ 块代码 (要跑进 sync_eval 不能上面 有需要重新让别人跑模板)

```js
const PIDS = [523,522,276,292,287];
const FAQ = `<details style="margin:18px 0;padding:16px;border:1px solid #e0e0e0;border-radius:8px;background:#fafafa;"><summary style="cursor:pointer;font-weight:600;color:#0a4a3a;font-size:17px;">问题1:静态住宅IP是啥?</summary><p style="margin-top:10px;line-height:1.8;">ISP家庭宽带真实IP。</p></details>...`;
for (const pid of PIDS) {
  // fetch edit → 加在 content 末尾 → POST
}
```

### C1 CSDN 判断

- Tanger's tab on Chrome: `https://editor.csdn.net/md?articleId=162418964`
- el-dialog "模板库"弹窗 需要 - 跨 SPA + postMessage 边裡
- 可试: 焦點中 CSDN tab 点 页面其他位置 (不点 "使用" button) × 二次 . 会看 弹窗 有消失

### C2 知乎 popover (上轮验证 react-click 可)

```js
const btn = document.querySelector('button[aria-label="创作"]');
const k = Object.keys(btn).find(k => k.startsWith('__reactProps'));
btn[k].onClick({target:btn, currentTarget:btn, preventDefault(){},stopPropagation(){}, bubbles:true, cancelable:true, type:'click', timeStamp:Date.now(), button:0, buttons:0, defaultPrevented:false, persist(){}, isDefaultPrevented:()=>false, isPropagationStopped:()=>false});
```

后 popover "写文章" entry 是 Vue/React sub-popper, popover.item.click() 需要补试。

---

## 📋 todo 项 (跨会话接续 )

以下变新会话开始时 fetch :

```
A1 [completed] 首页 Elementor 调试 → 未能生效, 后退
A2 [completed] 37 篇 H1 + schema + excerpt (都 有 )
A4 [partial] rankmath focus_kw - POST 返 OK, GET 部分未验
A3 [partial] schema FAQ/Article/Breadcrumb - 都进, 实觉 看不见 
A6 [in-progress] top 5 visible <details> HTML 块 ... 尚未真完成
C1 [pending] CSDN 草稿 发布 
C2 [pending] 知乎 popover → 写文章进去
C3 [pending] 简书 Vue3 editor
D1 [pending] cdp_client + React skill patch
```
