import requests
import random
import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pymongo import MongoClient

# TMDB API Key
TMDB_API_KEY = "90dde61a7cf8339a2cff5d805d5597a9"

# MongoDB setup
MONGO_URI = "mongodb+srv://botadmin:1sQZEOQ7y3SSPNV3@kdramabot.00xhgvx.mongodb.net/?retryWrites=true&w=majority&appName=kdramabot"
client_db = MongoClient(MONGO_URI)
db = client_db['kdramabot']
reminders_collection = db['reminders']

# Fetch upcoming K-Dramas from TMDB
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
            "type": "TV Series",
            "release_date": item.get("first_air_date"),
            "overview": item.get("overview", "No description available."),
            "poster": f"https://image.tmdb.org/t/p/w500{item['poster_path']}" if item.get("poster_path") else None
        }
        dramas.append(drama)
    return dramas

# Get trailer link for a drama
def get_trailer(tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}/videos?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url).json()

    for video in response.get("results", []):
        if video["site"] == "YouTube" and video["type"] == "Trailer":
            return f"https://youtu.be/{video['key']}"
    return None

# Save reminder to MongoDB
def save_reminder(user_id, drama):
    reminders_collection.update_one(
        {"user_id": user_id},
        {"$addToSet": {"dramas": drama}},
        upsert=True
    )

# Command Handler
@Client.on_message(filters.command("comingsoon"))
async def comingsoon_handler(client, message):
    dramas = get_coming_soon()
    if not dramas:
        await message.reply_text("🌸 No upcoming K-Dramas found at the moment!")
        return

    for drama in dramas[:5]:
        trailer = get_trailer(drama["id"])
        release_date = drama["release_date"] or "TBA"
        drama_type = drama.get("type", "Unknown")
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
            f"🎬 <b>{drama['title']}</b> ({drama_type})\n"
            f"📅 Release Date: {release_date}{days_left}\n\n"
            f"✨ {drama['overview']}"
        )

        buttons = []
        if trailer:
            buttons.append([InlineKeyboardButton("▶️ Watch Trailer", url=trailer)])
        buttons.append([InlineKeyboardButton("🔔 Remind Me", callback_data=f"remind_{drama['id']}")])

        await message.reply_photo(
            drama["poster"] if drama["poster"] else "https://i.ibb.co/6NfYQ7c/kdrama.jpg",
            caption=caption,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

# Callback Handler for "Remind Me"
@Client.on_callback_query(filters.regex(r"^remind_"))
async def remind_me(client, query):
    drama_id = query.data.split("_")[1]
    user_id = query.from_user.id
    drama_title = "Unknown Title"
    drama_type = "Unknown"

    # Try to find the drama title from the last fetched dramas
    for drama in get_coming_soon():
        if str(drama['id']) == drama_id:
            drama_title = drama['title']
            drama_type = drama.get('type', 'Unknown')
            break

    save_reminder(user_id, {"id": drama_id, "title": drama_title, "type": drama_type})
    await query.answer(f"🔔 Reminder set for {drama_title} ({drama_type})!", show_alert=True)
