### ~ Aitech config : aichatbot

from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "")) # get my.telegram.org/apps
API_HASH = getenv("API_HASH", "") # get my.telegram.org/apps
OWNER_ID = int(getenv("OWNER_ID", "1924693109")) # Owner ID: get @MissRose_bot /info ...
STRING_SESSION = getenv("STRING_SESSION", "") # Pyrogram v2 String Session: help @aiteknoloji
MONGO_URL = getenv("MONGO_URL", "") # Free mongo db url: "mongodb+srv://shikhar:shikhar@cluster0.6xzlh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
SUPPORT_GRP = getenv("SUPPORT_GRP", "aitsupport")
UPDATE_CHNL = getenv("UPDATE_CHNL", "aitbots")
OWNER_USERNAME = getenv("OWNER_USERNAME", "codmastervip") # Owner username "@" without 

# Random Start Images
IMG = [
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
]


# Random Stickers
STICKER = [
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
]

# Random Emojios
EMOJIOS = [
    "😍",
    "🌹",
    "😔",
    "❤️",
    "😻",
    "😝",
    "😁",
    "👀",
    "🇦🇿",
    "🤣",
    "🙈",
    "🤨",
    "🥹",
]
