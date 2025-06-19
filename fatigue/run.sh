#!/bin/bash

if [ -z "$1" ]; then
  n_scls=$(echo n_scls | m4 scls.m4 -)
  scls=$(seq 1 ${n_scls})
else
  scls=$1
fi

for scl in $scls; do
 echo SCL $scl
 sort -g -k1 -k2 ../secondary/results/scl-*-${scl}.dat | awk -f concat.awk > concat-scl${scl}.dat
 feenox nb3216.fee $scl | awk '{print NR-1,$0}' > input-${scl}.txt

 awk -f extrema.awk input-${scl}.txt > extrema-${scl}.dat
 awk -f all2all.awk extrema-${scl}.dat | sort -gr -k5 | awk -f cycles.awk > cycles-${scl}.dat
 
 echo n_scls | m4 scls.m4 - > n_scls.dat
 feenox cuf.fee $scl | tee cuf-${scl}.dat | awk -f format_cuf.awk > cuf-${scl}.tex
 awk '{cuf += $13} END { printf("%.03g\n", cuf) }' cuf-${scl}.dat | tee totalcuf-${scl}.dat
 
 cat concat-scl${scl}.dat | awk -f dump-discont.awk > disconts-${scl}.dat
 cat disconts-${scl}.dat | wc -l > n_disconts-${scl}.dat
 
 feenox fen-theler.fee ${scl} > fen-${scl}.dat
 feenox cufen-theler.fee ${scl} | tee cufen-${scl}.dat | awk -f format_cufen.awk > cufen-${scl}.tex
 awk '{cufen += $6} END { printf("%.03g\n", cufen) }' cufen-${scl}.dat | tee totalcufen-${scl}.dat
done

