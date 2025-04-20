import os
from colorama import Fore, init

init(autoreset=True)

def remove_directory(directory_toberemoved):
    try:
        os.rmdir(directory_toberemoved)
        print(Fore.LIGHTGREEN_EX + f"Directory '{directory_toberemoved}' removed successfully.")
    except FileNotFoundError:
        print(Fore.RED + f"Directory '{directory_toberemoved}' does not exist.")
    except OSError:
        print(Fore.RED + f"Directory '{directory_toberemoved}' is not empty.")
    except Exception as e:
        print(Fore.RED + f"Error removing directory: {e}")