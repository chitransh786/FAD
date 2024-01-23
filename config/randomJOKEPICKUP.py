import json
import random

def get_random_joke_or_pickup_line(category):
    try:
        with open('/home/runner/Bot/config/data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return random.choice(data.get(category, ["Category not found"]))
    except FileNotFoundError:
        return "File not found"
    except json.JSONDecodeError:
        return "Error decoding JSON"


# Example usage
category = random.choice(["jokes", "pickup_lines"])
message = get_random_joke_or_pickup_line('jokes')