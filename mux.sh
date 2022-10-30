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
WORKINGDIR=$HOME/.tmp/vega-mux

[ -z "$1" ] || [ "0" = "$1" ] && ASTREAMI=1 ;

for i in *."$FILETYPE" ; do
  VCODEC=$(mediainfo --Output=Video\;%Format% "$i");
  FRAMERATE=$(mediainfo --Output=Video\;%FrameRate% "$i");
  ACODEC=$(mediainfo --Output=Audio\;%Format%\\n "$i" | sed -n "$ASTREAMI"p);
  ABITRATE=$(mediainfo --Output=Audio\;%BitRate%\\n "$i" | sed -n "$ASTREAMI"p);
  FILENAME=$(basename "$i" .$FILETYPE);
  RND=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 8); # 8 random chars
  AFILE=0a-$RND.ac3
  VFILE=0v-$RND.264

  [ "$VCODEC" = "HEVC" ] && VSETTINGS="-c:v copy -map_metadata -1 -bsf:v hevc_mp4toannexb" && VFILE=0v-$RND.265

  if [ "$ACODEC" = "AAC" ] ;
  then
    AFILE=0a-$RND.aac
  elif [ "$ACODEC" = "E-AC-3" ] ;
  then
    ASETTINGS="-map 0:$ASTREAM -c:a ac3 -b:a $ABITRATE -map_metadata -1"
  elif [ "$ACODEC" != "AC-3" ] ;
  then
    ASETTINGS="-map 0:$ASTREAM -c:a ac3 -b:a 640k -map_metadata -1"
  fi

  [ -n "$SSTREAM" ] && SUBS="-map 0:$SSTREAM -c:s copy $FILENAME.srt"

  ffmpeg -i $i $VSETTINGS "$WORKINGDIR"/$VFILE $ASETTINGS "$WORKINGDIR"/$AFILE $SUBS -y -hide_banner ;
  rc=$?

  [ $rc -ne 0 ] && echo ERROR on ffmpeg : "$i" && exit 1
  [ $DELETE -eq 1 ] && rm "$i" 2>/dev/null ;

  MP4Box -add "$WORKINGDIR/$VFILE#trackID=1:fps=$FRAMERATE:name=" -packed \
         -add "$WORKINGDIR/$AFILE#trackID=1:name=" -tmp "$WORKINGDIR" -new "$FILENAME.mp4" ;
  rc=$?

  [ $rc -eq 0 ] && rm "$WORKINGDIR"/$AFILE "$WORKINGDIR"/$VFILE 2>/dev/null
  [ $rc -ne 0 ] && echo ERROR on MP4Box : "$i" && exit 2

done

exit 0
