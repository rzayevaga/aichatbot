from pyrogram import filters, Client
from pyrogram.types import Message

from Aitech import OWNER, Rzayev
from Aitech.database.chats import get_served_chats
from Aitech.database.users import get_served_users


@Rzayev.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""Ümumi Statistika {(await cli.get_me()).mention} :

➻ **Söhbətlər :** {chats}
➻ **istifadəçilər :** {users}"""
    )
