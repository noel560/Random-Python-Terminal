from colorama import Fore, init

init(autoreset=True)

def touch(filename):
    try:
        with open(filename, 'w') as file:
            file.write("")
        print(Fore.LIGHTGREEN_EX + f"File created: {filename}")
    except Exception as e:
        print(Fore.RED + f"Error while creating file: {e}")