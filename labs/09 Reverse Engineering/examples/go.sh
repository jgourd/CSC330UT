#!/bin/bash

# compile specified example
if [ ! -z "$1" ]; then
    if [ ! -f "$1" ]; then
        echo "Error: $1 doesn't exist!"
        exit
    fi

    fn=$(basename -- "$1")
    fe="${fn##*.}"
    fn="${fn%.*}"
    gcc -o $fn $fn.$fe -lssl -lcrypto
# compile all examples
else
    for f in *.c; do
        fn=$(basename -- "$f")
        fe="${fn##*.}"
        fn="${fn%.*}"
        gcc -o $fn $fn.$fe -lssl -lcrypto
    done
fi
