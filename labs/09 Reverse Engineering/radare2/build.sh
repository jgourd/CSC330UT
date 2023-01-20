#!/bin/bash

cp ~/.bash_aliases .
docker build -t radare2 .
rm .bash_aliases
