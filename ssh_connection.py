
import socket

# Default Timeout for making a network connection.
socket.setdefaulttimeout(2)

# Instantiate new variable from the socket class.
s =  socket.socket()

# Using the connect() method, we attempt to make a network connection to another IP Addr, using default SSH Port(22).
s.connect(("10.0.2.16", 22))

# recv() method reads the next 1024 bytes on the socket. The results are stored to variable 'ans' and printed. (i.e) -> print(ans)
ans = s.recv(1024)

# Checking which Version of SSH the Ip Addr is using and if the SSH Version is vulnerable.
if ("SSH-2.0-OpenSSH" in ans):
    print(" [+] SSH-2.0-OpenSSH Server is vulnereable")
else:
    print("OpenSSh Server not vulnerable")



