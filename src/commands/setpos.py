from highrise import *
from highrise.models import *
from config.load_permissions import load_settings
from config.update_settings import update_coordinates

async def setpos(self: BaseBot, user: User, message: str)-> None:
    settings = load_settings()
    if settings["command_permissions"].get("setpos", False):
        room_permissions = await self.highrise.get_room_privilege(user.id)
        if room_permissions.moderator or room_permissions.designer:
            parts = message.split(" ")
            key = parts[1]

            x = 0.0
            y = 0.0
            z = 0.0
            facing = ""
            entity_id = ""
            anchor_ix = 0
            
            response = await self.highrise.get_room_users()
            for item in response.content:
                usr, position = item

                if usr.username == user.username:
                    if isinstance(position, Position):
                        # Extract the position information from Position object
                        x = position.x
                        y = position.y
                        z = position.z
                        facing = position.facing
                        entity_id = None
                        anchor_ix = None
                    elif isinstance(position, AnchorPosition):
                        # Extract the position information from AnchorPosition object
                        x = None
                        y = None
                        z = None
                        facing = None
                        entity_id = position.entity_id
                        anchor_ix = position.anchor_ix

            res = update_coordinates(key, x, y, z, facing, entity_id, anchor_ix)
            if res:
                await self.highrise.chat(f"Position for {key} updated successfully.")
            else:
                await self.highrise.chat(f"Failed to update position for {key}.")