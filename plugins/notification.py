import asyncio
from pyrogram import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pymongo import MongoClient
import datetime

# MongoDB setup
MONGO_URI = "mongodb+srv://botadmin:1sQZEOQ7y3SSPNV3@kdramabot.00xhgvx.mongodb.net/?retryWrites=true&w=majority&appName=kdramabot"
client_db = MongoClient(MONGO_URI)
db = client_db['kdramabot']
subscriptions_collection = db['subscriptions']

# TMDB API Key
TMDB_API_KEY = "90dde61a7cf8339a2cff5d805d5597a9"

# Pyrogram Client setup

# Fetch upcoming K-Dramas from TMDB
def get_coming_soon():
    import requests
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

# Send Digest Function
async def send_digest():
    async with app:
        for sub in subscriptions_collection.find({"enabled": True}):
            chat_id = sub["chat_id"]
            dramas = get_coming_soon()

            for drama in dramas[:5]:
                caption = (
                    f"🎬 <b>{drama['title']}</b> ({drama['type']})\n"
                    f"📅 Release Date: {drama['release_date']}\n\n"
                    f"✨ {drama['overview']}"
                )
                await app.send_photo(
                    chat_id=chat_id,
                    photo=drama["poster"] if drama["poster"] else "https://i.ibb.co/6NfYQ7c/kdrama.jpg",
                    caption=caption
                )

# Scheduler
scheduler = AsyncIOScheduler()
scheduler.add_job(lambda: asyncio.run(send_digest()), 'cron', hour=9)  # Daily at 9 AM
scheduler.add_job(lambda: asyncio.run(send_digest()), 'cron', day_of_week='mon', hour=9)  # Weekly on Monday
scheduler.start()

# Keep the bot running
