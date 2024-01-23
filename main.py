from highrise import *
from highrise.models import *
from src.handlers.handleEvents import handle_start, handle_chat, handle_join, handle_reactions, handle_tips, handle_message


class Bot(BaseBot):

    def __init__(self):
        super().__init__()
    
    async def on_start(self: BaseBot, session_metadata: SessionMetadata) -> None:
        await handle_start(self, session_metadata)
    
    async def on_chat(self: BaseBot, user: User, message: str) -> None:
        await handle_chat(self, user, message)
    
    async def on_user_join(self: BaseBot, user: User, position: Position | AnchorPosition) -> None:
        await handle_join(self, user, position)
    
    async def on_tip(self: BaseBot, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
        await handle_tips(self, sender, receiver, tip)
    
    async def on_reaction(self: BaseBot, user: User, reaction: Reaction, receiver: User) -> None:
        await handle_reactions(self, user, reaction, receiver)
    
    async def on_message(self: BaseBot, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
        await handle_message(self, user_id, conversation_id, is_new_conversation)
    