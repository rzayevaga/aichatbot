from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 18052289))
API_HASH = getenv("API_HASH", "552525f45a3066fee54ca7852235c19c")
OWNER_ID = int(getenv("OWNER_ID", "1924693109"))
STRING_SESSION = getenv("STRING_SESSION", "")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://shikhar:shikhar@cluster0.6xzlh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
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
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
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
