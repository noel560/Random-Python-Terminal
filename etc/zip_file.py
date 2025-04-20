import os
import zipfile
from colorama import Fore, init

init(autoreset=True)

def zip_path(path):
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
        print(Fore.LIGHTGREEN_EX + f"Success: '{path}' has been compressed to '{zip_filename}'.")
        return
    else:
        print(Fore.RED + f"Error: Failed to create zip file '{zip_filename}'.")
        return