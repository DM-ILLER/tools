import socket
import termcolor

def scan(target, ports):
    print(termcolor.colored(f'\nStarting Scan For: {target}', 'blue'))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port Opened: {port}")
        sock.close()
    except:
        pass
    
targets = input("[*] Enter Targets To Scan(split the by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print(termcolor.colored('[*] Scanning Multiple Targets', 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    print("[*] Scanning One Target")
    scan(targets, ports) 