import json
import subprocess
from colorama import Fore, init
import os

init(autoreset=True)

def load_app_data():
    base_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_path, "apps.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def install_app(nickname):
    apps = load_app_data()
    app_id = apps.get(nickname.lower())

    if not app_id:
        print(Fore.RED + f"❌ Unknown app: {nickname}")
        return

    print(Fore.LIGHTYELLOW_EX + f"📦 Downloading started: {nickname} ({app_id})")

    try:
        process = subprocess.Popen(
            ["winget", "install", "--id", app_id, "--silent", "--accept-package-agreements", "--accept-source-agreements"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        for line in process.stdout:
            print("🔄", line.strip())

        process.wait()
        if process.returncode == 0:
            print(Fore.LIGHTGREEN_EX + f"✅ {nickname} downloaded successfully!")
        else:
            print(Fore.RED + f"❌ Error {nickname} while downloading. (Error: {process.returncode})")
    except FileNotFoundError:
        print(Fore.RED + "❌ Not found.")

def uninstall_app(nickname):
    apps = load_app_data()
    app_id = apps.get(nickname.lower())

    if not app_id:
        print(Fore.RED + f"❌ Unknown app: {nickname}")
        return

    print(Fore.LIGHTYELLOW_EX + f"🧹 Deleting started: {nickname} ({app_id})")

    try:
        result = subprocess.run(
            ["winget", "uninstall", "--id", app_id, "--silent"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.returncode == 0:
            print(Fore.LIGHTGREEN_EX + f"✅ {nickname} deleted successfully!")
        else:
            print(Fore.RED + f"❌ Error {nickname} while deleting.")
    except FileNotFoundError:
        print(Fore.RED + "❌ Not found.")

def list_apps():
    subprocess.run(["winget", "list"])