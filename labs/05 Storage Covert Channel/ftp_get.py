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
# different FTP file/folder (directory) listing methods:
# method 1 uses ftp.dir which only shows visible items (i.e., items that aren't hidden -- which begin with '.' on Linux systems)
# method 2 uses ftrp.retrlines which can optionally show hidden files (including the current and parent directories); however, this method requires more work to remove unnecessary items
# I recommend using method 2 to look around an FTP server to help determine where relevant items might be located, then switch to method 1 to actually fetch the items for decoding the covert message
LIST_METHOD = 1

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
# listing files method #1
if (LIST_METHOD == 1):
    ftp.dir(files.append)
elif (LIST_METHOD == 2):
    # use "LIST -a" to also include hidden items
    ftp.retrlines("LIST", files.append)
# exit the FTP server
ftp.quit()

# sort the files by filename, ignoring case
# use this if the listing retrieved from the FTP server isn't ordered/sorted properly
#files = sorted(files, key=lambda x: x[56:].lower())

# display the folder contents
for f in files:
    print(f)

