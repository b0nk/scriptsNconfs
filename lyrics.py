from mutagen.id3 import ID3
import os


flist = [dirpath + "\\" + f for dirpath, dirnames, fnames in os.walk('.') for f in fnames]
files = []

lyric_format = u'''Artist: %s
Title: %s
Album: %s

%s
'''

for i in flist:
  if i[-3:] == "mp3":
    files.append(i)

for j in files:
  audio = ID3(j)
  artist = audio.getall("TPE1")[0]
  album = audio.getall("TALB")[0]
  title = audio.getall("TIT2")[0]
  for i in audio.getall("USLT"):
    lyrics = str(i)
    lyrics = lyrics.replace(u"\r", u"")
    filename = u"%s - %s.txt" % (artist, title)
    filename = filename.replace(u"?", u"_")

    f = open(filename, "w+")
    print("Writing to -> %s" % filename)
    f.write(lyric_format % (artist, title, album, lyrics))
    f.close()
print("done")
input()
