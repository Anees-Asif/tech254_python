import json


def parse_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                print(f"{key}: {value}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")



file_path = input("Enter the path to the JSON file: ")

parse_json_file(file_path)
