
import socket

socket.setdefaulttimeout(2)

s = socket.socket()

# Using the connect() method, we attempt to make a network connection to another IP Addr, using default FTP Port(21)
s.connect(("10.0.2.16", 21))

ans = s.recv(1024)

# Checking which Version of FTP the Ip Addr is using and if the FTP Version is vulnerable.

if ("vsFTPd 2.3.4" in ans):
    print(" [+] vsFTPD 2.3.4 FTP Server is vulnerable")
elif("FreeFloat FTP Server" in ans):
    print(" [+] FreeFloat FTP Server is vulnerable.")
elif("Ability FTP Server" in ans):
    print(" [+]  Ability FTP Server is vulnerable." )
else:
    print(" [-] FTP Server is not vulnerable.")




