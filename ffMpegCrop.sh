#!/bin/bash

SOURCE=/home/source/directory/
cd $SOURCE
FILE=$(find . -type f -print -quit)
BASE=${FILE%_*}
FULLSOURCE="${SOURCE}${BASE:2}_%d.tiff"
DEST=/mnt/DATA/OUTPUTFILE.mp4
start=1666
numFrames=22000
qFactor=15

### crop width:heigth:x_topleft:y_topleft
ffmpeg -start_number $start -i $FULLSOURCE -filter:v "crop=2610:2894:182:118" -vframes $numFrames -c:v libx264 -crf  $qFactor $DEST
