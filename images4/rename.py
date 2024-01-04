
import os

def rename_files(folder_path, base_name):
    # Change working directory to the folder containing the files
    os.chdir(folder_path)

    # Get a list of all files in the directory
    files = os.listdir()

    # Sort the files to ensure a consistent order
    files.sort()

    # Counter for numbering the files
    counter = 300

    # Iterate through the files and rename them
    for file in files:
        # Construct the new file name
        new_name = f"{base_name}{counter}{os.path.splitext(file)[1]}"

        # Rename the file
        os.rename(file, new_name)

        # Increment the counter
        counter += 1

if __name__ == "__main__":
    # Replace 'folder_path' with the path to your folder containing the images

    folder_path = "images"

    # Replace 'base_name' with the desired base name for the files
    base_name = "img"

    rename_files(folder_path, base_name)

