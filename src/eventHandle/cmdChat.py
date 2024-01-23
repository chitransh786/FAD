from highrise import *
from highrise.models import *
import asyncio

async def read_and_process_commands(self: BaseBot):
    while True:
        command = await asyncio.get_event_loop().run_in_executor(None, input)
        if command == "exit":
            break
        # Process the command here, you can call appropriate functions or perform actions based on the command
        await self.highrise.chat(command)
