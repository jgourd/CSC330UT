#!/bin/bash

# clean all executables
for f in *.c; do
    fn=$(basename -- "$f")
    fe="${fn##*.}"
    fn="${fn%.*}"
    rm $fn
done
