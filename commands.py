from colorama import init, Fore
import os
import zipfile
from datetime import datetime
import random
import time
import math
from simpleeval import simple_eval
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import hashlib

init(autoreset=True)

# Help commands | commands.show_help() | Shows the list of commands
def show_help():
    #commands="help exit clear cls echo reset ls dir cd mkdir rmdir opendir run cat touch rm whereis zip unzip uptime whoami tree stat mv cp rename install uninstall applist"
    #commands=commands.replace(" ","\n")
    #print(commands)
    help_text = """
    Available Commands:

    help       - Displays this help message.
                Usage: help

    exit       - Exits the terminal interface.
                Usage: exit

    clear / cls - Clears the screen.
                Usage: clear OR cls

    echo       - Prints a message to the screen.
                Usage: echo <message>

    reset      - Resets the terminal or its state (custom behavior, define if needed).
                Usage: reset

    ls / dir   - Lists the files and directories in the current directory.
                Usage: ls OR dir

    cd         - Changes the current directory.
                Usage: cd <path>

    mkdir      - Creates a new directory.
                Usage: mkdir <directory_name>

    rmdir      - Removes an empty directory.
                Usage: rmdir <directory_name>

    opendir    - Opens the current directory in the file explorer or a specified directory.
                Usage: opendir <path>

    run        - Executes a file or program.
                Usage: run <path> (example: run C:/Windows/System32/calc.exe)

    cat        - Displays the contents of a file.
                Usage: cat <filename>

    touch      - Creates an empty file or updates the modification time.
                Usage: touch <filename>

    rm         - Deletes a file.
                Usage: rm <filename>

    whereis    - Locates the full path of a program.
                Usage: whereis <app_name> (example: whereis explorer.exe)

    zip        - Compress any file/folder into a .zip archive.
                Usage: zip <path>

    unzip      - Extracts files from a .zip archive.
                Usage: unzip <archive_name.zip>

    uptime     - Shows how long the system has been running.
                Usage: uptime

    whoami     - Displays the current user.
                Usage: whoami

    tree       - Displays directory structure as a tree.
                Usage: tree <path>

    stat       - Shows detailed file or directory information.
                Usage: stat <filename or directory>

    mv         - Moves or renames a file or directory.
                Usage: mv <source> <destination>

    cp         - Copies a file or directory.
                Usage: cp <source> <destination>

    rename     - Renames a file or directory.
                Usage: rename <old_name> <new_name>

    install    - Installs an application using winget.
                Usage: install <app_name>

    uninstall  - Uninstalls an application using winget.
                Usage: uninstall <app_name>

    applist    - Lists downloaded applications.
                Usage: applist

    kill       - Kills a specified process.
                Usage: kill <process_name>

    coinflip   - Simulates a coin flip.
                Usage: coinflip

    stopwatch  - Starts a stopwatch. Type 'stopwatch' again to stop it.
                Usage: stopwatch

    randnum    - Generates a random number between min and max.
                Usage: randnum <min> <max>
    
    calc       - Evaluates a mathematical expression.
                Usage: calc <expression>

    encrypt    - Encrypts a file using AES encryption.
                Usage: encrypt <file_path> <password>

    decrypt    - Decrypts a file using AES decryption.
                Usage: decrypt <file_path> <password>
    """

    print(Fore.LIGHTYELLOW_EX + help_text)

