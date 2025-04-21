import os
import sys
from colorama import Fore, init

import commands

# Initialize colorama
init(autoreset=True)

# Main execution function for commands
def execute(input):
    match input:
        # Help for specific commands -------------------------------------------
        case "cat": # Cat command
            print(Fore.RED + "See the content of a file\nUsage: cat <filename>")
            
        case "touch": # Touch command
            print(Fore.RED + "Make any file\nUsage: touch <filename>")

        case "rm": # Remove file command
            print(Fore.RED + "Remove any file\nUsage: rm <filename>")

        case "echo": # Echo command
            print(Fore.RED + "Echo any text\nUsage: echo <text>")
            
        case "cd": # Change directory command
            print(Fore.RED + "Change directory\nUsage: cd <directory>")

        case "opendir ": # Open directory command
            print(Fore.RED + "Open a directory\nUsage: opendir <directory>")

        case "rmdir": # Remove directory command
            print(Fore.RED + "Remove a directory\nUsage: rmdir <directory>")

        case "mkdir": # Make directory command
            print(Fore.RED + "Make a directory\nUsage: mkdir <directory>")

        case "whereis": # Whereis command
            print(Fore.RED + "Find a file\nUsage: whereis <filename>")

        case "zip": # Zip command
            print(Fore.RED + "Compress a file or directory\nUsage: zip <path>")

        case "unzip": # Unzip command
            print(Fore.RED + "Uncompress a zip file\nUsage: unzip <path>")

        case "run": # Run command
            print(Fore.RED + "Run any shell command\nUsage: run <command>")
        #----------------------------------------------------------------------

        # Input handling for commands
        case "help": # Help command
            commands.show_help()
        
        case "clear" | "cls": # Clear command
            os.system('cls' if os.name == 'nt' else 'clear')

        case str() if input.startswith("echo"): # Echo command
            echo_text = input[5:]
            print(echo_text)
        
        case "reset": # Reset terminal command
            display_welcome()

        case "ls" | "dir": # List directory command
            commands.list_directory()

        case str() if input.startswith("cd"): # Change directory command
            directory = input[3:]
            commands.change_directory(directory)

        case str() if input.startswith("mkdir"): # Make directory command
            directory = input[6:]
            commands.make_directory(directory)

        case str() if input.startswith("rmdir"): # Remove directory command
            directory = input[6:]
            commands.remove_directory(directory)

        case str() if input.startswith("opendir"): # Open directory command
            directory = input[8:]
            commands.open_directory(directory)

        case "opendir": # Open current directory command
            commands.open_current_directory()

        case str() if input.startswith("run"): # Run command
            command_to_run = input[4:]
            commands.run(command_to_run)

        case str() if input.startswith("touch"): # Touch command
            filename = input[6:]
            commands.touch(filename)

        case str() if input.startswith("cat"): # Cat command
            filename = input[4:]
            commands.cat(filename)

        case str() if input.startswith("rm"): # Remove file command
            filename = input[3:]
            commands.remove_file(filename)

        case str() if input.startswith("whereis"): # Whereis command
            filename = input[8:]
            commands.whereis(filename)

        case str() if input.startswith("zip"): # Zip command
            path = input[4:]
            commands.zip(path)

        case str() if input.startswith("unzip"): # Unzip command
            zip_path = input[6:]
            commands.unzip(zip_path)

        case "uptime": # Uptime command
            pass

        case "whoami": # Whoami command
            pass

        case "tree": # Tree command
            pass

        case str() if input.startswith("stat"): # Stat command
            pass

        case str() if input.startswith("mv"): # Move command
            pass

        case str() if input.startswith("cp"): # Copy command
            pass

        case str() if input.startswith("rename"): # Rename command
            pass
        
        case _:
            print(Fore.RED + "Command not found. Type 'help' for a list of commands.")

# Function to display the welcome message
def display_welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.chdir(os.path.expanduser("~")) # Change directory to the user's home directory
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

# Main function to handle user input and command execution
def main():
    display_welcome()

    username = os.getlogin() # Get the current user's name
    pc_name = os.uname().nodename if hasattr(os, 'uname') else os.environ.get('COMPUTERNAME', 'PC') # Get the PC name

    os.chdir(os.path.expanduser("~")) # Change directory to the user's home directory

    while True:
        current_directory = os.getcwd() # Get the current directory
        user_input = input(Fore.LIGHTGREEN_EX + f"{username}@{pc_name}" + Fore.WHITE + ":" + Fore.LIGHTBLUE_EX + current_directory + Fore.WHITE + "$ ")

        if user_input == "exit":
            sys.exit(0)
        else:
            try:
                execute(user_input)
            except Exception as e:
                print(Fore.RED + f"Error: {e}")
                continue

if __name__ == "__main__":
    main()