@echo off

set ffx_profile_appdata=%appdata%\Mozilla\Firefox\Profiles\06bjdzti.default-1457903950020\
set ffx_profile_local=%appdata%\..\Local\Mozilla\Firefox\Profiles\06bjdzti.default-1457903950020\
set fxp_home=.\FirefoxPortable\
set fxp_profile=%fxp_home%App\DefaultData\profile\
set fxp_plugins=%fxp_home%App\DefaultData\plugins\
set fxp_install=%fxp_home%App\Firefox\

set flash_xpi=https://addons.mozilla.org/firefox/downloads/file/519940/playflash_32bit-23.0.0.185-fx+sm-windows.xpi

title Installing Firefox Portable
start /WAIT FirefoxPortable.paf.exe

title Copying profile
xcopy /E /Y %ffx_profile_appdata%* %fxp_profile%
xcopy /E /Y %ffx_profile_local%* %fxp_profile%

title Removing unnecessary files and folders
rmdir /S /Q %fxp_profile%bookmarkbackups
rmdir /S /Q %fxp_profile%cache2
rmdir /S /Q %fxp_profile%crashes
rmdir /S /Q %fxp_profile%datareporting
rmdir /S /Q %fxp_profile%gmp-gmpopenh264
rmdir /S /Q %fxp_profile%gmp-eme-adobe
rmdir /S /Q %fxp_profile%gmp
rmdir /S /Q %fxp_profile%healthreport
rmdir /S /Q %fxp_profile%minidumps
rmdir /S /Q %fxp_profile%startupCache
rmdir /S /Q %fxp_profile%safebrowsing
rmdir /S /Q %fxp_profile%webapps
rmdir /S /Q %fxp_profile%anticontainer_plugins
rmdir /S /Q %fxp_profile%jumpListCache
rmdir /S /Q %fxp_profile%saved-telemetry-pings
rmdir /S /Q %fxp_profile%thumbnails
rmdir /S /Q %fxp_profile%HTTPSEverywhereUserRules
rmdir /S /Q %fxp_profile%storage
rmdir /S /Q %fxp_profile%OfflineCache
for /d %%i in ("%fxp_profile%extensions\https-everywhere-eff@eff.org\chrome\locale\*") do if /i not "%%~nxi"=="en" rmdir /S /Q "%%i"
for /d %%i in ("%fxp_profile%extensions\{b2e69492-2358-071a-7056-24ad0c3defb1}\chrome\locale\*") do if /i not "%%~nxi"=="en-US" rmdir /S /Q "%%i"

del /F /Q %fxp_profile%_CACHE_CLEAN_
del /F /Q %fxp_profile%cookies.sqlite
del /F /Q %fxp_profile%dta_queue.sqlite
del /F /Q %fxp_profile%enumerate_devices.txt
del /F /Q %fxp_profile%healthreport.sqlite
del /F /Q %fxp_profile%times.json
del /F /Q %fxp_profile%formhistory.sqlite

rmdir /S /Q %fxp_install%uninstall
rmdir /S /Q %fxp_install%gmp-clearkey

del /F /Q %fxp_install%crashreporter.exe
del /F /Q %fxp_install%crashreporter.ini
del /F /Q %fxp_install%maintenanceservice.exe
del /F /Q %fxp_install%maintenanceservice_installer.exe
del /F /Q %fxp_install%updater.exe
del /F /Q %fxp_install%updater.ini
del /F /Q %fxp_install%update-settings.ini
del /F /Q %fxp_install%webapp-uninstaller.exe

rmdir /S /Q %fxp_home%App\Firefox64

wget "%flash_xpi%" -O "%fxp_plugins%playflash_32bit-23.0.0.185-fx+sm-windows.xpi"

title Creating SFX package
start /B /LOW /WAIT 7z a -mx9 -mmt -y -sfx FirefoxPortable.exe %fxp_home%

title Cleaning up
rmdir /S /Q %fxp_home%

title DONE!
pause
