import os
from colorama import Fore, init

init(autoreset=True)

def change_directory(directory):
    try:
        os.chdir(directory)
        print(f"Changed directory to: {os.getcwd()}")
    except Exception as e:
        print(f"Error while changing directory: {e}")