
import socket

# Define function to return banner.

def retBanner(ip_addr, port_no):

    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip_addr, port_no))
        banner = s.recv(1024)
        return banner

    except:
        return


# Define function to Check Vulnerabilities in target server.

def checkVulns(banner):

    # FTP Servers
    if ("vsFTPd 2.3.4" in banner):
        print("[+] vsFTPD 2.3.4 FTP Server is vulnerable")
    elif("FreeFloat FTP Server" in banner):
        print("[+] FreeFloat FTP Server is vulnerable.")
    elif("Ability FTP Server" in banner):
        print("[+]  Ability FTP Server is vulnerable." )
    elif ("SSH-2.0-OpenSSH" in banner):
        print("[+] SSH-2.0-OpenSSH Server is vulnereable")
    else:
        print("\n[-]" + banner + " Server not vulnerable")

# Define ip-address(es) and port-number(s) -- for all target machines that we will connect to.

ip1 = "10.0.2.16"
port1 = 21       # FTP Server
port2 = 22       # SSH Server


def banners(banner):
    if banner:
        print('\n')
        print('[+]' + ' ' + ip1 + ' : ' + ' ' +  banner.strip('\n'))
        checkVulns(banner + '\n')


banner1 = retBanner(ip1, port1)
banner2 = retBanner(ip1, port2)


banners(banner1)
banners(banner2)


