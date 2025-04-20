import os
from colorama import Fore, init

init(autoreset=True)

def get_drives():
    return [f"{chr(drive)}:\\" for drive in range(65, 91) if os.path.exists(f"{chr(drive)}:\\")]

def whereis(filename):
    drives = get_drives()
    for drive in drives:
        for root, dirs, files in os.walk(drive):  # Az összes meghajtót végigjárja
            if filename in files:
                print(Fore.GREEN + f"Found: {os.path.join(root, filename)}")
                return
    print(Fore.RED + "File not found.")