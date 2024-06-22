from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Aitech import OWNER
from Aitech import Rzayev

DEV_OP = [
    [
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", user_id=OWNER),
        InlineKeyboardButton(text="Dəstək", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="Məni Qrupa Əlavə et",
            url=f"https://t.me/{Rzayev.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="Kömək & Əmrlər", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="Haqqımda", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="Məni Qrupa əlavə et",
            url=f"https://t.me/{Rzayev.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="Bağla",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="Geri", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="ChatBot", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="Özəlliklər", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="Geri", callback_data="BACK"),
        InlineKeyboardButton(text="Bağla", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="Bağla", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="Enable", callback_data=f"addchat"),
        InlineKeyboardButton(text="Disable", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="Tezliklə", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="Geri", callback_data="SBACK"),
        InlineKeyboardButton(text="Bağla", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="Geri", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="Bağla", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="Kömək", callback_data="HELP"),
        InlineKeyboardButton(text="Bağla", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="Kömək", url=f"https://t.me/{Rzayev.username}?start=help"
        ),
        InlineKeyboardButton(text="Bağla", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="Dəstək", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="Kömək", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", user_id=OWNER),
    ],
    [
        InlineKeyboardButton(text="Kanal", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="Geri", callback_data="BACK"),
    ],
]
