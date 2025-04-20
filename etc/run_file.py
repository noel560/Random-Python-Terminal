import os
from colorama import Fore, init

init(autoreset=True)

def run(command_to_run):
    try:
        os.system(command_to_run)
    except Exception as e:
        print(Fore.RED + f"Error running command: {e}")