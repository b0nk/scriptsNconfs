#!/bin/sh

FILETYPE=mkv
DELETE=1
ASTREAM=$1
ASTREAMI=$1
SSTREAM=$2
AFILE=0a.ac3
VFILE=0v.264
ASETTINGS="-map 0:$ASTREAM -c:a copy -map_metadata -1"
VSETTINGS="-c:v copy -map_metadata -1 -bsf:v h264_mp4toannexb"

[ -z "$1" ] || [ "0" = "$1" ] && ASTREAMI=1 ;

for i in *."$FILETYPE" ; do
  VCODEC=$(mediainfo --Output=Video\;%Format% "$i");
  FRAMERATE=$(mediainfo --Output=Video\;%FrameRate% "$i");
  ACODEC=$(mediainfo --Output=Audio\;%Format%\\n "$i" | sed -n "$ASTREAMI"p);
  ABITRATE=$(mediainfo --Output=Audio\;%BitRate%\\n "$i" | sed -n "$ASTREAMI"p);
  FILENAME=$(basename "$i" .$FILETYPE);

  [ "$VCODEC" = "HEVC" ] && VSETTINGS="-c:v copy -map_metadata -1 -bsf:v hevc_mp4toannexb" && VFILE=0v.265

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

  [ -n "$SSTREAM" ] && SUBS="-map 0:$SSTREAM -c:s copy $FILENAME.srt"

  ffmpeg -i "$i" $VSETTINGS $VFILE $ASETTINGS $AFILE $SUBS -y -hide_banner ;
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
