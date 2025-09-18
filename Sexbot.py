from telethon import TelegramClient, events
from pymongo import MongoClient
from datetime import datetime

# ========= CONFIG =========
API_ID = 24526311   # apna API ID dalen
API_HASH = "717d5df262e474f88d86c537a787c98d"  # apna API Hash dalen
SESSION = "BQF2PecANAmsjfKJkBv-PwZxQvinq0a7lcJ-6KCdyu13xnl8jeDV7YR9gk20ifB2M_7H2XqqUQMH0OAab9SXzfFqepsXHARqnp8JN7Iplo_5Odzwe6n5NBCFOyVP4Y3FGSdEQ4Y8UTM3VmCxTk8Jur_h9lCIKgxtLapFiiaYwgLwKWfP6W3XfsOs33FhjTEpHI8AOmZtqO4f5aAf3_2Mi032AHXKBDuzRqioX8RcG7JjYsjt-e8qnSudSpL20USBzR1FhGsYZjUx7W9_uPB7wjNH0P_6I3zJyynGPgdqIzkBi3sdZ2gRtgk7D-63t-jMbYuXIu5OfM6IZfCior4CVvRPu79nawAAAAHwVWW1AA"

# ========= MONGO DB CONFIG =========
MONGO_URI = "mongodb+srv://afzal99550:afzal99550@cluster0.aqmbh9q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "BanallBot"

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
users_col = db["users"]

# ========= START CLIENT =========
client = TelegramClient(SESSION, API_ID, API_HASH)

# ========= EVENT HANDLER =========
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:  # sirf DM me chalega
        text = event.raw_text.strip().lower()

        # Save to MongoDB
        user_data = {
            "user_id": event.sender_id,
            "username": (await event.get_sender()).username,
            "message": event.raw_text,
            "date": datetime.utcnow()
        }
        users_col.insert_one(user_data)

        if text in ["desi 69", "desi69", "desi-69", "desi_69"]:
            await event.respond(
                "Hlo I'm King",
                file="https://i.ibb.co/gFmGLHp3/x.jpg"
            )
        else:
            await event.respond("Owner is busy.")

# ========= RUN =========
print("Userbot running...")
client.start()
client.run_until_disconnected()
