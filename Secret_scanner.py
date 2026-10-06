import os
import re

patterns = {
    "API Key": r"(?i)api[_-]?key\s*[:=]\s*['\"]?([a-zA-Z0-9]{16,})",
    "Password": r"(?i)password\s*[:=]\s*['\"]?([^\s'\"]{6,})",
    "Token": r"(?i)token\s*[:=]\s*['\"]?([a-zA-Z0-9_\-]{16,})",
    "AWS Key": r"AKIA[0-9A-Z]{16}",
    "Private Key": r"-----BEGIN (RSA|DSA|EC) PRIVATE KEY-----",
}

def scan_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line_num, line in enumerate(f, 1):
                for name, pattern in patterns.items():
                    if re.search(pattern, line):
                        print(f"[!] {name} в {filepath}:{line_num}")
                        print(f"    {line.strip()[:80]}")
    except Exception as e:
        pass

def scan_folder(folder):
    print(f"Сканирую {folder}...\n")
    found = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith((".py", ".txt", ".json", ".yaml", ".yml", ".env", ".cfg", ".ini")):
                scan_file(os.path.join(root, file))
                found += 1
    print(f"\nПроверено файлов: {found}")

folder = input("Введите путь к папке: ")
scan_folder(folder)