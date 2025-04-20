import os
from colorama import Fore, init

init(autoreset=True)

def remove(filename):
    if os.path.isfile(filename):
        os.remove(filename)
        print(Fore.LIGHTGREEN_EX + f"File '{filename}' removed successfully.")
    else:
        print(Fore.RED + f"File '{filename}' not found.")