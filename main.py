import os
import sys
import time
from colorama import Fore, init
import requests
import urllib.request
import subprocess

import commands

start_time = time.time()

CURRENT_VERSION = "1.0.3" # Current version of the application

# Initialize colorama
init(autoreset=True)

# Get the latest version from the GitHub repository
def get_latest_version():
    try:
        with urllib.request.urlopen("https://raw.githubusercontent.com/noel560/Random-Python-Terminal/main/version.txt") as response:
            return response.read().decode().strip()
    except:
        return None

# Function to update the application
def update_app():
    url = "https://github.com/noel560/Random-Python-Terminal/releases/latest/download/RatShell.Setup.exe"
    local_filename = os.path.join(os.getenv("TEMP"), "RatShell Setup.exe")

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        subprocess.Popen([local_filename])
        sys.exit()
    else:
        print(f"Download failed with status code {response.status_code}")


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

        case "tree": # Tree command
            print(Fore.RED + "Display the directory structure\nUsage: tree <path>")

        case "stat": # Stat command
            print(Fore.RED + "Display file or directory information\nUsage: stat <path>")

        case "mv" | "move": # Move command
            print(Fore.RED + "Move a file or directory\nUsage: mv <item> <destination>")

        case "cp" | "copy": # Copy command
            print(Fore.RED + "Copy a file or directory\nUsage: cp <from_path> <to_path>")

        case "rename": # Rename command
            print(Fore.RED + "Rename a file or directory\nUsage: rename <old_name> <new_name>")
        
        case "install": # Install command
            print(Fore.RED + "Install an app\nUsage: install <app_name>")

        case "uninstall": # Uninstall command
            print(Fore.RED + "Uninstall an app\nUsage: uninstall <app_name>")

        case "kill": # Kill command
            print(Fore.RED + "Kill a process\nUsage: kill <process_name>")
        
        case "randnum": # Random command
            print(Fore.RED + "Generate a random number\nUsage: randnum <min> <max>")
        
        case "convert": # Convert command
            print(Fore.RED + "Converts between different units\nUsage: convert <value> <from_unit> <to_unit>")

        case "calc": # Calculator command
            print(Fore.RED + "Simple calculator\nUsage: calc <expression>")

        case "encrypt": # Encrypt command
            print(Fore.RED + "Encrypt a file\nUsage: encrypt <file_path> <password>")

        case "decrypt": # Decrypt command
            print(Fore.RED + "Decrypt a file\nUsage: decrypt <file_path> <password>")

        case "git": # Git command
            print(Fore.RED + "Git command\nUsage: git <command>")
        #----------------------------------------------------------------------

        # Input handling for commands
        case "help": # Help command
            commands.show_help()

        case "version": # Version command
            print(Fore.LIGHTYELLOW_EX + f"RatShell version: {CURRENT_VERSION}")

        case "update": # Update command
            latest = get_latest_version()
            if latest and latest != CURRENT_VERSION:
                print(Fore.RED + f"New version available: {latest}. Updating...")
                update_app()
            else:
                print(Fore.LIGHTYELLOW_EX + "You are using the latest version.")
        
        case "clear" | "cls": # Clear command
            os.system('cls' if os.name == 'nt' else 'clear')

        case str() if input.startswith("echo"): # Echo command
            echo_text = input[5:]
            print(Fore.LIGHTYELLOW_EX + echo_text)
        
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

        case "opendir": # Open current directory command
            commands.open_current_directory()

        case str() if input.startswith("opendir"): # Open directory command
            directory = input[8:]
            commands.open_directory(directory)

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
            uptime_seconds = time.time() - start_time
            uptime_minutes, uptime_seconds = divmod(uptime_seconds, 60)
            uptime_hours, uptime_minutes = divmod(uptime_minutes, 60)
            print(Fore.LIGHTYELLOW_EX + f"Terminal uptime: {int(uptime_hours)}h {int(uptime_minutes)}m {int(uptime_seconds)}s")

        case "whoami": # Whoami command
            print(Fore.LIGHTYELLOW_EX + f"Current user: {os.getlogin()}")

        case str() if input.startswith("tree"): # Tree command
            path = input[5:]
            commands.tree(path)

        case str() if input.startswith("stat"): # Stat command
            path = input[5:]
            commands.stat(path)

        case str() if input.startswith("mv") or input.startswith("move"): # Move command
            if input.startswith("mv"):
                item, destination = input[3:].split(" ")
                commands.mv(item, destination)
            else:
                item, destination = input[5:].split(" ")
                commands.move(item, destination)

        case str() if input.startswith("cp") or input.startswith("copy"): # Copy command
            if input.startswith("cp"):
                from_path, to_path = input[3:].split(" ")
                commands.cp(from_path, to_path)
            else:
                from_path, to_path = input[5:].split(" ")
                commands.copy(from_path, to_path)

        case str() if input.startswith("rename"): # Rename command
            old_name, new_name = input[7:].split(" ")
            commands.rename(old_name, new_name)

        case str() if input.startswith("install"): # Install command
            import app_manager
            app_name = input[8:]
            app_manager.install_app(app_name)
        
        case str() if input.startswith("uninstall"): # Uninstall command
            import app_manager
            app_name = input[10:]
            app_manager.uninstall_app(app_name)
        
        case "applist": # List installed apps command
            import app_manager
            print(Fore.LIGHTYELLOW_EX + "Showing installed apps...")
            app_manager.list_apps()

        case str() if input.startswith("kill"): # Kill command
            process_name = input[5:]
            commands.kill(process_name)

        case "coinflip": # Coin flip command
            commands.coinflip()

        case "stopwatch": # Stopwatch command
            commands.stopwatch()

        case str() if input.startswith("randnum"): # Random number command
            try:
                _, min_num, max_num = input.split(" ")
                commands.randnum(int(min_num), int(max_num))
            except ValueError:
                print(Fore.RED + "Usage: randnum <min> <max>")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        case str() if input.startswith("calc"): # Calc command
            expression = input[5:]
            commands.calc(expression)

        case str() if input.startswith("encrypt"): # Encrypt command
            try:
                _, file_path, password = input.split(" ")
                commands.encrypt_file(file_path, password)
            except ValueError:
                print(Fore.RED + "Usage: encrypt <file_path> <password>")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        case str() if input.startswith("decrypt"): # Decrypt command
            try:
                _, file_path, password = input.split(" ")
                commands.decrypt_file(file_path, password)
            except ValueError:
                print(Fore.RED + "Wrong password\nUsage: decrypt <file_path> <password>")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        case "processlist": # Process list command
            result=subprocess.run('powershell "Get-WmiObject Win32_Process | ForEach-Object { $_.ProcessId, $_.ParentProcessId, $_.Name }"', shell=True, capture_output=True, text=True)
            print(Fore.LIGHTYELLOW_EX + result.stdout.strip())

        case str() if input.startswith("git"): # Git command
            git_command = input[4:]
            result = subprocess.run(['git'] + git_command.split(), capture_output=True, text=True)
            print(Fore.LIGHTYELLOW_EX + result.stdout.strip())

        case "pwd": # Print working directory command
            print(Fore.LIGHTYELLOW_EX + os.getcwd())
        
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

    latest = get_latest_version()
    if latest and latest != CURRENT_VERSION:
        print(Fore.LIGHTGREEN_EX + f"New version available: {latest}. Type 'update' to update.")

# Main function to handle user input and command execution
def main():
    #latest = get_latest_version()
    #if latest and latest != CURRENT_VERSION:
    #    print(Fore.RED + f"New version available: {latest}. Updating...")
    #    update_app()

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