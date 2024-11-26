#!/bin/bash

# FTP Covert Channel (10-bit mode script)
# Author: Dr. Jean Gourd
# Takes a message and encodes it using the 10-bit mode as discussed in class.
# Use this to create messages so that you can test your FTP code.
# Set the variables below as appropriate.

# VARIABLES
# the folder to create files in
DIR=/srv/ftp/10
# the file that contains the message to encode
MESSAGE_FILE=message-10.txt
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

# get the number of bits required to encode the message
n=$((${#msg} * 7))
while ((n % 10 != 0)); do
    ((n++))
done
# get the number of files required to encode the message
((n /= 10))

# generate the random files
files=()
for ((i=0; i<n; i++)); do
    files+=(`echo $RANDOM | md5sum | cut -c -$(($RANDOM % ($MAX_FILE_LEN - $MIN_FILE_LEN) + $MIN_FILE_LEN))`)
done
# sort the files
sorted_files=($(printf '%s\n' "${files[@]}" | sort))

# clear the FTP directory
rm -rf "$DIR"/*
# generate the binary encoding of the message
bin=
for ((i=0; i<${#msg}; i++)); do
    l=${msg:$i:1}				# the current letter
    n=`echo "$l" | xxd -u -p | cut -c -2`	# the hex (ASCII) value of the current letter
    b=`echo "obase=2; ibase=16; $n" | bc`	# the binary value of the current letter

    # prepend 0s to set the number to 7 digits
    while ((${#b} < 7)); do
        b=0$b
    done
    bin="$bin$b"
done

# append 0s to set the entire messages length to be a multiple of 10
while ((${#bin} % 10 != 0)); do
    bin="$bin"0
done

# generate the permissions
i=0	# current bit position
n=0	# current file
p=	# current permissions
while ((i < ${#bin})); do
    # we're at the end of 10 bits
    if ((i % 10 == 0)); then
        # but not at the beginning
        if ((i > 0)); then
            # get the current file/directory
            f=${sorted_files[$n]}
            # if a directory, create it
            if ((d == 1)); then
                mkdir "$DIR"/$f
            # if a file, create it
            else
                touch "$DIR"/$f
            fi
            # set its permissions
            chmod $p "$DIR"/$f
            # reset the permissions and go to the next file
            p=
            ((n++))
        fi
        # get the file/directory bit and go to the next bit
        d=${bin:$i:1}
        ((i++))
    # we're still processing bits for a file
    else
        # grab the next 3 bits and convert them to decimal
        pn=${bin:$i:3}
        pn=`echo "obase=10; ibase=2; $pn" | bc`
        # update the permissions and go to the next 3 bits
        p=$p$pn
        ((i += 3))
    fi
done
# handle the final 10 bits
f=${sorted_files[$n]}
if ((d == 1)); then
    mkdir "$DIR"/$f
else
    touch "$DIR"/$f
fi
chmod $p "$DIR"/$f
