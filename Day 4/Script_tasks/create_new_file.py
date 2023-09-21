import os


def create_blank_file():
    directory_path = input("Enter the directory path where you want to create the file: ")

    file_name = input("Enter the name of the new file.: ")
    file_name_with_extension = f"{file_name}.txt"

    # Combine the path and file name to create the full file path
    full_file_path = os.path.join(directory_path, file_name_with_extension)

    try:
        # Create a new, blank file
        with open(full_file_path, 'w') as new_file:
            pass  # This line creates an empty file

        print(f"Blank file '{full_file_path}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


create_blank_file()
