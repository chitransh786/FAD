from highrise import *
from highrise.models import *
from config.load_permissions import load_settings
import random

async def on_tip(self: BaseBot, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:

    settings = load_settings()
  
    if settings["loggers"].get("tips", False):
        print(f"{sender.username} tipped {receiver.username} {tip.amount} {tip.type}!")

    if receiver.id == settings["config"].get("botID", False):
        await self.highrise.chat(f"Thanks for giving {tip.amount} gold to me @{sender.username} !")
        options = ['heart', 'thumbs', 'wink']  # Valid Reaction values
        random_choice = random.choice(options)
        await self.highrise.react(random_choice, sender.id)
    else:
        await self.highrise.chat(f" @{sender.username} tipped {tip.amount} gold to @{receiver.username} !")
