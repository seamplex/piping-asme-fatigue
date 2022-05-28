n_scls=$(echo n_scls | m4 ../scls.m4 -)
scls=$(seq 1 ${n_scls})

for scl in ${scls}; do
  rm -f transient-sep.dat
  sort -g -k1 -k2 results/scl-*-${scl}.dat | awk -f concat.awk > results/concat-scl${scl}.dat
done
pyxplot secondary.ppl
