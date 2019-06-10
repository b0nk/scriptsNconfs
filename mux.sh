#!/bin/sh

FILETYPE=mkv
DELETE=0
ASTREAM=1
SSTREAM=0
AFILE=0a.ac3
VFILE=0v.264
ASETTINGS="-map 0:$ASTREAM -c:a copy -map_metadata -1"
VSETTINGS="-c:v copy -map_metadata -1 -bsf:v h264_mp4toannexb"

for i in *."$FILETYPE" ; do
  VCODEC=$(mediainfo --Output=Video\;%Format% "$i");
  FRAMERATE=$(mediainfo --Output=Video\;%FrameRate% "$i");
  ACODEC=$(mediainfo --Output=Audio\;%Format%\\n "$i" | sed -n "$ASTREAM"p);
  ABITRATE=$(mediainfo --Output=Audio\;%BitRate%\\n "$i" | sed -n "$ASTREAM"p);
  FILENAME=$(basename "$i" .$FILETYPE);

  if [ "$VCODEC" = "HEVC" ] ;
  then
    VSETTINGS="-c:v copy -map_metadata -1 -bsf:v hevc_mp4toannexb"
    VFILE=0v.265
  fi

  if [ "$ACODEC" = "AAC" ] ;
  then
    AFILE=0a.aac
  elif [ "$ACODEC" = "E-AC-3" ] ;
  then
    ASETTINGS="-map 0:$ASTREAM -c:a ac3 -b:a $ABITRATE -map_metadata -1"
  elif [ "$ACODEC" != "AC-3" ] ;
  then
    ASETTINGS="-map 0:$ASTREAM -c:a ac3 -b:a 640k -map_metadata -1"
  fi

  if [ "$SSTREAM" -ne 0 ] ;
  then
    SUBS="-map 0:$SSTREAM -c:s copy $FILENAME.srt"
  fi

  ffmpeg -i "$i $VSETTINGS $VFILE $ASETTINGS $AFILE $SUBS" -y -hide_banner ;
  rc=$?

  if [ $rc -ne 0 ] ;
  then
    echo ERROR on ffmpeg : "$i" ;
    break
  elif [ $DELETE -eq 1 ] ;
  then
    rm "$i" 2>/dev/null ;
  fi

  MP4Box -add "$VFILE#trackID=1:fps=$FRAMERATE:name=" -packed \
         -add "$AFILE#trackID=1:name=" -tmp . -new "$FILENAME.mp4" ;
  rc=$?

  if [ $rc -ne 0 ] ;
  then
    echo ERROR on MP4Box : "$i" ;
    break
  else
    rm $VFILE $AFILE 2>/dev/null ;
  fi
done

rm ./*isotmp 2>/dev/null ;
