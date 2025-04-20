import os
from colorama import Fore, init

init(autoreset=True)

def change_directory(directory):
    try:
        os.chdir(directory)
        print(Fore.LIGHTGREEN_EX + f"Changed directory to: {os.getcwd()}")
    except Exception as e:
        print(Fore.RED + f"Error while changing directory: {e}")