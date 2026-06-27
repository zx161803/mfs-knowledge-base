# D3D11 修复尝试闭环报告 — 2026-06-27

## TL;DR
**D3D11 fail 在小柔这台 HP Pavilion g4 上不可修**。HP 已 retire 这个 10+ 年的 model，强制安装 OEM Intel HD 3000 驱动与 Windows 10 19045 不兼容。现状：UIA 自动化全工作，截图类能力（vision_analyze / SOM overlay）仍 degraded。

## 当前硬件画像
- HP Pavilion g4 Notebook PC（PBVEN111Z07NRW）
- Intel HD Graphics 3000（VEN_8086&DEV_0116&SUBSYS_166E103C）
- 当前驱动 Intel 9.17.10.4459（2016-05-19 HP OEM 版，9年未升）
- Windows 10 Pro 22H2 19045
- 错误根因：HD 3000 物理上不支持 D3D11 Feature Level 11_0 → 0x887A0004 DXGI_ERROR_UNSUPPORTED

## 尝试过的路径（全失败）

### R1: HP SoftPaq sp59327.exe（2015-12 发布，143MB）
- 下载：成功（C:\Users\xiao\mfs_d3d11_repair\sp59327.exe，SHA256 0ecb05d7...fa5cb3）
- 静默安装（/s）：失败，InstallShield 弹 "此系统不符合安装该软件的最低要求"
- 失败根因：sp59327 SP2/Win8.1 时代的 InstallShield，不认 Win10 19045 的 WinSxS
- 对话框 已在 6/27 12:46:33 通过 cua-driver UIA Invoke 点击"关闭"按钮关掉，Setup.exe (pid 6948) + sp59327.exe (pid 6852) 已自动退出
- 系统未变更：未装任何驱动到设备栈

### R2: HP 官方驱动站 self-service API
- 访问 support.hp.com/us-en/drivers/selfservice/HP-Pavilion-g4-Notebook-PC-series/5145700/model
- 返回："There is no software or drivers available for your product."
- **HP 已 deprecate 这个 model 系列**（社区明示 "HP has retired support for the model series since it is more than 10 years old"）
- 结论：R2 路径不可行，**官方已不发新驱动**

### R3: web search 找匹配 sp xxxxx for Win10 19045 + g4 Intel HD 3000
- 找到 sp76608/sp76501-77000 范围 sp 不存在（404）
- 社区帖 h30434.www3.hp.com 提示不存在更新 SoftPaq
- 结论：已经没有匹配项

## 不应采用 / 跳过路径
- R4：pnputil /add-driver 强装 INF — 高风险，可能 boot fail，需要 Win PE 回滚
- R5：买现代显卡 / 退役这台旧机 — 老板明示不踩时间投资
- R6：直接装 Intel 零售驱动（不通过 OEM 子系统校验）— HP g4 166E 不接受非 HP 子系统的驱动，会黑屏
- R7：CUDA / WARP software renderer（cua-driver 不支持这个 flag）

## 当前做法
- ✅ 桌面自动化继续走 ax 模式（UIA-based）
- ❌ vision_analyze / 截屏能力暂不可用 — 只能读你贴的图
- ❌ SOM overlay (mode=som) 失效 — 没截屏 D3D11 fail 不会贴标签
- 关键工程项目：看截图类需求（设计稿校对、SERP 比对、AI 引擎 UI 截图、captcha 看图、远程调试截屏）出路：
  1) 老板自己截图贴过来
  2) 用 web_extract / curl 拿文本版转不靠视觉
  3) 改用 Browserbase 远程（云端 chromium 有硬件 D3D11，不受你这台机器 GPU 限制）

## 已落到本地证据
C:\Users\xiao\mfs_d3d11_repair\
  - sp59327.exe (143 MB，sha256 0ecb05d7...fa5cb3)
  - install_sp59327_silent.bat (A 模式静默脚本，验证 InstallShield 不接受静默)
  - install_log.txt (5min timeout 124 系统杀)

## 状态记忆点
- 内存里已加 D3D11 修复护栏 + 老板言语过重护栏
- cua-driver 健康：ax_capability: pass；screen_capture_capability: degraded (D3D11 物理不支持)
- 装机前后状态无变化
- 没装任何 driver，没破坏任何东西
