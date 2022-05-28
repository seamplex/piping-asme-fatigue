#!/bin/sh
# generate both a webm video out of png frames

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "usage: $0 basename fps"
  echo "finds files named basename.0000.png and builds a video named basename.avi"
  echo "with the prescribed number of frames per seconds"
  exit 0
fi

if [ "x$(which ffmpeg)" = "x" ]; then
  echo "error: ffmpeg not installed"
  exit 1
fi

# avconv -y -f image2 -framerate $2 -i $1.%04d.png -qmax 25 -vcodec libvpx $1.mp4 #-v quiet
ffmpeg -y -f image2 -framerate $2 -i $1.%04d.png $1.mp4 #-v quiet
