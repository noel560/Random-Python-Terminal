import os
from colorama import Fore, init

init(autoreset=True)

def open_current_directory():
    try:
        os.startfile(os.getcwd()) if os.name == 'nt' else os.system(f'xdg-open "{os.getcwd()}"')
        print(Fore.LIGHTGREEN_EX + f"Opened current directory '{os.getcwd()}'.")
    except Exception as e:
            print(Fore.RED + f"Error opening current directory: {e}")

def open_directory(directory_to_open):
    try:
        if os.path.isdir(directory_to_open):
            os.startfile(directory_to_open) if os.name == 'nt' else os.system(f'xdg-open "{directory_to_open}"')
            print(Fore.LIGHTGREEN_EX + f"Opened directory '{directory_to_open}'.")
        else:
            print(Fore.RED + f"'{directory_to_open}' is not a valid directory.")
    except Exception as e:
        print(Fore.RED + f"Error opening directory: {e}")