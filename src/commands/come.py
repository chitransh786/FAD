from highrise import *
from highrise.models import *
from config.load_permissions import load_settings

async def come(self: BaseBot, user: User, message: str)-> None:
    settings = load_settings()
    if settings["command_permissions"].get("come", False):
        room_permissions = await self.highrise.get_room_privilege(user.id)
        if room_permissions.moderator or room_permissions.designer:
            response = await self.highrise.get_room_users()
            for item in response.content:
                usr, position = item
                if usr.username == user.username:
                    if isinstance(position, Position):
                        # Extract the position information
                        x = position.x
                        y = position.y
                        z = position.z
                        facing = position.facing
                    else:
                        # The user is already sitting on a chair
                        await self.highrise.send_whisper(user.id, "You are sitting on a chair, and I cannot sit over you because you are already sitting.\nSORRY!")
                        return  # Exit the function to avoid walking to the position

            await self.highrise.chat(f" @{user.username} Wait!!, I'm coming.")
            await self.highrise.walk_to(Position(x, y, z, facing))