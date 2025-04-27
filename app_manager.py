import json
import subprocess
from colorama import Fore, init
import os

init(autoreset=True)

# Function to load application data from a JSON file
def load_app_data():
    # Get the directory of the current script
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the JSON file containing app data
    json_path = os.path.join(base_path, "apps.json")
    # Open and load the JSON file
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Function to install an application using its nickname
def install_app(nickname):
    # Load the app data from the JSON file
    apps = load_app_data()
    # Get the app ID corresponding to the nickname
    app_id = apps.get(nickname.lower())

    # If the app ID is not found, display an error message
    if not app_id:
        print(Fore.RED + f"Unknown app: {nickname}")
        return

    # Notify the user that the download has started
    print(Fore.LIGHTYELLOW_EX + f"Downloading started: {nickname} ({app_id})")

    try:
        # Run the winget command to install the app silently
        process = subprocess.Popen(
            ["winget", "install", "--id", app_id, "--silent", "--accept-package-agreements", "--accept-source-agreements"],
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.STDOUT,  # Redirect standard error to standard output
            text=True  # Enable text mode for output
        )

        # Print the output of the installation process line by line
        for line in process.stdout:
            print("🔄", line.strip())

        # Wait for the process to complete
        process.wait()
        # Check the return code to determine success or failure
        if process.returncode == 0:
            print(Fore.LIGHTGREEN_EX + f"{nickname} downloaded successfully!")
        else:
            print(Fore.RED + f"Error {nickname} while downloading. (Error: {process.returncode})")
    except FileNotFoundError:
        # Handle the case where the winget command is not found
        print(Fore.RED + "Not found.")

# Function to uninstall an application using its nickname
def uninstall_app(nickname):
    # Load the app data from the JSON file
    apps = load_app_data()
    # Get the app ID corresponding to the nickname
    app_id = apps.get(nickname.lower())

    # If the app ID is not found, display an error message
    if not app_id:
        print(Fore.RED + f"Unknown app: {nickname}")
        return

    # Notify the user that the uninstallation has started
    print(Fore.LIGHTYELLOW_EX + f"Deleting started: {nickname} ({app_id})")

    try:
        # Run the winget command to uninstall the app silently
        result = subprocess.run(
            ["winget", "uninstall", "--id", app_id, "--silent"],
            capture_output=True,  # Capture both stdout and stderr
            text=True  # Enable text mode for output
        )
        # Print the output of the uninstallation process
        print(result.stdout)
        # Check the return code to determine success or failure
        if result.returncode == 0:
            print(Fore.LIGHTGREEN_EX + f"{nickname} deleted successfully!")
        else:
            print(Fore.RED + f"Error {nickname} while deleting.")
    except FileNotFoundError:
        # Handle the case where the winget command is not found
        print(Fore.RED + "Not found.")

# Function to list all installed applications using winget
def list_apps():
    # Run the winget list command to display installed apps
    subprocess.run(["winget", "list"])