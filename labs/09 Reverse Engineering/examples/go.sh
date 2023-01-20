#!/bin/bash

# compile all examples
for f in *.c; do
    fn=$(basename -- "$f")
    fe="${fn##*.}"
    fn="${fn%.*}"
    gcc -o $fn $fn.$fe -lssl -lcrypto
done
