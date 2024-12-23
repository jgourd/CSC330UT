#!/bin/bash

# clean all executables
for f in *.c; do
    fn=$(basename -- "$f")
    fe="${fn##*.}"
    fn="${fn%.*}"

    if [ -f "$fn" ]; then
        rm $fn
    fi
done
