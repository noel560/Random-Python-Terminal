import os
import zipfile
from colorama import Fore, init

init(autoreset=True)

def unzip_path(zip_path):
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
        print(Fore.LIGHTGREEN_EX + f"Success: '{zip_path}' has been extracted to '{extract_dir}'.")
    else:
        print(Fore.RED + f"Error: Failed to extract contents of '{zip_path}'.")