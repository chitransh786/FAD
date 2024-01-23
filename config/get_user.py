from highrise import *
from highrise.models import *
from highrise.webapi import *

async def get_user_from_username(self, user):
    username = user[1:]
    response = await self.webapi.get_users(username = username, limit = 3, sort_order = "asc", starts_after = None, ends_before = None)

    user_id = response.users[0].user_id

    return user_id