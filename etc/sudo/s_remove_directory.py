import shutil
from colorama import Fore, init

init(autoreset=True)

def remove_directory(directory_toberemoved):
    try:
        shutil.rmtree(directory_toberemoved)
        print(Fore.LIGHTGREEN_EX + f"Directory '{directory_toberemoved}' removed successfully.")
    except FileNotFoundError:
        print(Fore.RED + f"Directory '{directory_toberemoved}' does not exist.")
    except Exception as e:
        print(Fore.RED + f"Error removing directory: {e}")
# Disabled, for now