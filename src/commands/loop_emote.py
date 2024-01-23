from highrise import *
from highrise.models import *
import asyncio, time
from asyncio import Task
from config.load_emotes import emotes


async def loop(self: BaseBot, user: User, message: str) -> None:
    # Defining the loop_emote method locally so it cann't be accessed from the command handler.
    async def loop_emote(self: BaseBot, user: User, emote_name: str) -> None:
        emote_id = ""
        duration = 0
        for emote_data in emotes:
            cmd = emote_data['command']
            emote = emote_data['emote']
            if cmd.lower() == emote_name.lower():
                emote_id = emote
                duration = emote_data.get('duration', 0)
                break
        if emote_id == "":
            await self.highrise.chat("Invalid emote")
            return
        user_position = None
        user_in_room = False
        room_users = (await self.highrise.get_room_users()).content
        for room_user, position in room_users:
            if room_user.id == user.id:
                user_position = position
                start_position = position
                user_in_room = True
                break
        if user_position == None:
            await self.highrise.chat("User not found")
            return
        await self.highrise.chat(f"@{user.username} is looping {emote_name}")

        while True:
            try:
                await self.highrise.send_emote(emote_id, user.id)
            except:
                await self.highrise.chat(f"Sorry, @{user.username}, this emote isn't free or you don't own it.")
                return
              
            sleep_duration = float(duration) if duration is not None else 10.0
            await asyncio.sleep(sleep_duration)
          
            room_users = (await self.highrise.get_room_users()).content
            user_in_room = False
            for room_user, position in room_users:
              if room_user.id == user.id:
                  user_in_room = True
                  break
                  
            if user_in_room == False:
                break
    try:
        splited_message = message.split(" ")
        # The emote name is every string after the first one
        emote_name = " ".join(splited_message[1:])
    except:
        await self.highrise.chat("Invalid command format. Please use 'loop <emote name>.")
        return
    else:   
        taskgroup = self.highrise.tg
        task_list : list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_name() == user.username:
                # Removes the task from the task group
                task.cancel()

        room_users = (await self.highrise.get_room_users()).content
        user_list  = []
        for room_user, pos in room_users:
            user_list.append(room_user.username)

        taskgroup.create_task(coro=loop_emote(self, user, emote_name))
        task_list : list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_coro().__name__ == "loop_emote" and not (task.get_name() in user_list):
                task.set_name(user.username)

async def stop_loop(self: BaseBot, user: User, message: str) -> None:
        taskgroup = self.highrise.tg
        task_list : list[Task] = list(taskgroup._tasks)
        for task in task_list:
            print(task.get_name())
            if task.get_name() == user.username:
                task.cancel()
                await self.highrise.chat(f"Stopping your emote loop, {user.username}!")
                return
        await self.highrise.chat(f"You're not looping any emotes, {user.username}")
        return