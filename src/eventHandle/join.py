from highrise import *
from highrise.models import *
from config.load_permissions import load_settings
from config.load_emotes import emotes
import random


async def on_join(self: BaseBot, user: User, position: Position | AnchorPosition) -> None:
    settings = load_settings()
    if settings["loggers"].get("joins", False):
        message = f"User joined: {user.username}:{user.id}"
        print(message)  # This will still print the message to the console
  
    if position is not None:
  
        config = settings["config"]
  
        await self.highrise.send_whisper(user.id, f"\nWELCOME TO {config.get('roomName', 'Default Room')} @{user.username}")
  
        
        random_emote = random.choice(emotes)
        emote_id = random_emote['emote']
        await self.highrise.send_emote(emote_id, user.id)
      
        promo_msg = config.get("promo_msg", {})
        ownerpromo_msg = config.get("ownerpromo_msg", {})
        extra_msg = config.get("extra_msg", {})
        if promo_msg:
            msg = promo_msg
            await self.highrise.send_whisper(user.id, msg)
      
        if extra_msg:
            msg = extra_msg
            await self.highrise.send_whisper(user.id, msg)
      
        if ownerpromo_msg:
            msg = ownerpromo_msg
            await self.highrise.send_whisper(user.id, msg)