from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "26064247"
# -------------------------------------------------------------
API_HASH = "c55cdb7652486811acfa038f4cda154f"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "6613874040:AAGpMxEwyhGHXHk9sTQiknZ65HZeEaF5X_4")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://deeprobot:a@cluster0.hu7q9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", "7394590844"))
SUPPORT_GRP = getenv("SUPPORT_GRP", "DEEPANSHUXD")
UPDATE_CHNL = getenv("UPDATE_CHNL", "DEEPANSHUXD")
OWNER_USERNAME = getenv("OWNER_USERNAME", "STD_DEEPANSHU")
API = getenv("API", "https://chatwithai.codesearch.workers.dev/?chat=")
