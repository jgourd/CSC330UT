#!/bin/bash

docker run -it --rm --name lab02-jupyter -p 8888:8888 -v ~/Downloads/CSC330UT/labs/02\ Containers/docker-examples/jupyter/notebooks:/home/jovyan jupyter/minimal-notebook
