from highrise import *
from highrise.models import *
import random, asyncio
from config.load_emotes import load_emotes_data

async def emoted(self: BaseBot):

    emotes = load_emotes_data()
    while True:
      duration = 0
      try:
          random_emote = random.choice(emotes)
          emote_id = random_emote['emote']
          duration = random_emote.get('duration', 0)
          await self.highrise.send_emote(emote_id)
      except:
          await self.highrise.chat("An error occurred while performing the emote.")
          return

      sleep_duration = float(duration) if duration is not None else 10.0
      await asyncio.sleep(sleep_duration)