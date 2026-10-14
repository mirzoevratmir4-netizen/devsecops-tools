import socket
import sys

if len(sys.argv) < 3:
    print("Использование: python Scanner.py <IP> <порты>")
    print("Пример: python Scanner.py 8.8.8.8 22,80,443")
    sys.exit(1)

target = sys.argv[1]
ports_input = sys.argv[2]

ports = []
for p in ports_input.split(","):
    ports.append(int(p.strip()))

print(f"Сканирую {target}...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] порт {port} ОТКРЫТ")
    else:
        print(f"[-] порт {port} закрыт")
    
    sock.close()