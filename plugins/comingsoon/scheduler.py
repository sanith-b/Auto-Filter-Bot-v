from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from .core import get_reminders_for_today, fetch_drama_details
from logging_helper import LOGGER

scheduler = AsyncIOScheduler()

async def check_reminders(client):
    today = datetime.now().date()
    reminders = await get_reminders_for_today(today)
    
    for reminder in reminders:
        user_id = reminder['user_id']
        drama = await fetch_drama_details(reminder['drama_id'])
        try:
            await client.send_photo(
                user_id,
                photo=drama['poster'],
                caption=f"🔔 Release Today! 🎬 {drama['title']} is releasing today!"
            )
            await delete_reminder(reminder['_id'])
        except Exception as e:
            LOGGER.error(f"[REMINDER ERROR] {e}")

def start_scheduler(client):
    scheduler.add_job(check_reminders, 'cron', hour=7, minute=0, args=[client])
    scheduler.start()
