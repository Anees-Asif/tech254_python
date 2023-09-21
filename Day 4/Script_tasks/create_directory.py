import os


def create_directory():
    directory_name = input("Enter the name of the directory: ")

    try:
        # Create the directory
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")


create_directory()
