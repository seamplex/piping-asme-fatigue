#!/bin/bash -ex

for i in transients thermal primary modal secondary fatigue; do
  echo $i
  cd $i
  ./run.sh
  if [ ! -z "$1" ]; then
    ./plot.sh
  fi  
  cd ..
done

