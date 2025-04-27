import os
import sys
import time
from colorama import Fore, init
import requests
import urllib.request
import subprocess

import commands

start_time = time.time()

CURRENT_VERSION = "1.0.4" # Current version of the application

# Initialize colorama
init(autoreset=True)

# Function to fettch the latest version of the application from a GitHub repository
def get_latest_version():
    try:
        with urllib.request.urlopen("https://raw.githubusercontent.com/noel560/Random-Python-Terminal/main/version.txt") as response:
            return response.read().decode().strip()
    except:
        return None  # Return None if the request fails

# Function to update the application by downloading the latest installer
def update_app():
    url = "https://github.com/noel560/Random-Python-Terminal/releases/latest/download/RatShell.Setup.exe"
    local_filename = os.path.join(os.getenv("TEMP"), "RatShell Setup.exe")

    response = requests.get(url, stream=True)
    if response.status_code == 200:  # Check if the download was successful
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        subprocess.Popen([local_filename])  # Run the installer
        sys.exit()  # Exit the current application
    else:
        print(f"Download failed with status code {response.status_code}")

# Main function to execute user commands
def execute(input):
    match input:
        # Help command: Dispalys a list of available commands
        case "help":
            commands.show_help()

        # Version command: Displays the current version of the application
        case "version":
            print(Fore.LIGHTYELLOW_EX + f"RatShell version: {CURRENT_VERSION}")

        # Update command: Checks for updates and updates the application if needed
        case "update":
            latest = get_latest_version()
            if latest and latest != CURRENT_VERSION:
                print(Fore.RED + f"New version available: {latest}. Updating...")
                update_app()
            else:
                print(Fore.LIGHTYELLOW_EX + "You are using the latest version.")

        # Clear command: Clears the terminal screen
        case "clear" | "cls":
            os.system('cls' if os.name == 'nt' else 'clear')

        # Echo command: Prints the provided text
        case str() if input.startswith("echo"):
            echo_text = input[5:]
            print(Fore.LIGHTYELLOW_EX + echo_text)

        # Reset command: Resets the terminal and displays the welcome message
        case "reset":
            display_welcome()

        # List directory command: Lists files and directories in the current directory
        case "ls" | "dir":
            commands.list_directory()

        # Change directory command: Changes the current working directory
        case str() if input.startswith("cd"):
            directory = input[3:]
            commands.change_directory(directory)

        # Make directory command: Creates a new directory
        case str() if input.startswith("mkdir"):
            directory = input[6:]
            commands.make_directory(directory)

        # Remove directory command: Deletes a directory
        case str() if input.startswith("rmdir"):
            directory = input[6:]
            commands.remove_directory(directory)

        # Open current directory command: Opens the current directory in the file explorer
        case "opendir":
            commands.open_current_directory()

        # Open specific directory command: Opens a specified directory in the file explorer
        case str() if input.startswith("opendir"):
            directory = input[8:]
            commands.open_directory(directory)

        # Run command: Executes a shell command
        case str() if input.startswith("run"):
            command_to_run = input[4:]
            commands.run(command_to_run)

        # Touch command: Creates an empty file
        case str() if input.startswith("touch"):
            filename = input[6:]
            commands.touch(filename)

        # Cat command: Displays the contents of a file
        case str() if input.startswith("cat"):
            filename = input[4:]
            commands.cat(filename)

        # Remove file command: Deletes a file
        case str() if input.startswith("rm"):
            filename = input[3:]
            commands.remove_file(filename)

        # Whereis command: Locates a file in the system
        case str() if input.startswith("whereis"):
            filename = input[8:]
            commands.whereis(filename)

        # Zip command: Compresses a file or directory
        case str() if input.startswith("zip"):
            path = input[4:]
            commands.zip(path)

        # Unzip command: Extracts a compressed file
        case str() if input.startswith("unzip"):
            zip_path = input[6:]
            commands.unzip(zip_path)

        # Uptime command: Displays the time since the application started
        case "uptime":
            uptime_seconds = time.time() - start_time
            uptime_minutes, uptime_seconds = divmod(uptime_seconds, 60)
            uptime_hours, uptime_minutes = divmod(uptime_minutes, 60)
            print(Fore.LIGHTYELLOW_EX + f"Terminal uptime: {int(uptime_hours)}h {int(uptime_minutes)}m {int(uptime_seconds)}s")

        # Whoami command: Displays the current user's name
        case "whoami":
            print(Fore.LIGHTYELLOW_EX + f"Current user: {os.getlogin()}")

        # Tree command: Displays the directory structure
        case str() if input.startswith("tree"):
            path = input[5:]
            commands.tree(path)

        # Stat command: Displays file or directory statistics
        case str() if input.startswith("stat"):
            path = input[5:]
            commands.stat(path)

        # Move command: Moves a file or directory
        case str() if input.startswith("mv") or input.startswith("move"):
            if input.startswith("mv"):
                item, destination = input[3:].split(" ")
                commands.mv(item, destination)
            else:
                item, destination = input[5:].split(" ")
                commands.mv(item, destination)

        # Copy command: Copies a file or directory
        case str() if input.startswith("cp") or input.startswith("copy"):
            if input.startswith("cp"):
                from_path, to_path = input[3:].split(" ")
                commands.cp(from_path, to_path)
            else:
                from_path, to_path = input[5:].split(" ")
                commands.cp(from_path, to_path)

        # Rename command: Renames a file or directory
        case str() if input.startswith("rename"):
            old_name, new_name = input[7:].split(" ")
            commands.rename(old_name, new_name)

        # Install command: Installs an application
        case str() if input.startswith("install"):
            import app_manager
            app_name = input[8:]
            app_manager.install_app(app_name)

        # Uninstall command: Uninstalls an application
        case str() if input.startswith("uninstall"):
            import app_manager
            app_name = input[10:]
            app_manager.uninstall_app(app_name)

        # List installed apps command: Displays a list of installed applications
        case "applist":
            import app_manager
            print(Fore.LIGHTYELLOW_EX + "Showing installed apps...")
            app_manager.list_apps()

        # Kill command: Terminates a process
        case str() if input.startswith("kill"):
            process_name = input[5:]
            commands.kill(process_name)

        # Coin flip command: Simulates a coin flip
        case "coinflip":
            commands.coinflip()

        # Stopwatch command: Starts a stopwatch
        case "stopwatch":
            commands.stopwatch()

        # Random number command: Generates a random number within a range
        case str() if input.startswith("randnum"):
            try:
                _, min_num, max_num = input.split(" ")
                commands.randnum(int(min_num), int(max_num))
            except ValueError:
                print(Fore.RED + "Usage: randnum <min> <max>")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        # Calculator command: Evaluates a mathematical expression
        case str() if input.startswith("calc"):
            expression = input[5:]
            commands.calc(expression)

        # Encrypt command: Encrypts a file
        case str() if input.startswith("encrypt"):
            try:
                _, file_path, password = input.split(" ")
                commands.encrypt_file(file_path, password)
            except ValueError:
                print(Fore.RED + "Encrypts a file\nUsage: encrypt <file_path> <password>")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        # Decrypt command: Decrypts a file
        case str() if input.startswith("decrypt"):
            try:
                _, file_path, password = input.split(" ")
                commands.decrypt_file(file_path, password)
            except ValueError:
                print(Fore.RED + "Wrong password\nUsage: decrypt <file_path> <password>")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        # Process list command: Displays a list of running processes
        case "processlist":
            result = subprocess.run('powershell "Get-WmiObject Win32_Process | ForEach-Object { $_.ProcessId, $_.ParentProcessId, $_.Name }"', shell=True, capture_output=True, text=True)
            print(Fore.LIGHTYELLOW_EX + result.stdout.strip())

        # Git command: Executes a Git command
        case str() if input.startswith("git"):
            result = subprocess.run(input, capture_output=True, text=True)
            if not result.stdout == "":
                print(Fore.LIGHTYELLOW_EX + result.stdout.strip())
            if not result.stderr == "":
                print(Fore.LIGHTYELLOW_EX + result.stderr.strip())

        # Print working directory command: Displays the current working directory
        case "pwd":
            print(Fore.LIGHTYELLOW_EX + os.getcwd())

        # Currency conversion command: Converts currency values
        case str() if input.startswith("currency"):
            try:
                _, value, from_unit, to_unit = input.split(" ")
                commands.currency_converter(value, from_unit, to_unit)
            except ValueError:
                print(Fore.RED + "Usage: currency <value> <from_unit> <to_unit>")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        # Notes command: Manages notes (add, view, remove, reset)
        case str() if input.startswith("notes"):
            try:
                _, action, *args = input.split(" ")
                if action == "add":
                    note = " ".join(args)
                    commands.notes_add(note)
                elif action == "view":
                    commands.notes_view()
                elif action == "remove":
                    note_id = args[0]
                    commands.notes_remove(note_id)
                elif action == "reset":
                    commands.notes_reset()
                else:
                    print(Fore.RED + "Usage: notes <add/view/remove/reset> [note]")
            except ValueError:
                print(Fore.RED + "Usage: notes <add/view/remove/reset> [note]")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")
        
        # Default case: Handles unknown commands
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
    display_welcome()  # Show the welcome message

    username = os.getlogin() # Get the current user's name
    pc_name = os.uname().nodename if hasattr(os, 'uname') else os.environ.get('COMPUTERNAME', 'PC') # Get the PC name

    os.chdir(os.path.expanduser("~")) # Change directory to the user's home directory

    # Check for updates and notify the user if a new version is available
    latest = get_latest_version()
    if latest and latest != CURRENT_VERSION:
        print(Fore.LIGHTGREEN_EX + f"New version available: {latest}. Type 'update' to update.")

    # Main loop to process user input
    while True:
        current_directory = os.getcwd() # Get the current directory
        user_input = input(Fore.LIGHTGREEN_EX + f"{username}@{pc_name}" + Fore.WHITE + ":" + Fore.LIGHTBLUE_EX + current_directory + Fore.WHITE + "$ ")

        if user_input == "exit":  # Exit the application
            sys.exit(0)
        else:
            try:
                execute(user_input)  # Execute the user command
            except Exception as e:
                print(Fore.RED + f"Error: {e}")  # Handle errors gracefully
                continue

# Entry point of the application
if __name__ == "__main__":
    main()