# Cat command | commands.cat(filename) | Reads the contents of a file
def cat(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
        print(Fore.LIGHTYELLOW_EX + f"Contents of {filename}:" + Fore.WHITE + f"\n{contents}")
    except Exception as e:
        print(Fore.RED + f"Error while reading file: {e}")

# Change directory (cd) command | commands.change_directory(directory) | Changes the current working directory
def change_directory(directory):
    try:
        os.chdir(directory)
        print(Fore.LIGHTYELLOW_EX + f"Changed directory to: {os.getcwd()}")
    except Exception as e:
        print(Fore.RED + f"Error while changing directory: {e}")

# List directory (ls) command | commands.list_directory() | Lists the contents of the current directory
def list_directory():
    try:
        contents = os.listdir(os.getcwd())
        if contents:
            for item in contents:
                if os.path.isdir(item):
                    print(Fore.LIGHTYELLOW_EX + f"{item}/")  # Mappa
                else:
                    print(f"{item}")  # Fájl
        else:
            print("The directory is empty.")
    except Exception as e:
        print(Fore.RED + f"Error while listing contents: {e}")

# Make directory (mkdir) command | commands.make_directory(directory) | Creates a new directory
def make_directory(directory):
    try:
        os.mkdir(directory)
        print(Fore.LIGHTYELLOW_EX + f"Directory '{directory}' created successfully.")
    except FileExistsError:
        print(Fore.RED + f"Directory '{directory}' already exists.")
    except Exception as e:
        print(Fore.RED + f"Error creating directory: {e}")

# Remove directory (rmdir) command | commands.remove_directory(directory) | Removes a specified directory
def remove_directory(directory):
    try:
        os.rmdir(directory)
        print(Fore.LIGHTYELLOW_EX + f"Directory '{directory}' removed successfully.")
    except FileNotFoundError:
        print(Fore.RED + f"Directory '{directory}' does not exist.")
    except OSError:
        print(Fore.RED + f"Directory '{directory}' is not empty.")
    except Exception as e:
        print(Fore.RED + f"Error removing directory: {e}")

# Open current directory (opendir) command | commands.open_current_directory() | Opens the current directory in the file explorer
def open_current_directory():
    try:
        os.startfile(os.getcwd()) if os.name == 'nt' else os.system(f'xdg-open "{os.getcwd()}"')
        print(Fore.LIGHTYELLOW_EX + f"Opened current directory '{os.getcwd()}'.")
    except Exception as e:
            print(Fore.RED + f"Error opening current directory: {e}")

# Open directory (opendir) command | commands.open_directory(directory) | Opens a specified directory in the file explorer
def open_directory(directory):
    try:
        if os.path.isdir(directory):
            os.startfile(directory) if os.name == 'nt' else os.system(f'xdg-open "{directory}"')
            print(Fore.LIGHTYELLOW_EX + f"Opened directory '{directory}'.")
        else:
            print(Fore.RED + f"'{directory}' is not a valid directory.")
    except Exception as e:
        print(Fore.RED + f"Error opening directory: {e}")

# Remove file (rm) command | commands.remove_file(filename) | Removes a specified file
def remove_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)
        print(Fore.LIGHTYELLOW_EX + f"File '{filename}' removed successfully.")
    else:
        print(Fore.RED + f"File '{filename}' not found.")

# Touch command | commands.touch(filename) | Creates a new file
def touch(filename):
    try:
        with open(filename, 'w') as file:
            file.write("")
        print(Fore.LIGHTYELLOW_EX + f"File created: {filename}")
    except Exception as e:
        print(Fore.RED + f"Error while creating file: {e}")

# Run command | commands.run(command_to_run) | Executes a specified command in the shell
def run(command_to_run):
    try:
        os.system(command_to_run)
    except Exception as e:
        print(Fore.RED + f"Error running command: {e}")

# Get drives for whereis command
def get_drives():
    return [f"{chr(drive)}:\\" for drive in range(65, 91) if os.path.exists(f"{chr(drive)}:\\")]
# Whereis command | commands.whereis(filename) | Searches for a file in all drives
def whereis(filename):
    drives = get_drives()
    for drive in drives:
        for root, dirs, files in os.walk(drive):  # Az összes meghajtót végigjárja
            if filename in files:
                print(Fore.GREEN + f"Found: {os.path.join(root, filename)}")
                return
    print(Fore.RED + "File not found.")

