@echo off
for /D %%d in (*.*) do title Compressing %%d... & start /B /LOW /WAIT 7z a -mx9 -t7z "%%d.cb7" "%%d"
pause