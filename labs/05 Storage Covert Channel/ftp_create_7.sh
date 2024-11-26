#!/bin/bash

# FTP Covert Channel (7-bit mode script)
# Author: Dr. Jean Gourd
# Takes a message and encodes it using the 7-bit mode as discussed in class.
# Use this to create messages so that you can test your FTP code.
# Set the variables below as appropriate.

# VARIABLES
# the folder to create files in
DIR=/srv/ftp/7
# the file that contains the message to encode
MESSAGE_FILE=message-7.txt
# the minimum and maximum length of filenames created
MIN_FILE_LEN=3
MAX_FILE_LEN=32

#############################
# DO NOT EDIT BELOW THIS LINE
#############################

# create the directory if it doesn't exist
if [ ! -d "$DIR" ]; then
	mkdir -p "$DIR"
fi

# set the message
msg=`cat $MESSAGE_FILE`
echo "$msg"

# generate one random file for each letter in the message
files=()
for ((i=0; i<${#msg}; i++)); do
    files+=(`echo $RANDOM | md5sum | cut -c -$(($RANDOM % ($MAX_FILE_LEN - $MIN_FILE_LEN) + $MIN_FILE_LEN))`)
done
# sort the files
sorted_files=($(printf '%s\n' "${files[@]}" | sort))

# clear the FTP directory
rm -rf "$DIR"/*
# set the permission of each file appropriately
for ((i=0; i<${#msg}; i++)); do
    f=${sorted_files[$i]}			# the current file
    l=${msg:$i:1}				# the current letter
    n=`echo "$l" | xxd -u -p | cut -c -2`	# the hex (ASCII) value of the current letter
    b=`echo "obase=2; ibase=16; $n" | bc`	# the binary value of the current letter

    # prepend 0s to set the number to 9 digits (for permissions)
    while ((${#b} < 9)); do
        b=0$b
    done
    # set the decimal representation of the permissions
    p=
    for ((j=1; j<=3; j++)); do
        pn=`echo $b | cut -c $((j * 3 - 2))-$((j * 3))`
        pn=`echo "obase=10; ibase=2; $pn" | bc`
        p=$p$pn
    done

    # create the file and set its permissions
    touch "$DIR"/$f
    chmod $p "$DIR"/$f
done

# generate a few noise files (where one or more of the first three bits of the permission are set)
for ((i=0; i<$((${#files[@]} / 4)); i++)); do
    f=`echo $RANDOM | md5sum | cut -c -$(($RANDOM % ($MAX_FILE_LEN - $MIN_FILE_LEN) + $MIN_FILE_LEN))`
    p=
    for ((j=0; j<3; j++)); do
        if ((j == 0)); then
            pn=$(($RANDOM % (8 - 2) + 2))
        else
            pn=$(($RANDOM % 8))
        fi
        p=$p$pn
    done
    touch "$DIR"/$f
    chmod $p "$DIR"/$f
done
