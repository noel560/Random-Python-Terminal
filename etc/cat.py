from colorama import init, Fore

init(autoreset=True)

def cat(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
        print(Fore.LIGHTGREEN_EX + f"Contents of {filename}:" + Fore.WHITE + f"\n{contents}")
    except Exception as e:
        print(Fore.RED + f"Error while reading file: {e}")