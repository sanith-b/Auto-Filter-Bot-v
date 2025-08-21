# plugins/comingsoon.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.users_chats_db import db
from datetime import datetime
import requests
import asyncio

TMDB_API_KEY = "90dde61a7cf8339a2cff5d805d5597a9"

comingsoon_col = db.comingsoon  # Using your existing db instance

# ---------------- HELPERS ----------------
def fetch_upcoming_dramas():
    url = f"https://api.themoviedb.org/3/tv/upcoming?api_key={TMDB_API_KEY}&language=en-US&page=1"
    res = requests.get(url).json()
    for item in res.get('results', []):
        drama_id = str(item['id'])

        # Fetch top 5 cast
        cast = []
        credits_res = requests.get(f"https://api.themoviedb.org/3/tv/{drama_id}/credits?api_key={TMDB_API_KEY}").json()
        cast = [c['name'] for c in credits_res.get('cast', [])[:5]]

        # Fetch genres
        genre_mapping = requests.get(f"https://api.themoviedb.org/3/genre/tv/list?api_key={TMDB_API_KEY}&language=en-US").json().get('genres', [])
        genre_dict = {g['id']: g['name'] for g in genre_mapping}
        genres = [genre_dict.get(gid, str(gid)) for gid in item.get('genre_ids', [])]

        # Fetch trailer
        trailer = ''
        videos_res = requests.get(f"https://api.themoviedb.org/3/tv/{drama_id}/videos?api_key={TMDB_API_KEY}&language=en-US").json()
        for vid in videos_res.get('results', []):
            if vid['type'] == 'Trailer' and vid['site'] == 'YouTube':
                trailer = f"https://youtu.be/{vid['key']}"
                break

        comingsoon_col.update_one(
            {"_id": drama_id},
            {"$set": {
                "_id": drama_id,
                "title": item.get('name'),
                "release_date": item.get('first_air_date', "2099-01-01"),
                "overview": item.get('overview', ''),
                "poster_path": item.get('poster_path', ''),
                "cast": cast,
                "genre": genres,
                "trailer": trailer
            }},
            upsert=True
        )

def drama_buttons():
    buttons = []
    dramas = comingsoon_col.find().sort("release_date", 1).limit(10)
    for drama in dramas:
        buttons.append([InlineKeyboardButton(drama['title'], callback_data=f"drama:{drama['_id']}")])
    return InlineKeyboardMarkup(buttons)

def format_drama_details(drama):
    release_date = datetime.strptime(drama['release_date'], "%Y-%m-%d")
    days_left = (release_date - datetime.now()).days
    poster_url = f"https://image.tmdb.org/t/p/w500{drama['poster_path']}" if drama.get('poster_path') else ''
    text = f"🎬 <b>{drama['title']}</b>\n" \
           f"📅 Release Date: {drama['release_date']} ({days_left} days left)\n" \
           f"⭐ Genres: {', '.join(drama.get('genre', []))}\n" \
           f"🎭 Cast: {', '.join(drama.get('cast', []))}\n" \
           f"📝 Synopsis: {drama.get('overview','')[:300]}...\n"
    if drama.get('trailer'):
        text += f"▶️ Trailer: {drama['trailer']}\n"
    if poster_url:
        text += poster_url
    return text

# ---------------- COMMAND ----------------
@Client.on_message(filters.command("comingsoon"))
async def comingsoon_command(client, message):
    fetch_upcoming_dramas()
    buttons = drama_buttons()
    await message.reply_text(
        "📺 <b>Upcoming K-Dramas:</b>\nClick a drama to see details.",
        reply_markup=buttons,
        disable_web_page_preview=True
    )

# ---------------- CALLBACKS ----------------
@Client.on_callback_query()
async def callback_handler(client, callback_query):
    data = callback_query.data
    if data.startswith("drama:"):
        drama_id = data.split(":")[1]
        drama = comingsoon_col.find_one({"_id": drama_id})
        if drama:
            text = format_drama_details(drama)
            await callback_query.message.edit_text(text, disable_web_page_preview=False)
