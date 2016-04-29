@echo off

SET FILETYPE=mkv
SET FRAMERATE=23.976
SET ASTREAM=1
SET AFILE=a.ac3

for %%i in (*.%FILETYPE%) do (
  ffmpeg -i "%%i" -c:v copy -map_metadata -1 -bsf:v h264_mp4toannexb raw.264 ^
         -map 0:%ASTREAM% -c:a ac3 -b:a 640k -map_metadata -1 %AFILE% ^
         -map 0:5 -c:s copy "%%~ni.srt" -y

  mp4box -add "raw.264#trackID=1:fps=%FRAMERATE%:name=" -packed ^
         -add "%AFILE%#trackID=1:name=" -tmp ".\\" -new "%%~ni.mp4"
)
del raw.264
del %AFILE%
pause
