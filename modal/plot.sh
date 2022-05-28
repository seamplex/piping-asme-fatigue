#!/bin/bash

if [ !  -z "`which pyxplot`" ]; then
  pyxplot spectrum.ppl
  m4 n_modes.m4 modes.ppl | pyxplot
fi

if [[ !  -z "`which pvpython`" ]] && [[ !  -z "`which sed`" ]]; then
  for i in x y z; do
    sed s/ax/a${i}/ fig.py | pvpython
    convert -trim a${i}.png a${i}.png
  done
fi

