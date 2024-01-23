from highrise import *
from highrise.models import *
from highrise.webapi import *
from highrise.models_webapi import *
from config.load_permissions import load_settings
from config.load_emotes import extract_emote_commands
from src.commands.update import update
from src.commands.crash import crash
from src.commands.uptime import get_uptime
from src.eventHandle import start

async def message(self: BaseBot, user_id, conversation_id, is_new_conversation) -> None:
    settings = load_settings()
  
    parts = conversation_id.split(":")
    id = parts[1]
    resp = await self.webapi.get_user(id)
    usernme = resp.user.username

    message = await self.highrise.get_conversations(False)
    message = await self.highrise.get_messages(conversation_id)
    msg_content = message.messages[0]  # Accessing the last message in the list
    message_content = msg_content.content  # Retrieving the content of the last message
  
    if settings["loggers"].get("message", False):
        log_print = f"{usernme} -> {message_content}"
        print(log_print)

    if message_content.lower().startswith("settings "):
        res = await update(self, usernme, message_content)
        await self.highrise.send_message(conversation_id, res, 'text')

    if message_content.lower().startswith("uptime"):
        reply = await get_uptime(start.start.start_time)
        await self.highrise.send_message(conversation_id, reply, "text", None)

    if message_content.lower().startswith("emotelist"):
        reply = extract_emote_commands()
        await self.highrise.send_message(conversation_id, reply, "text", None)

    if message_content.startswith("crash"):
        await crash()