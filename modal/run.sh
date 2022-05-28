#!/bin/bash -ex

for i in m4 gmsh feenox; do
 if [ -z "$(which ${i})" ]; then
  echo "error: ${i} not installed"
  exit 1
 fi
done

if [ ! -e modal.msh ]; then
 gmsh -3 modal.geo
fi

if [ ! -e modes.dat ]; then
  feenox modal.fee | tee modes.dat
  m4 seismic_load.fee.m4 | feenox -
fi  
