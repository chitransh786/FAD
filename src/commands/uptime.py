from highrise import *
from highrise.models import *
import asyncio
import time
from datetime import datetime, timedelta
from src.eventHandle import start
from config.load_permissions import load_settings

async def uptime(self: BaseBot, user: User, message: str)-> None:
    settings = load_settings()
    if message.lower().startswith(f"{settings['config'].get('prefix', '')}uptime") and settings["command_permissions"].get("uptime", False):
        reply = await get_uptime(start.start.start_time)
        await self.highrise.chat(reply)
    
async def get_uptime(start_time):
    current_time = time.time()
    uptime = current_time - start_time
  
    # Convert uptime to timedelta object for easier calculations
    uptime_timedelta = timedelta(seconds=uptime)
  
    # Extract different time components
    days = uptime_timedelta.days
    hours, remainder = divmod(uptime_timedelta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
  
    # Create a human-readable uptime string
    uptime_string = await format_time_component(days, "days")
    uptime_string += " " + await format_time_component(hours, "hours")
    uptime_string += " " + await format_time_component(minutes, "minutes")
    uptime_string += " " + await format_time_component(seconds, "seconds")
    uptime_string = uptime_string.strip()
  
    return f"Uptime: {uptime_string}"

async def format_time_component(value, unit):
    if value > 0:
        if value == 1:
            unit = unit[:-1]  # Remove plural form if the value is 1
        return f"{value} {unit}"
    return ""
  
