#!/bin/bash

docker run -d --rm --name lab02-apache -p 80:80 -v ~/Downloads/CSC330UT/labs/02\ Containers/docker-examples/apache/html:/var/www/html php:7.2-apache
