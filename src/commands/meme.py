from highrise import *
from highrise.models import *
import random, asyncio
from config.randomJOKEPICKUP import get_random_joke_or_pickup_line

async def meme(self):
    while True:
        try:
            category = random.choice(["jokes", "pickup_lines"])
            message = get_random_joke_or_pickup_line('jokes')
            await self.highrise.chat(message)

            await asyncio.sleep(30)
        except:
            await self.highrise.chat("An error occurred while sending meme.")
            return