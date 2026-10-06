import socket

target = input("Введите IP или домен: ")
ports_input = input("Введите порты через запятую (например 22,80,443): ")

ports = []
for p in ports_input.split(","):
    ports.append(int(p.strip()))

print(f"\nСканирую {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] порт {port} ОТКРЫТ")
    else:
        print(f"[-] порт {port} закрыт")
    
    sock.close()