from highrise import *
from highrise.models import *
from src.eventHandle import start, join, chat, react, message, tips


async def handle_start(self: BaseBot, session_metadata: SessionMetadata) -> None:
    try:
        await start.on_start(self, session_metadata)
    except Exception as e:
        print(f"An Error Occured: {e}")

async def handle_join(self, user: User, position: Position | AnchorPosition) -> None:
    try:
        await join.on_join(self, user, position)
    except Exception as e:
        print(f"An Error Occurred: {e}")

async def handle_chat(self: BaseBot, user: User, message: str) -> None:
    try:
        await chat.on_chat(self, user, message)
    except Exception as e:
        print(f"An Error Occured: {e}")

async def handle_reactions(self: BaseBot, user: User, reaction: Reaction, receiver: User) -> None:
    try:
        await react.on_reaction(self, user, reaction, receiver)
    except Exception as e:
        print(f"An Error Occured: {e}")

async def handle_tips(self: BaseBot, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
    try:
        await tips.on_tip(self, sender, receiver, tip)
    except Exception as e:
        print(f"An Error Occured: {e}")

async def handle_message(self: BaseBot, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
    try:
        await message.message(self, user_id, conversation_id, is_new_conversation)
    except Exception as e:
        print(f"An Error Occured: {e}")