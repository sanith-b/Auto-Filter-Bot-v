import requests
from datetime import datetime
from database.users_chats_db import db
from info import TMDB_API_KEY
from logging_helper import LOGGER

TMDB_BASE_URL = 'https://api.themoviedb.org/3'

async def fetch_upcoming_dramas():
    url = f"{TMDB_BASE_URL}/discover/tv?api_key={TMDB_API_KEY}&language=en-US&sort_by=release_date.asc&air_date.gte={datetime.now().date()}"
    response = requests.get(url)
    return response.json().get('results', [])

async def fetch_drama_details(drama_id):
    url = f"{TMDB_BASE_URL}/tv/{drama_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    trailer_url = None
    if 'videos' in data and data['videos']['results']:
        trailer_url = f"https://www.youtube.com/watch?v={data['videos']['results'][0]['key']}"
    return {
        'title': data['name'],
        'overview': data['overview'],
        'release_date': data['first_air_date'],
        'poster': f"https://image.tmdb.org/t/p/w500{data['poster_path']}" if data['poster_path'] else None,
        'trailer_url': trailer_url
    }

async def save_reminder(user_id, drama_id, release_date):
    await db.reminders.insert_one({
        'user_id': user_id,
        'drama_id': drama_id,
        'release_date': release_date
    })

async def get_reminders_for_today(today):
    return await db.reminders.find({'release_date': today}).to_list(length=None)

async def delete_reminder(reminder_id):
    await db.reminders.delete_one({'_id': reminder_id})
