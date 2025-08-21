import datetime
import asyncio
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from motor.motor_asyncio import AsyncIOMotorClient

# ---------------- CONFIG ----------------
TMDB_API_KEY = "90dde61a7cf8339a2cff5d805d5597a9"
MONGO_URI = "mongodb+srv://botadmin:1sQZEOQ7y3SSPNV3@kdramabot.00xhgvx.mongodb.net/?retryWrites=true&w=majority&appName=kdramabot"
DB_NAME = "kdramabot"

# ---------------- DATABASE ----------------
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

comingsoon_col = db.comingsoon
watchlist_col = db.watchlist
subscriptions_col = db.subscriptions

# ---------------- HELPERS ----------------
async def fetch_coming_soon():
    """Fetch upcoming K-Dramas from TMDb with cast, genres, trailer"""
    today = datetime.date.today().strftime("%Y-%m-%d")
    url = (
        f"https://api.themoviedb.org/3/discover/tv"
        f"?api_key={TMDB_API_KEY}"
        f"&with_origin_country=KR"
        f"&sort_by=first_air_date.asc"
        f"&first_air_date.gte={today}"
        f"&language=en-US&page=1"
    )
    res = requests.get(url).json()
    genres_list = requests.get(f"https://api.themoviedb.org/3/genre/tv/list?api_key={TMDB_API_KEY}&language=en-US").json().get("genres", [])
    genre_dict = {g["id"]: g["name"] for g in genres_list}

    for item in res.get("results", []):
        drama_id = str(item.get("id"))

        # Cast
        cast_res = requests.get(f"https://api.themoviedb.org/3/tv/{drama_id}/credits?api_key={TMDB_API_KEY}").json()
        cast = [c["name"] for c in cast_res.get("cast", [])[:5]]

        # Genres
        genres = [genre_dict.get(gid, str(gid)) for gid in item.get("genre_ids", [])]

        # Trailer
        trailer_res = requests.get(f"https://api.themoviedb.org/3/tv/{drama_id}/videos?api_key={TMDB_API_KEY}&language=en-US").json()
        trailer = ""
        for vid in trailer_res.get("results", []):
            if vid.get("site") == "YouTube" and vid.get("type") == "Trailer":
                trailer = f"https://youtu.be/{vid['key']}"
                break

        await comingsoon_col.update_one(
            {"_id": drama_id},
            {"$set": {
                "title": item.get("name"),
                "release_date": item.get("first_air_date"),
                "overview": item.get("overview", "No description."),
                "poster": f"https://image.tmdb.org/t/p/w500{item['poster_path']}" if item.get("poster_path") else None,
                "cast": cast,
                "genre": genres,
                "trailer": trailer
            }},
            upsert=True
        )

def drama_buttons(drama):
    buttons = []
    if drama.get("trailer"):
        buttons.append([InlineKeyboardButton("▶️ Watch Trailer", url=drama["trailer"])])
    buttons.append([
        InlineKeyboardButton("➕ Add to Watchlist", callback_data=f"watchlist:{drama['_id']}"),
        InlineKeyboardButton("🔔 Subscribe", callback_data=f"subscribe:{drama['_id']}")
    ])
    return InlineKeyboardMarkup(buttons)

def format_drama_caption(drama):
    release_date = drama.get("release_date") or "TBA"
    days_left = ""
    if release_date != "TBA":
        try:
            rd = datetime.datetime.strptime(release_date, "%Y-%m-%d").date()
            diff = (rd - datetime.date.today()).days
            if diff >= 0:
                days_left = f"\n⏳ {diff} days left!"
        except:
            pass
    caption = (
        f"🎬 <b>{drama['title']}</b>\n"
        f"📅 Release Date: {release_date}{days_left}\n"
        f"⭐ Genres: {', '.join(drama.get('genre', []))}\n"
        f"🎭 Cast: {', '.join(drama.get('cast', []))}\n\n"
        f"✨ {drama.get('overview')}"
    )
    return caption

# ---------------- COMMAND ----------------
@Client.on_message(filters.command("comingsoon"))
async def comingsoon_handler(client, message):
    await fetch_coming_soon()
    await asyncio.sleep(1)
    dramas = await comingsoon_col.find().sort("release_date", 1).to_list(length=5)

    if not dramas:
        await message.reply_text("🌸 No upcoming K-Dramas found!")
        return

    for drama in dramas:
        await message.reply_photo(
            drama.get("poster") or "https://i.ibb.co/6NfYQ7c/kdrama.jpg",
            caption=format_drama_caption(drama),
            reply_markup=drama_buttons(drama)
        )

# ---------------- CALLBACKS ----------------
@Client.on_callback_query(filters.regex(r"^watchlist:"))
async def watchlist_callback(client, query):
    drama_id = query.data.split(":")[1]
    user_id = query.from_user.id
    await watchlist_col.update_one(
        {"user_id": user_id, "drama_id": drama_id},
        {"$set": {"user_id": user_id, "drama_id": drama_id}},
        upsert=True
    )
    await query.answer("➕ Added to your watchlist!", show_alert=True)

@Client.on_callback_query(filters.regex(r"^subscribe:"))
async def subscribe_callback(client, query):
    drama_id = query.data.split(":")[1]
    user_id = query.from_user.id
    await subscriptions_col.update_one(
        {"user_id": user_id, "drama_id": drama_id},
        {"$set": {"user_id": user_id, "drama_id": drama_id}},
        upsert=True
    )
    await query.answer("🔔 You are subscribed! You'll get notified on release day.", show_alert=True)

# ---------------- NOTIFICATIONS ----------------
async def notify_subscribers():
    """Send notifications to subscribers daily"""
    while True:
        today = datetime.date.today().strftime("%Y-%m-%d")
        dramas_today = await comingsoon_col.find({"release_date": today}).to_list(length=50)

        for drama in dramas_today:
            subscribers = await subscriptions_col.find({"drama_id": drama["_id"]}).to_list(length=50)
            for sub in subscribers:
                try:
                    await BOT.send_message(
                        chat_id=sub["user_id"],
                        text=f"🎉 <b>{drama['title']}</b> is released today!\nWatch here: {drama.get('trailer','')}",
                        disable_web_page_preview=False
                    )
                except:
                    continue

        await asyncio.sleep(86400)  # run once daily
