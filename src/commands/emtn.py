from highrise import *
from highrise.models import *
from config.load_permissions import load_settings
import asyncio

async def emoting(self: BaseBot, match, cmd, emote, user: User, message: str)-> None:
    if match:
        username = match.group(1)
        fetch = await self.highrise.get_room_users()
        index = next((i for i, item in enumerate(fetch.content) if item[0].username == username), -1)
        if index != -1:
            target = fetch.content[index][0]
            task1 = asyncio.create_task(self.highrise.send_emote(emote, user.id))
            task2 = asyncio.create_task(self.highrise.send_emote(emote, target.id))
            await asyncio.gather(task1, task2)
        return
    elif message.strip().lower().startswith(cmd + " all"):
        room_permissions = await self.highrise.get_room_privilege(user.id)
        if room_permissions.moderator or room_permissions.designer:
            response = await self.highrise.get_room_users()
            users = [content[0] for content in response.content]  # Extract the user objects
            userIds = [user.id for user in users]  # Extract the user IDs
            tasks = []
            for id in userIds:
                task = asyncio.create_task(self.highrise.send_emote(emote, id))
                tasks.append(task)
            # Gather all the tasks together and wait for them to complete
            await asyncio.gather(*tasks)
        return

    elif message.startswith(cmd):
        await self.highrise.send_emote(emote, user.id)