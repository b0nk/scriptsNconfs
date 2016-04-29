for %%f in (*.mkv) do (
ffmpeg -i "%%f" -vf "select=gte(n\,28000)" -vframes 1 "%%~nf".bmp
)
optipng -strip all *.bmp