# Zip command | commands.zip(path) | Compresses a file or directory into a zip file
def zip(path):
    # Check if the path exists
    if not os.path.exists(path):
        print(Fore.RED + f"Error: Path '{path}' not found.")
        return

    # Check if the path is already a zip file
    if path.endswith('.zip'):
        print(Fore.RED + f"Error: Path '{path}' is already a zip file.")
        return

    # Define the zip file name
    zip_filename = f"{path}.zip"

    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isfile(path):
                # If it's a file, add it to the zip archive
                zipf.write(path, os.path.basename(path))
            elif os.path.isdir(path):
                # If it's a folder, add all its contents
                for root, dirs, files in os.walk(path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start=path)
                        zipf.write(file_path, arcname)
    except Exception as e:
        print(Fore.RED + f"Error: Failed to compress '{path}'. Reason: {e}")
        return

    # Verify if the zip file was created successfully
    if os.path.isfile(zip_filename):
        print(Fore.LIGHTYELLOW_EX + f"Success: '{path}' has been compressed to '{zip_filename}'.")
        return
    else:
        print(Fore.RED + f"Error: Failed to create zip file '{zip_filename}'.")
        return

# Unzip command | commands.unzip(zip_path) | Extracts a zip file to a specified directory
def unzip(zip_path):
    # Check if the zip file exists
    if not os.path.exists(zip_path):
        print(Fore.RED + f"Error: File '{zip_path}' not found.")
        return

    # Check if the file is a zip file
    if not zip_path.endswith('.zip'):
        print(Fore.RED + f"Error: File '{zip_path}' is not a zip file.")
        return

    # Define the extraction directory
    extract_dir = os.path.splitext(zip_path)[0]

    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            # Extract all contents to the extraction directory
            zipf.extractall(extract_dir)
    except Exception as e:
        print(Fore.RED + f"Error: Failed to extract '{zip_path}'. Reason: {e}")
        return

    # Verify if the extraction was successful
    if os.path.isdir(extract_dir):
        print(Fore.LIGHTYELLOW_EX + f"Success: '{zip_path}' has been extracted to '{extract_dir}'.")
    else:
        print(Fore.RED + f"Error: Failed to extract contents of '{zip_path}'.")

# Tree command | commands.tree(path) | Displays the directory structure in a tree format
def tree(path):
    try:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                level = root.replace(path, '').count(os.sep)
                indent = ' ' * 4 * (level)
                print(Fore.LIGHTYELLOW_EX + f"{indent}{os.path.basename(root)}/")
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    print(f"{subindent}{f}")
        else:
            print(Fore.RED + f"Path '{path}' does not exist.")
    except Exception as e:
        print(Fore.RED + f"Error while displaying tree: {e}")

# Stat command | commands.stat(path) | Display file or directory information
def stat(path):
    try:
        if os.path.exists(path):
            file_info = os.stat(path)
            print(Fore.LIGHTYELLOW_EX + f"Information for '{path}':")
            print(Fore.WHITE + f"Size: {file_info.st_size} bytes")
            print(Fore.WHITE + f"Last modified: {datetime.fromtimestamp(file_info.st_mtime)}")
            print(Fore.WHITE + f"Last accessed: {datetime.fromtimestamp(file_info.st_atime)}")
            print(Fore.WHITE + f"Creation time: {datetime.fromtimestamp(file_info.st_birthtime)}")
        else:
            print(Fore.RED + f"Path '{path}' does not exist.")
    except Exception as e:
        print(Fore.RED + f"Error while getting file information: {e}")

# Move command | commands.move(item, destination) | Moves a file or directory to a new location
def mv(item, destination):
    try:
        new_path = os.path.join(destination, os.path.basename(item))
        os.replace(item, new_path)
        print(Fore.LIGHTYELLOW_EX + f"Moved {item} to {destination}")
    except Exception as e:
        print(Fore.RED + f"Error while moving: {e}")

# Copy command | commands.copy(from_path, to_path) | Copies a file from one location to another
def cp(from_path, to_path):
    try:
        if os.path.isfile(from_path):
            with open(from_path, 'rb') as fsrc:
                with open(to_path, 'wb') as fdst:
                    fdst.write(fsrc.read())
            print(Fore.LIGHTYELLOW_EX + f"Copied {from_path} to {to_path}")
        else:
            print(Fore.RED + f"Source file '{from_path}' does not exist.")
    except Exception as e:
        print(Fore.RED + f"Error while copying: {e}")

