import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", "14766829"))
    API_HASH = os.environ.get("API_HASH" "cfaca926290f395a7404927ccb88422d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6540003079:AAFsSYmu2QvD9Hyiy3SHycOO_1ydGElgbT8")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5281368582"))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1001956308914")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://rde33242:appleiphone@realme.7n9loel.mongodb.net/?retryWrites=true&w=majority")
