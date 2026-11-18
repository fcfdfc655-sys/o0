#!/data/data/com.termux/files/usr/bin/bash

echo -e "\033[94m==================================================\033[0m"
echo -e "\033[92m   [ NET-BREAKER INSTALLER - SETTING UP ENVIRONMENT ]\033[0m"
echo -e "\033[94m==================================================\033[0m"

echo -e "\033[93m[*] Updating packages & installing dependencies...\033[0m"
pkg update -y && pkg upgrade -y
pkg install python p7zip curl -y
pip install requests

WORK_DIR="$HOME/NetBreaker"
mkdir -p "$WORK_DIR"
cd "$WORK_DIR"

echo -e "\033[93m[*] Downloading Tool 1 (Encryption Engine)...\033[0m"
if [ ! -f encrypt.py ]; then
    # تم ربطها برابط المستودع الخاص بك
    curl -L https://raw.githubusercontent.com/fcfdfc655-sys/o0/main/main.py -o encrypt.py
fi

# أرسل لي رابط الأداة الثانية لكي أضيفه هنا مباشرة 👇
# if [ ! -f upload.py ]; then
#     curl -L [رابط_الأداة_الثانية_هنا] -o upload.py
# fi

echo -e "\033[92m"
echo "=================================================="
echo " ✅ تم تثبيت الأداة الأولى بنجاح!"
echo "=================================================="
echo -e "\033[0m"

