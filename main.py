import os
import sys
from colorama import Fore, init
import shutil

# Local imports
import etc.help
import etc.list_directory
import etc.change_directory
import etc.make_directory
import etc.remove_directory
import etc.open_directory
import etc.run_file
import etc.touch
import etc.cat

#Sudo imports
import etc.sudo.s_remove_directory as sudo_remove_directory

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

    os.chdir(os.path.expanduser("~")) # Change directory to the user's home directory

    while True:
        current_directory = os.getcwd() # Get the current directory
        user_input = input(Fore.LIGHTGREEN_EX + f"{username}@{pc_name}" + Fore.WHITE + ":" + Fore.LIGHTBLUE_EX + current_directory + Fore.WHITE + "$ ")

        # SUDO Input handling
        match user_input.startswith("sudo"):
            case True:
                match user_input[5:]: # Check if the input starts with "sudo"
                    case "rmdir": # sudo rmdir command
                        directory_toberemoved = user_input[11:]
                        sudo_remove_directory.remove_directory(directory_toberemoved)

                    case _:
                        print(Fore.RED + "Command not found. Type 'help' for a list of commands.")
                continue # If sudo command is executed, continue to the next iteration
            case False: # If not a sudo command, continue with normal input handling
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
                etc.make_directory.make_directory(directory_tobemade)

            case str() if user_input.startswith("rmdir "): # remove directory command
                directory_toberemoved = user_input[6:]
                etc.remove_directory.remove_directory(directory_toberemoved)
            
            case str() if user_input.startswith("opendir "): # open directory command
                directory_to_open = user_input[8:]
                etc.open_directory.open_directory(directory_to_open)

            case "opendir": # open current directory command
                etc.open_directory.open_current_directory()

            case str() if user_input.startswith("run "): # run command
                command_to_run = user_input[4:]
                etc.run_file.run(command_to_run)

            case str() if user_input.startswith("touch "): # touch command
                filename = user_input[6:]
                etc.touch.touch(filename)

            case str() if user_input.startswith("cat "): # cat command
                filename = user_input[4:]
                etc.cat.cat(filename)
            
            case "cat":
                print(Fore.RED + "See the content of a file\nUsage: cat <filename>")
            
            case "touch":
                print(Fore.RED + "It makes a file you want\nUsage: touch <filename>")

            case _: # unknown command
                print(Fore.RED + "Command not found. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()