#!/bin/bash

SOURCE_BASE=/source_directory/
DEST_BASE=/destination_directory/
cd $SOURCE_BASE

for SOURCE in M*/ ; do
  # echo $SOURCE
  cd $SOURCE
  # echo $PWD
  FILE=$(find . -type f -print -quit)
  BASE=${FILE%_*}
  FULLSOURCE="${SOURCE_BASE}${SOURCE}${BASE:2}_%05d.jpg"
  DEST="${DEST_BASE}movie${SOURCE:0:3}.mp4"
  echo $FULLSOURCE
  echo $DEST
  qFactor=15
  ffmpeg -start_number 1 -i $FULLSOURCE -filter:v fps=10 -c:v libx264 -crf  $qFactor $DEST
  cd $SOURCE_BASE
done
