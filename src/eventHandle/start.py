from highrise import *
from highrise.models import *
import time, asyncio
from config.load_permissions import load_settings
from config.update_settings import update_json_value
from src.eventHandle.cmdChat import read_and_process_commands
from src.commands.emoted import emoted
from src.commands.meme import meme

class start:
    start_time = time.time()

async def on_start(self: BaseBot, session_metadata: SessionMetadata) -> None:
    start_time = time.time()

    settings = load_settings()

    tasks = []

    if settings["loggers"].get("SessionMetadata", False):
        rate_limits = session_metadata.rate_limits
        formatted_rate_limits = ', '.join(
            str(value) for value in rate_limits.values())
        print(f"Bot ID: {session_metadata.user_id}\nRate Limits: {formatted_rate_limits}\nConnection ID: {session_metadata.connection_id}\nSDK Version: {session_metadata.sdk_version}")

    await update_json_value("config", "botID", session_metadata.user_id)
    await update_json_value("config", "roomName", session_metadata.room_info.room_name)


    
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

    if settings["loggers"].get("cmdChat", False):
        tasks.append(asyncio.create_task(read_and_process_commands(self)))

    if settings["command_permissions"].get("emoted", False):
        tasks.append(asyncio.create_task(emoted(self)))

    if settings["command_permissions"].get("jk&pickup", False):
        tasks.append(asyncio.create_task(meme(self)))

    if tasks:
        await asyncio.gather(*tasks)