# Rename command | commands.rename(old_name, new_name) | Renames a file or directory
def rename(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(Fore.LIGHTYELLOW_EX + f"Renamed '{old_name}' to '{new_name}'.")
    except Exception as e:
        print(Fore.RED + f"Error while renaming: {e}")

# Kill command | commands.kill(process_name) | Kills a specified process
def kill(process_name):
    try:
        os.system(f"taskkill /f /im {process_name}")
        print(Fore.LIGHTYELLOW_EX + f"Killed process '{process_name}'.")
    except Exception as e:
        print(Fore.RED + f"Error while killing process: {e}")

# Coinflip command | commands.coinflip() | Simulates a coin flip
def coinflip():
    print(Fore.LIGHTYELLOW_EX + "Flipping a coin.")
    time.sleep(0.5)
    print(Fore.LIGHTYELLOW_EX + "Flipping a coin..")
    time.sleep(0.5)
    print(Fore.LIGHTYELLOW_EX + "Flipping a coin...")
    time.sleep(0.5)

    result = random.choice(["Heads", "Tails"])
    print(Fore.LIGHTYELLOW_EX + f"Coin flip result: {result}")

# Stopwatch command | commands.stopwatch() | Starts and stops a stopwatch
stopwatch_start_time = None
def stopwatch():
    global stopwatch_start_time
    if stopwatch_start_time is None:
        # Start the stopwatch
        stopwatch_start_time = time.time()
        print(Fore.LIGHTYELLOW_EX + "Stopwatch started. Type 'stopwatch' again to stop.")
    else:
        # Stop the stopwatch and calculate elapsed time
        elapsed_time = time.time() - stopwatch_start_time
        stopwatch_start_time = None  # Reset the start time
        print(Fore.LIGHTYELLOW_EX + f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds.")

# Randnum command | commands.randnum() | Generates a random number between min and max
def randnum(min_num, max_num):
    try:
        min_num = int(min_num)
        max_num = int(max_num)
        if min_num >= max_num:
            print(Fore.RED + "Error: Minimum number must be less than maximum number.")
            return
        random_number = random.randint(min_num, max_num)
        print(Fore.LIGHTYELLOW_EX + f"Random number between {min_num} and {max_num}: {random_number}")
    except ValueError:
        print(Fore.RED + "Error: Please provide valid integers for min and max numbers.")
    except Exception as e:
        print(Fore.RED + f"Error while generating random number: {e}")

# Calc command | commands.calc(expression) | Evaluates a mathematical expression
def calc(expression):
    try:
        result = simple_eval(expression)
        print(Fore.LIGHTYELLOW_EX + f"Result: {result}")
    except Exception as e:
        print(Fore.RED + f"Error while calculating: {e}")

# Encrypt command | commands.encrypt(file_path, password) | Encrypts a file using AES encryption
def encrypt_file(file_path, password):
    key = hashlib.sha256(password.encode()).digest()

    iv = get_random_bytes(AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(file_path, 'rb') as file:
        file_data = file.read()

    padded_data = pad(file_data, AES.block_size)

    ciphertext = cipher.encrypt(padded_data)

    with open(file_path, 'wb') as output_file:
        output_file.write(base64.b64encode(iv + ciphertext))

    print(f"File '{file_path}' encrypted and saved as '{file_path}'.")

# Decrypt command | commands.decrypt(file_path, password) | Decrypts a file using AES decryption
def decrypt_file(file_path, password):
    key = hashlib.sha256(password.encode()).digest()

    with open(file_path, 'rb') as file:
        encrypted_data = base64.b64decode(file.read())

    iv = encrypted_data[:AES.block_size]
    ciphertext = encrypted_data[AES.block_size:]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(file_path, 'wb') as output_file:
        output_file.write(decrypted_data)

    print(f"File '{file_path}' decrypted and saved as '{file_path}'.")