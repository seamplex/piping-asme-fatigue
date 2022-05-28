#!/bin/bash -ex

for i in m4 gmsh feenox; do
 if [ -z "`which $i`" ]; then
  echo "error: $i not installed"
  exit 1
 fi
done

n=$(ls ../transients | grep "pt-.*\\.dat" | wc -l)
if [ ${n} -eq 0 ]; then
  echo "transients not initialized"
  exit 1
fi

if [ ! -e ../thermal.msh ]; then
 cd ..; gmsh -3 thermal.geo; cd thermal
fi

# if [ ! -e thermal.msh ]; then 
#  ln -s ../thermal.msh
# fi


if [ -z "$1" ]; then
  transients=$(seq 1 ${n})
else
  transients=$1
fi


for i in ${transients}; do
  if [ ! -e temp-${i}.msh ]; then
    feenox thermal.fee ${i} | tee temp-${i}.dat
  fi
done
