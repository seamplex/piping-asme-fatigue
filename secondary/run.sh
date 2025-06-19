#!/bin/bash -ex

for i in m4 gmsh feenox awk sort head; do
 if [ -z "$(which ${i})" ]; then
  echo "error: ${i} not installed"
  exit 1
 fi
done


if [ -z "$1" ]; then
  n=$(ls ../transients | grep pt- | grep dat | wc -l)
  trans=$(seq 1 $n)
else
  trans=$1
fi

if [ -z "$2" ]; then
  dt0=10
else
  dt0=$1
fi

mkdir -p temp results
m4 scl-linearize-secondary.fee.m4 > scl-linearize-secondary.fee

if [ ! -e ../mech.msh ]; then
 cd ..
 gmsh -3 mech.geo
 cd secondary
fi

max_DT_tran=$(awk '{print $1, $2, ($3-$5)^2}' ../thermal/temp*.dat | sort -rgk3 | head -n1 | awk '{printf("%d", $1)}')
max_DT_time=$(awk '{print $1, $2, ($3-$5)^2}' ../thermal/temp*.dat | sort -rgk3 | head -n1 | awk '{printf("%d", $2)}')

seismic_tran=$(awk '{print $1}' seismic-time.dat)
seismic_time=$(awk '{print $2}' seismic-time.dat)
seismic_dt=$(awk '{print $3}' seismic-time.dat)

for i in ${trans}; do
 awk -vdt0=${dt0} -f choose-times.awk ../transients/pt-${i}.dat > times-${i}.dat
 echo $dt0 > mech_dt0.dat

 # make sure to pass through the maximum temperature difference point
 if [ ${i} -eq $max_DT_tran ]; then
   echo $max_DT_time >> times-${i}.dat
   sort -ug times-${i}.dat > tmp
   mv tmp times-${i}.dat
 fi

 # and through the times of the earthquake
 if [ ${i} -eq $seismic_tran ]; then
   echo $seismic_time >> times-${i}.dat
   echo $(($seismic_time+$seismic_dt)) >> times-${i}.dat
   echo $(($seismic_time+$seismic_dt+$seismic_dt)) >> times-${i}.dat
   sort -ug times-${i}.dat > tmp
   mv tmp times-${i}.dat
 fi
 awk -f tdt.awk times-${i}.dat > tdt-${i}.dat

 # do the work!
 if [ ! -e results/scl-${i}-1.dat ]; then
   feenox secondary.fee ${i}  | tee -a secondary.dat
 fi  
done
