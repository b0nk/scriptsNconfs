@echo off
SET palette="palette.png"
SET filters="fps=25,scale=320:-1:flags=lanczos"

ffmpeg -v verbose -i %1 -vf "%filters%, palettegen" -y %palette%
ffmpeg -v verbose -i %1 -i %palette% -lavfi "%filters% [x]; [x][1:v] paletteuse" -y %2
del palette.png
