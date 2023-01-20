# Chat Client
# Author: Dr. Jean Gourd
# A sample chat covert channel client.
# Set the variables below as appropriate.

import socket
from sys import stdout
from time import time

# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "localhost"
port = 31337

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096).decode("utf-8")
while (data.rstrip("\n") != "EOF"):
    # output the data
    stdout.write(data)
    stdout.flush()
    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096).decode("utf-8")
    t1 = time()
    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)
    if (DEBUG):
        stdout.write(f" {delta}\n")
        stdout.flush()

# close the connection to the server
s.close()

