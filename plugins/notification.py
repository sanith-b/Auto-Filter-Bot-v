from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pymongo import MongoClient

# MongoDB setup
MONGO_URI = "mongodb+srv://botadmin:1sQZEOQ7y3SSPNV3@kdramabot.00xhgvx.mongodb.net/?retryWrites=true&w=majority&appName=kdramabot"
client_db = MongoClient(MONGO_URI)
db = client_db['kdramabot']
favorites_collection = db['favorites']

# Pyrogram Client
app = Client("kdrama_bot")

# Callback Handler for Favorites
@app.on_callback_query(filters.regex(r"^favorite_"))
async def favorite_drama(client, query):
    drama_id = query.data.split("_")[1]
    user_id = query.from_user.id
    drama_title = "Unknown Title"
    drama_type = "Unknown"

    # Replace with your function to get drama details
    from comingsoon_kdrama import get_coming_soon
    for drama in get_coming_soon():
        if str(drama['id']) == drama_id:
            drama_title = drama['title']
            drama_type = drama.get('type', 'Unknown')
            break

    # Save to MongoDB
    favorites_collection.update_one(
        {"user_id": user_id},
        {"$addToSet": {"dramas": {"id": drama_id, "title": drama_title, "type": drama_type}}},
        upsert=True
    )

    await query.answer(f"❤️ Added {drama_title} ({drama_type}) to your Favorites!", show_alert=True)

# Command to View Favorites
@app.on_message(filters.command("myfavorites"))
async def my_favorites(client, message):
    user_id = message.from_user.id
    data = favorites_collection.find_one({"user_id": user_id})

    if not data or not data.get("dramas"):
        await message.reply_text("🌸 Your Favorites list is empty!")
        return

    msg = "💖 Your Favorites:\n\n"
    for drama in data["dramas"]:
        msg += f"🎬 {drama['title']} ({drama['type']})\n"

    await message.reply_text(msg)
