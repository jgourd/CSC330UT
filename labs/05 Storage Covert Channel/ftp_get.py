# FTP Directory Listing
# Author: Dr. Jean Gourd
# Shows how to use Python to connect to an FTP server and list directory contents.
# Set the variables below as appropriate.

from ftplib import FTP

# FTP server details
IP = "localhost"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = ""
USE_PASSIVE = True # set to False if the connection times out

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

# sort the files by filename, ignoring case
#files = sorted(files, key=lambda x: x[56].lower())

# display the folder contents
for f in files:
	print(f)
