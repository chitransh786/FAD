from highrise import *
from highrise.models import *
from src.handlers.handleCommands import command_handler
from src.commands.emtn import emoting
from config.load_permissions import load_settings
from config.load_emotes import load_emotes_data
from src.commands.loop_emote import loop, stop_loop
from src.commands.react import react
from src.commands.iq import generate_iq_and_message
from src.commands.loveORhate import love_or_hate
import re

async def on_chat(self: BaseBot, user: User, message: str) -> None:
    settings = load_settings()

    # Split the message into parts
    message = message.lower()
    parts = message.split()
    command = parts[0]

    emotes = load_emotes_data()
    if settings["loggers"].get("chat", False):
        msg = f"{user.username} -> {message}"
        print(msg)  # This will still print the message to the console

    for emote_data in emotes:
        cmd = emote_data['command']
        emote = emote_data['emote']
        match = re.match(f"{cmd}\s+@([_\w.]+)", message, re.IGNORECASE)
        await emoting(self, match, cmd, emote, user, message)

    if command in ["heart", "thumb", "wave", "wink", "clap"]:
        await react(self, user, parts)

    if message.startswith("iq"):
        iq, message = generate_iq_and_message()
        msg = f"IQ Score of @{user.username}: {iq}, or {message}"
        await self.highrise.chat(msg)

    if message.startswith("loveorhate"):
        msg = love_or_hate()
        await self.highrise.chat(msg)

    if message.lstrip().startswith(settings['config'].get('prefix', '/')):
        await command_handler(self, user, message)

    