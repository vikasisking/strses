from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "21131430"))
API_HASH = environ.get("API_HASH", "f69348955d470bc6b5f34116e054785e")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7900999963")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://vdhorroranimation898:zs4A9PSlOGxscRnh@cluster0.apsfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
