import json

def load_settings():
    try:
        with open("config/config.json", "r") as file:
            settings = json.load(file)

        # Check for the 'authorization' key
        if 'authorization' not in settings:
            raise ValueError("Missing 'authorization' key in settings.json")

        return settings

    except FileNotFoundError:
        print("settings.json file not found. Please check the file path.")
    except json.JSONDecodeError:
        print("Error decoding settings.json. Please check the file format.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None