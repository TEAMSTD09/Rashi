from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "26064247"
# -------------------------------------------------------------
API_HASH = "c55cdb7652486811acfa038f4cda154f"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "6561481013:AAEV640dDQPty5Upkx-TH4To8ZjnJnkSp_c")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://chutiyapabot:a@cluster0.heiwp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", "7482534247"))
SUPPORT_GRP = getenv("SUPPORT_GRP", "TG_FRIENDSS")
UPDATE_CHNL = getenv("UPDATE_CHNL", "OK_WIN_PREDICTIONS")
OWNER_USERNAME = getenv("OWNER_USERNAME", "THE_VIP_BOY")
API = getenv("API", "https://chatwithai.codesearch.workers.dev/?chat=")
