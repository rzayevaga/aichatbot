from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 18052289))
API_HASH = getenv("API_HASH", "552525f45a3066fee54ca7852235c19c")
OWNER_ID = int(getenv("OWNER_ID", "1924693109"))
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "aitsupport")
UPDATE_CHNL = getenv("UPDATE_CHNL", "aitbots")
OWNER_USERNAME = getenv("OWNER_USERNAME", "codmastervip")

# Random Start Images
IMG = [
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
]


# Random Stickers
STICKER = [
    "https://t.me/addstickers/TheCoin",
    "https://t.me/addstickers/Webp_14",
    "https://t.me/addstickers/Webp_14",
]


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
