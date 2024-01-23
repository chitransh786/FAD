import json, random

def load_emotes_data():
    file_path = "config/emotes.json"
    try:
        with open(file_path, 'r') as file:
            emote_data = json.load(file)
            return emote_data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} does not contain valid JSON.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def extract_emote_commands():
    file_path = "config/emotes.json"
    with open(file_path, 'r') as file:
        emote_data = json.load(file)
    command_names = [item["command"] for item in emote_data]

    # Creating a formatted string with all commands in a numbered list
    commands_string = '\n'.join([f"{i+1}. {command}" for i, command in enumerate(command_names)])

    return commands_string

emotes = load_emotes_data()