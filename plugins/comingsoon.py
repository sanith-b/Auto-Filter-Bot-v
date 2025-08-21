import requests
from pyrogram import filters,Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pymongo import MongoClient
import datetime

# ===== CONFIG =====
TMDB_API_KEY = "90dde61a7cf8339a2cff5d805d5597a9"
MONGO_URI = "mongodb+srv://botadmin:1sQZEOQ7y3SSPNV3@kdramabot.00xhgvx.mongodb.net/?retryWrites=true&w=majority&appName=kdramabot"
DB_NAME = "kdramabot"

# ===== INIT =====
client_db = MongoClient(MONGO_URI)[DB_NAME]
reminders = client_db["reminders"]
scheduler = AsyncIOScheduler()
DRAMA_CACHE = {}

# ===== FETCH COMING SOON =====
def fetch_comingsoon():
    url = f"https://api.themoviedb.org/3/discover/tv?api_key={TMDB_API_KEY}&language=ko-KR&sort_by=popularity.desc&with_origin_country=KR&first_air_date.gte={datetime.date.today()}"
    res = requests.get(url).json()
    return res.get("results", [])[:5]

# ===== REGISTER PLUGIN =====
def register_comingsoon(bot):

    @bot.on_message(filters.command("comingsoon"))
    async def comingsoon_handler(client, message):
        dramas = fetch_comingsoon()
        if not dramas:
            return await message.reply("No upcoming dramas found.")

        buttons = []
        for drama in dramas:
            DRAMA_CACHE[str(drama['id'])] = drama
            buttons.append([InlineKeyboardButton(drama['name'], callback_data=f"drama_{drama['id']}")])

        await message.reply("📺 Coming Soon K-Dramas:", reply_markup=InlineKeyboardMarkup(buttons))

    @bot.on_callback_query(filters.regex(r"^drama_"))
    async def drama_details(client, query: CallbackQuery):
        drama_id = query.data.split("_")[1]
        drama = DRAMA_CACHE.get(drama_id)
        if not drama:
            return await query.answer("Drama details expired. Use /comingsoon again.", show_alert=True)

        url = f"https://api.themoviedb.org/3/tv/{drama_id}?api_key={TMDB_API_KEY}&language=ko-KR&append_to_response=videos"
        drama_full = requests.get(url).json()

        title = drama_full.get("name")
        overview = drama_full.get("overview", "No description.")
        release_date = drama_full.get("first_air_date", "?")
        poster = f"https://image.tmdb.org/t/p/w500{drama_full.get('poster_path')}" if drama_full.get('poster_path') else None

        trailer_key = None
        for v in drama_full.get("videos", {}).get("results", []):
            if v["type"] == "Trailer" and v["site"] == "YouTube":
                trailer_key = v["key"]
                break
        trailer_url = f"https://youtube.com/watch?v={trailer_key}" if trailer_key else None

        buttons = [[InlineKeyboardButton("🔔 Remind Me", callback_data=f"remind_{drama_id}_{release_date}")]]
        if trailer_url:
            buttons.append([InlineKeyboardButton("🎬 Watch Trailer", url=trailer_url)])

        caption = f"<b>{title}</b>\n📅 Release: {release_date}\n\n{overview}"

        if poster:
            await query.message.reply_photo(poster, caption=caption, reply_markup=InlineKeyboardMarkup(buttons))
        else:
            await query.message.reply(caption, reply_markup=InlineKeyboardMarkup(buttons))

        await query.answer()

    @bot.on_callback_query(filters.regex(r"^remind_"))
    async def set_reminder(client, query: CallbackQuery):
        parts = query.data.split("_")
        drama_id = parts[1]
        release_date = parts[2]
        user_id = query.from_user.id

        reminders.update_one({"user_id": user_id, "drama_id": drama_id},
                             {"$set": {"user_id": user_id, "drama_id": drama_id, "release_date": release_date}}, upsert=True)

        await query.answer("Reminder set! You will be notified on release day.", show_alert=True)

# ===== SCHEDULED REMINDER =====
def start_scheduler(bot_client):
    async def check_reminders():
        today = datetime.date.today().isoformat()
        docs = reminders.find({"release_date": today})
        for doc in docs:
            try:
                drama_id = doc['drama_id']
                user_id = doc['user_id']
                url = f"https://api.themoviedb.org/3/tv/{drama_id}?api_key={TMDB_API_KEY}&language=ko-KR"
                drama = requests.get(url).json()
                title = drama.get("name")
                poster = f"https://image.tmdb.org/t/p/w500{drama.get('poster_path')}" if drama.get('poster_path') else None
                caption = f"🔔 <b>Release Today!</b>\n🎬 {title} is releasing today!"

                if poster:
                    await bot_client.send_photo(user_id, poster, caption=caption)
                else:
                    await bot_client.send_message(user_id, caption)

                reminders.delete_one({"_id": doc['_id']})
            except Exception as e:
                print(f"Failed to send reminder to {doc['user_id']}: {e}")

    scheduler.add_job(check_reminders, 'cron', hour=7, minute=0)
    scheduler.start()
