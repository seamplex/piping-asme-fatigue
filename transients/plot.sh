#!/bin/bash

for i in pyxplot; do
 if [ -z "`which $i`" ]; then
  echo "error: $i not installed"
  exit 1
 fi
done

for i in transient*.ppl; do
  pyxplot ${i}
done
