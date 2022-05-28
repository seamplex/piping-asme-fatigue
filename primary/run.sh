#!/bin/bash -e

for i in m4 gmsh feenox awk sort head; do
 if [ -z "$(which ${i})" ]; then
  echo "error: ${i} not installed"
  exit 1
 fi
done


if [ ! -e ../mech.msh ]; then
 cd ..; gmsh -3 mech.geo; cd primary
fi

m4 scls.vtk.m4 > scls.vtk
m4 scl-linearize-primary.fee.m4 > scl-linearize-primary.fee

maxp=$(awk '{print $3}' ../transients/pt-*.dat | sort -gr | head -n1)

if [ ! -e primary.txt ]; then
  feenox primary.fee ${maxp} | tee primary.txt
fi
