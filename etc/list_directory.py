import os
from colorama import Fore, init

init(autoreset=True)

def dir():
    try:
        contents = os.listdir(os.getcwd())
        if contents:
            for item in contents:
                if os.path.isdir(item):
                    print(Fore.LIGHTGREEN_EX + f"{item}/")  # Mappa
                else:
                    print(f"{item}")  # Fájl
        else:
            print("The directory is empty.")
    except Exception as e:
        print(Fore.RED + f"Error while listing contents: {e}")