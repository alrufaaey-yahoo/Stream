import os
from dotenv import load_dotenv

load_dotenv()

OWNER_ID = int(os.getenv("OWNER_ID", 7851734792))
API_ID = int(os.getenv("API_ID", 34179581))
API_HASH = os.getenv("API_HASH", "d1643888aaf2da525b496d9f738f3668")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8373798184:AAHAoDZKvSejuwYYbBlFBtDyiHNZGJJiOTc")
DEFAULT_RTMP_URL = "rtmps://dc4-1.rtmp.t.me/s/"
LOGGER_ID = int(os.getenv("LOGGER_ID", -1003640123116))
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://alrufaaey:engmomo@cluster0.codtlum.mongodb.net/?appName=Cluster0")
