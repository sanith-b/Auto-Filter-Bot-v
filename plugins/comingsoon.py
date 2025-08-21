import requests
import random
import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pymongo import MongoClient

# 🔑 Replace with your TMDB API Key
TMDB_API_KEY = "90dde61a7cf8339a2cff5d805d5597a9"

# 🔗 MongoDB Connection
MONGODB_URI = "mongodb+srv://botadmin:1sQZEOQ7y3SSPNV3@kdramabot.00xhgvx.mongodb.net/?retryWrites=true&w=majority&appName=kdramabot"
DB_NAME = "kdramabot"

# Connect to MongoDB
mongo_client = MongoClient(MONGODB_URI)
db = mongo_client[DB_NAME]
reminders_collection = db["reminders"]

# 🎬 Fetch upcoming K-Dramas from TMDB
def get_coming_soon():
    today = datetime.date.today().strftime("%Y-%m-%d")
    url = (
        f"https://api.themoviedb.org/3/discover/tv"
        f"?api_key={TMDB_API_KEY}"
        f"&with_origin_country=KR"
        f"&sort_by=first_air_date.asc"
        f"&first_air_date.gte={today}"
        f"&language=en-US&page=1"
    )

    response = requests.get(url)
    data = response.json()

    dramas = []
    for item in data.get("results", []):
        drama = {
            "id": item.get("id"),
            "title": item.get("name"),
            "release_date": item.get("first_air_date"),
            "overview": item.get("overview", "No description available."),
            "poster": f"https://image.tmdb.org/t/p/w500{item['poster_path']}" if item.get("poster_path") else None
        }
        dramas.append(drama)

    return dramas


# 🎬 Get trailer link for a drama
def get_trailer(tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}/videos?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url).json()

    for video in response.get("results", []):
        if video["site"] == "YouTube" and video["type"] == "Trailer":
            return f"https://youtu.be/{video['key']}"
    return None


# ⚡ Command Handler
@Client.on_message(filters.command("comingsoon"))
async def comingsoon_handler(client, message):
    dramas = get_coming_soon()

    if not dramas:
        await message.reply_text("🌸 No upcoming K-Dramas found at the moment!")
        return

    for drama in dramas[:5]:  # Show only first 5 upcoming dramas
        trailer = get_trailer(drama["id"])
        release_date = drama["release_date"] or "TBA"
        days_left = ""
        if release_date and release_date != "TBA":
            try:
                rd = datetime.datetime.strptime(release_date, "%Y-%m-%d").date()
                diff = (rd - datetime.date.today()).days
                if diff >= 0:
                    days_left = f"\n⏳ {diff} days left!"
            except:
                pass

        caption = (
            f"🎬 <b>{drama['title']}</b>\n"
            f"📅 Release Date: {release_date}{days_left}\n\n"
            f"✨ {drama['overview']}"
        )

        buttons = []
        if trailer:
            buttons.append([InlineKeyboardButton("▶️ Watch Trailer", url=trailer)])
        buttons.append([InlineKeyboardButton("🔔 Remind Me", callback_data=f"remind_{drama['id']}_{drama['title']}")])

        await message.reply_photo(
            drama["poster"] if drama["poster"] else "https://i.ibb.co/6NfYQ7c/kdrama.jpg",
            caption=caption,
            reply_markup=InlineKeyboardMarkup(buttons)
        )


# ⚡ Callback Handler for "Remind Me"
@Client.on_callback_query(filters.regex(r"^remind_"))
async def remind_me(client, query):
    data_parts = query.data.split("_")
    drama_id = data_parts[1]
    drama_title = "_".join(data_parts[2:])  # Handle titles with underscores
    
    user_id = query.from_user.id
    username = query.from_user.username or f"user_{user_id}"
    
    # Check if reminder already exists
    existing_reminder = reminders_collection.find_one({
        "user_id": user_id,
        "drama_id": drama_id
    })
    
    if existing_reminder:
        await query.answer("🔔 You already set a reminder for this drama!", show_alert=True)
        return
    
    # Save reminder to MongoDB
    reminder_data = {
        "user_id": user_id,
        "username": username,
        "drama_id": drama_id,
        "drama_title": drama_title,
        "reminder_date": datetime.datetime.now(),
        "notified": False
    }
    
    reminders_collection.insert_one(reminder_data)
    
    await query.answer(f"🔔 Reminder set for {drama_title.replace('_', ' ')}! We'll notify you when it's released.", show_alert=True)


# Function to check and send reminders (to be called periodically)
async def check_and_send_reminders(client):
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # Get dramas released today
    url = (
        f"https://api.themoviedb.org/3/discover/tv"
        f"?api_key={TMDB_API_KEY}"
        f"&with_origin_country=KR"
        f"&first_air_date={today}"
        f"&language=en-US&page=1"
    )
    
    response = requests.get(url)
    data = response.json()
    
    released_dramas = data.get("results", [])
    
    for drama in released_dramas:
        drama_id = str(drama.get("id"))
        drama_title = drama.get("name")
        
        # Find all users who want reminders for this drama
        reminders = reminders_collection.find({
            "drama_id": drama_id,
            "notified": False
        })
        
        for reminder in reminders:
            try:
                user_id = reminder["user_id"]
                message_text = (
                    f"🎉 Good news! <b>{drama_title}</b> is released today!\n\n"
                    f"Enjoy watching! 🍿"
                )
                
                await client.send_message(user_id, message_text)
                
                # Mark as notified
                reminders_collection.update_one(
                    {"_id": reminder["_id"]},
                    {"$set": {"notified": True}}
                )
            except Exception as e:
                print(f"Failed to send reminder to user {user_id}: {e}")
