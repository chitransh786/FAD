import json
from typing import Union

async def update_json_value(section: str, key: str, new_value: Union[str, bool]):
    file_path = 'config/config.json'
    res = ""
    try:
        # Load the existing data
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Check if the section exists
        if section not in data:
            print(f"Section '{section}' not found in the file.")
            res = f"Section '{section}' not found in the file."
            return res

        # Check if new_value is a boolean in string format and convert it
        if new_value.lower() == "true":
            new_value = True
        elif new_value.lower() == "false":
            new_value = False

        # Update the value
        if key in data[section]:
            data[section][key] = new_value
            # Write the data back to the file
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Updated '{key}' in '{section}' to '{new_value}'.")
            res = f"Updated '{key}' in '{section}' to '{new_value}'."
        else:
            print(f"Key '{key}' not found in the section '{section}'.")
            res = f"Key '{key}' not found in the section '{section}'."

        return res
      
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_coordinates(key: str, x, y, z, facing, entity_id, anchor_ix):
    file_path = 'config/config.json'

    try:
        # Load the existing JSON data from the file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Check if x, y, z, and facing are provided
        if x is not None and y is not None and z is not None and facing is not None:
            data["config"][key] = {"x": x, "y": y, "z": z, "facing": facing}
        # Check if entity_id and anchor_ix are provided
        elif entity_id is not None and anchor_ix is not None:
            data["config"][key] = {"entity_id": entity_id, "anchor_ix": anchor_ix}
        else:
            print("Invalid parameters provided. Please provide either x, y, z, facing or entity_id, anchor_ix.")
            return False

        # Write the updated data back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Updated {key} successfully!")
        return True

    except FileNotFoundError:
        return f"Error: File {file_path} not found."
        return False
    except json.JSONDecodeError:
        return f"Error decoding {file_path}. Please check the file format."
        return False