#!/bin/sh

FILETYPE=mkv
ASTREAM=1
SSTREAM=0
AFILE=0a.ac3
VFILE=0v.264
VSETTINGS="-c:v copy -map_metadata -1 -bsf:v h264_mp4toannexb"

rm ./*_isotmp 2>/dev/null ;

for i in *.$FILETYPE ; do
  FRAMERATE=$(mediainfo --Output=Video\;%FrameRate% "$i");
  ACODEC=$(mediainfo --Output=Audio\;%Format%\\n "$i" | sed -n "$ASTREAM"p);
  FILENAME=$(basename "$i" .$FILETYPE);

  ASETTINGS="-map 0:$ASTREAM -c:a copy -map_metadata -1"

  if [ "$ACODEC" = "AAC" ] ;
  then
    AFILE=0a.aac
  elif [ "$ACODEC" != "AC-3" ] ;
  then
    ASETTINGS="-map 0:$ASTREAM -c:a ac3 -b:a 640k -map_metadata -1"
  fi

  if [ $SSTREAM -ne 0 ] ;
  then
    SUBS="-map 0:$SSTREAM -c:s copy $FILENAME.srt"
  fi

  ffmpeg -i "$i" $VSETTINGS $VFILE $ASETTINGS $AFILE $SUBS -y -hide_banner ;
  rc=$?

  if [ $rc -eq 0 ] ;
  then
    MP4Box -add "$VFILE#trackID=1:fps=$FRAMERATE:name=" -packed \
           -add "$AFILE#trackID=1:name=" -tmp . -new "$FILENAME.mp4" ;
    rc=$?
  fi
done

if [ $rc -eq 0 ] ;
then
  rm $VFILE 2>/dev/null ;
  rm $AFILE 2>/dev/null ;
fi
