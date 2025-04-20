import os
from colorama import Fore, init

init(autoreset=True)

def make_directory(directory_tobemade):
    try:
        os.mkdir(directory_tobemade)
        print(Fore.LIGHTGREEN_EX + f"Directory '{directory_tobemade}' created successfully.")
    except FileExistsError:
        print(Fore.RED + f"Directory '{directory_tobemade}' already exists.")
    except Exception as e:
        print(Fore.RED + f"Error creating directory: {e}")