from highrise import *
from highrise.models import *
from config.update_settings import update_json_value

async def update(self: BaseBot, username: str, message: str):
    parts = message.split(" ")
    section = parts[1]
    key = parts[2]
    new_value = parts[3]

    res = await update_json_value(section, key, new_value)

    return res