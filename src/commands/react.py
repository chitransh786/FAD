from highrise import *
from highrise.models import *
from highrise.webapi import *
from config.get_user import get_user_from_username
from config.load_permissions import load_settings
import asyncio

async def react(self, user, parts) -> None:
    count = 1  # Default count
    reaction_type = parts[0]
    target_user = user.id
    settings = load_settings()
    bot_id = settings["config"].get("botID", "")
    
    if len(parts) == 2:
        room_permissions = await self.highrise.get_room_privilege(user.id)
        if room_permissions.moderator or room_permissions.designer:
            if parts[1] == 'all':
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the user objects
              userIds = [user.id for user in users if user.id != bot_id]
              tasks = []
              for id in userIds:
                  task = asyncio.create_task(self.highrise.react(reaction_type, id))
                  tasks.append(task)
    
              return
                
            # Check if it's a count or a username
            try:
                count = int(parts[1])
            except ValueError:
                target_user = await get_user_from_username(self, parts[1])

    elif len(parts) == 3:
        target_user = await get_user_from_username(self, parts[1])
        count = int(parts[2])
      

    for _ in range(count):
        await self.highrise.react(reaction_type, target_user)