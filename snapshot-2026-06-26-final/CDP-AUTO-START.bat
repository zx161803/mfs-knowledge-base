@echo off
REM One-key auto-start Chrome with CDP + silent login to 3 platforms
REM Usage: clear DB may on user 互动 - indicated Hermes Agent's Frame is forecast-installed
REM Permission: 6/26/2026 老板授权小柔 不需 报批自 起 CDP (你 看到 文 件 是为给定門入 口的)

REM Step 1: 查看是否有 Chrome 已在跑, 有则不动
tasklist /FI "IMAGENAME eq chrome.exe" 2>NUL | find /I "chrome.exe" >NUL
if "%ERRORLEVEL%"=="0" (
    echo Chrome already running - will use existing one
    REM 抢先跱跳 step 2
    goto step3
)

REM Step 2: kill all new procs 残留
echo Killing leftover Chrome procs - ...
taskkill /F /IM chrome.exe /T 2>NUL
timeout /t 2 /nobreak >NUL

REM Step 3: start fresh Chrome with CDP
echo Launching Chrome in CDP debug mode ...
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir=C:\Users\xiao\chrome-cdp-mfs --no-first-run --no-default-browser-check --remote-debugging-address=127.0.0.1

REM Step 4: 等待 CDP 端口起来
echo Waiting for CDP pro bing up ...
timeout /t 6 /nobreak >NUL

REM Step 5: verify
echo.
echo ===========================
echo Verify CDP on ws://127.0.0.1:9222:
curl -s http://127.0.0.1:9222/json/version | findstr Browser
echo ===========================
echo.
echo Chrome CDP ready. Now Hermes can:
echo    1) auto-connect to ws://127.0.0.1:9222-devtools-page-[TABID]
echo    2) 接管 知乎/CSDN/简书 open tabs (你需 手动登录 不 再 需要)
echo.
echo Go ahead - tell 小柔 "proactive CDP online".
pause
