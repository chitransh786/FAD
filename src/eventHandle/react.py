from highrise import *
from highrise.models import *
from config.load_permissions import load_settings

async def on_reaction(self: BaseBot, user: User, reaction: Reaction, receiver: User) -> None:
    settings = load_settings()
  
    if settings["loggers"].get("reactions", False):
        print(f"{user.username} send {reaction} to {receiver.username}")
    if user.id == settings["config"].get("botID"):
        return  # Ignore reactions initiated by the bot itself
    if receiver.id == settings["config"].get("botID"):
        await self.highrise.react(reaction, user.id)
    else:
        await self.highrise.chat(f" @{user.username} send {reaction} to @{receiver.username}")
      