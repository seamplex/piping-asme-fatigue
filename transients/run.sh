#!/bin/bash

for i in m4 awk; do
 if [ -z "$(which $i)" ]; then
  echo "error: $i not installed"
  exit 1
 fi
done

rm -f pt.dat
cd def
i=0
for txt in $(ls *.txt); do
  name=$(basename $txt .txt)
  n=`head -n1 $txt | cut -d '(' -f2 | cut -d ')' -f1 | awk '{print $1}'`
  i=$((${i} + 1))
  echo 
  echo ${i} ${name}
  echo ${n} > ../n-${i}.dat
  grep -v '#' $txt | awk 'BEGIN{t=0}{t +=$ 3; print t, $2, $1;}' | tee  ../pt-${i}.dat
  m4 -Dxxx=${i} -Dt1=${t1} -Dt2=${t} -Ddt=${dt} ../transients.ppl.m4 > ../transient${i}.ppl

  # global
  awk -vt0=$t0 '{$1 += t0; print $0}' ../pt-${i}.dat >> ../pt.dat
  t0=`tail -n1 ../pt.dat | awk '{print $1}'`

done
cd ..
