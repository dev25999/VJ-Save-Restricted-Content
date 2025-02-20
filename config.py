import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "18331175"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e1c809381b2515aa7cbc663a232e4852")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "689720245"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://devarshisaksena9:voYrn0luBeKANxj4@cluster0.h1xod.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
