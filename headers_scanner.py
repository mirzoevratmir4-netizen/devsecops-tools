import requests 

url = input("Введите URL (Например https://example.com)")

try:
    response = requests.get(url, timeout=5)
except Exception as e:
    print(f"ошибка: {e}")
    exit()

security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy", 
]

print(f"\nПроверка {url}\n")
                    
for header in security_headers:
    if header in response.headers:
        print(f"[+] {header}: {response.headers[header]}")
    else:
        print(f"[-] {header}: ОТСУТСТВУЕТ")

print(f"\nВсего заголовков на сайте: {len(response.headers)}")
    