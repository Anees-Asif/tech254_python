import os


def create_directory():
    directory_name = input("Enter the name of the directory: ")

    directory_path = input("Enter the directory path (leave empty for current directory): ")

    # Combine the path and directory name to create the full directory path
    full_directory_path = os.path.join(directory_path, directory_name)

    try:
        # Create the directory
        os.mkdir(full_directory_path)
        print(f"Directory '{full_directory_path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{full_directory_path}' already exists.")


create_directory()
