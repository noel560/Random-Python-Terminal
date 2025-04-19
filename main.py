import os
import sys
from colorama import Fore, init
import shutil

import etc.help
import etc.list_directory
import etc.change_directory

init(autoreset=True)

#---\\---//---#=#---\\---//---#=#---\\---//---#=#---\\---//---#=#---\\---//---#
#                               Side Functions                                #
#---\\---//---#=#---\\---//---#=#---\\---//---#=#---\\---//---#=#---\\---//---#

def display_welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
    """
                _..----.._    _
                .'  .--.    "-.(0)_
    '-.__.-'"'=:|   ,  _)_ /__ . c\'-..
                '''------'---''---'-"
    """)
    print("")
    print("Welcome to RatShell! Your system. Our tunnels.")
    print("Type 'help' to see the list of commands.")
    print("")

#---\\---//---#=#---\\---//---#=#---\\---//---#=#---\\---//---#=#---\\---//---#
#                                    Main                                     #
#---\\---//---#=#---\\---//---#=#---\\---//---#=#---\\---//---#=#---\\---//---#

def main():
    display_welcome()

    username = os.getlogin() # Get the current username
    pc_name = os.uname().nodename if hasattr(os, 'uname') else os.environ.get('COMPUTERNAME', 'PC') # Get the PC name

    while True:
        current_directory = os.getcwd() # Get the current directory
        user_input = input(Fore.LIGHTGREEN_EX + f"{username}@{pc_name}" + Fore.WHITE + ":" + Fore.LIGHTBLUE_EX + current_directory + Fore.WHITE + "$ ")

        # SUDO Input handling
        match user_input.startswith("sudo"):

            case True:

                match user_input[5:]:

                    case "rmdir": # sudo rmdir command

                        directory_toberemoved = user_input[11:]
                        try:
                            shutil.rmtree(directory_toberemoved)
                            print(Fore.LIGHTGREEN_EX + f"Directory '{directory_toberemoved}' removed successfully.")
                        except FileNotFoundError:
                            print(Fore.RED + f"Directory '{directory_toberemoved}' does not exist.")
                        except Exception as e:
                            print(Fore.RED + f"Error removing directory: {e}")

                    case _:
                        print(Fore.RED + "Command not found. Type 'help' for a list of commands.")
                continue

            case False:
                pass

        # Normal Input handling
        match user_input:

            case "help": # help command
                etc.help.show_help()

            case "exit": # exit command
                sys.exit()

            case "clear" | "cls": # clear command
                os.system('cls' if os.name == 'nt' else 'clear')

            case str() if user_input.startswith("echo"): # echo command
                echo_text = user_input[5:]
                print(echo_text)

            case "reset": # reset terminal command
                display_welcome()

            case "ls" | "dir": # list files command
                etc.list_directory.dir()

            case str() if user_input.startswith("cd"): # change directory command
                directory = user_input[3:]
                etc.change_directory.change_directory(directory)

            case str() if user_input.startswith("mkdir "): # make directory command
                directory_tobemade = user_input[6:]
                try:
                    os.mkdir(directory_tobemade)
                    print(Fore.LIGHTGREEN_EX + f"Directory '{directory_tobemade}' created successfully.")
                except FileExistsError:
                    print(Fore.RED + f"Directory '{directory_tobemade}' already exists.")
                except Exception as e:
                    print(Fore.RED + f"Error creating directory: {e}")

            case str() if user_input.startswith("rmdir "): # remove directory command
                directory_toberemoved = user_input[6:]
                try:
                    os.rmdir(directory_toberemoved)
                    print(Fore.LIGHTGREEN_EX + f"Directory '{directory_toberemoved}' removed successfully.")
                except FileNotFoundError:
                    print(Fore.RED + f"Directory '{directory_toberemoved}' does not exist.")
                except OSError:
                    print(Fore.RED + f"Directory '{directory_toberemoved}' is not empty.")
                except Exception as e:
                    print(Fore.RED + f"Error removing directory: {e}")
            
            case str() if user_input.startswith("opendir "): # open directory command
                directory_to_open = user_input[8:]
                try:
                    if os.path.isdir(directory_to_open):
                        os.startfile(directory_to_open) if os.name == 'nt' else os.system(f'xdg-open "{directory_to_open}"')
                        print(Fore.LIGHTGREEN_EX + f"Opened directory '{directory_to_open}'.")
                    else:
                        print(Fore.RED + f"'{directory_to_open}' is not a valid directory.")
                except Exception as e:
                    print(Fore.RED + f"Error opening directory: {e}")

            case _: # unknown command
                print(Fore.RED + "Command not found. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()