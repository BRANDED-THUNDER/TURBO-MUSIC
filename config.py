from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/edf8f2bdc919ae8584650.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/6b26a7973dbd91a1a0fe2.jpg")

SESSION = getenv("SESSION", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Friends_chatting_Group_Sigma")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BRANDRD_BOT")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ᴛʜᴜɴᴅᴇʀ 〆 ᴍᴜꜱɪᴄ")  

FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
