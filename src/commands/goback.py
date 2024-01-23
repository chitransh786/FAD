from highrise import *
from highrise.models import *
from config.load_permissions import load_settings

async def goback(self: BaseBot, user: User, message: str)-> None:
    settings = load_settings()
    if settings["command_permissions"].get("goback", False):
        room_permissions = await self.highrise.get_room_privilege(user.id)
        if room_permissions.moderator or room_permissions.designer:
            config = settings["config"]
            coordinates = config.get("coordinates", {})

            x = coordinates.get("x")
            y = coordinates.get("y")
            z = coordinates.get("z")
            facing = coordinates.get("facing")
            entity_id = coordinates.get("entity_id")
            anchor_ix = coordinates.get("anchor_ix")

            # Check which data is available and act accordingly
            if entity_id is not None and anchor_ix is not None:
                # Use AnchorPosition if entity_id and anchor_ix are provided
                await self.highrise.walk_to(AnchorPosition(entity_id, anchor_ix))
            elif x is not None and y is not None and z is not None and facing is not None:
                # Use Position if x, y, z, and facing are provided
                await self.highrise.walk_to(Position(x, y, z, facing))