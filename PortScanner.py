import socket

def scan(targets, ports):
    print('\nStarting Scan For '+ str(targets))
    for port in range(1,ports):
        scan_port(targets,port)

def scan_port(ipaddress,port):
    try:  
        sock = socket.socket()
        sock.connect((ipaddress,port))
        print('[+] Port is Open '+ str(port))
        sock.close()
    except:
        pass

targets = input("[*] Enter Target To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Wants To Scan: "))

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_address in targets.split(','):
        scan(ip_address.strip(' '),ports)
else:
    scan(targets,ports)
