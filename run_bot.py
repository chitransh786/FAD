from highrise.__main__ import *
import time
from config.load_permissions import load_settings

settings = load_settings()

bot_file_name = "main"
bot_class_name = "Bot"
data = settings["authorization"]
room_id = data.get("room")
bot_token = data.get("token")

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occourred: {e}")
        time.sleep(5)
