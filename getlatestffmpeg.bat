@echo off
wget https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z -t 0 -c
title Extracting...
7z e ffmpeg-release-full.7z -y -o".\cont"
title Deleting archive...
del ffmpeg-release-full.7z
title Copying...
xcopy .\cont\*.exe .\ /R /Y
title Cleaning up...
rmdir /S /Q .\cont
title Done! ffmpeg
pause
