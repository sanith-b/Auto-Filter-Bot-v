import requests
import random
import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pymongo import MongoClient
import asyncio
from typing import Optional

# 🔑 API Keys and Database Configuration
TMDB_API_KEY = "90dde61a7cf8339a2cff5d805d5597a9"
MONGODB_URI = "mongodb+srv://botadmin:1sQZEOQ7y3SSPNV3@kdramabot.00xhgvx.mongodb.net/?retryWrites=true&w=majority&appName=kdramabot"
DATABASE_NAME = "kdramabot"

# 🗄️ MongoDB Connection
try:
    mongo_client = MongoClient(MONGODB_URI)
    db = mongo_client[DATABASE_NAME]
    reminders_collection = db.reminders
    users_collection = db.users
    print("✅ MongoDB connection established successfully!")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
    mongo_client = None
    db = None

# 📊 Database helper functions
def save_reminder(user_id: int, username: str, drama_id: str, drama_title: str, release_date: str):
    """Save a reminder to MongoDB"""
    if not db:
        return False
    
    try:
        reminder_data = {
            "user_id": user_id,
            "username": username,
            "drama_id": drama_id,
            "drama_title": drama_title,
            "release_date": release_date,
            "created_at": datetime.datetime.now(),
            "notified": False
        }
        
        # Check if reminder already exists
        existing = reminders_collection.find_one({
            "user_id": user_id,
            "drama_id": drama_id
        })
        
        if existing:
            return "exists"
        
        reminders_collection.insert_one(reminder_data)
        return True
    except Exception as e:
        print(f"Error saving reminder: {e}")
        return False

def get_user_reminders(user_id: int):
    """Get all reminders for a user"""
    if not db:
        return []
    
    try:
        reminders = list(reminders_collection.find({"user_id": user_id, "notified": False}))
        return reminders
    except Exception as e:
        print(f"Error fetching reminders: {e}")
        return []

def update_user_stats(user_id: int, username: str):
    """Update or create user statistics"""
    if not db:
        return
    
    try:
        users_collection.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "username": username,
                    "last_active": datetime.datetime.now()
                },
                "$inc": {"command_count": 1}
            },
            upsert=True
        )
    except Exception as e:
        print(f"Error updating user stats: {e}")

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

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error fetching TMDB data: {e}")
        return []

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
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error fetching trailer: {e}")
        return None

    for video in data.get("results", []):
        if video["site"] == "YouTube" and video["type"] == "Trailer":
            return f"https://youtu.be/{video['key']}"
    return None

# ⚡ Command Handler
@Client.on_message(filters.command("comingsoon"))
async def comingsoon_handler(client, message):
    # Update user stats
    update_user_stats(
        message.from_user.id, 
        message.from_user.username or message.from_user.first_name
    )
    
    # Send loading message
    loading_msg = await message.reply_text("🔄 Fetching upcoming K-Dramas...")
    
    dramas = get_coming_soon()

    if not dramas:
        await loading_msg.edit_text("🌸 No upcoming K-Dramas found at the moment!")
        return

    await loading_msg.delete()

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
        
        buttons.append([InlineKeyboardButton("📅 Remind Me", callback_data=f"remind_{drama['id']}_{drama['title'][:20]}")])

        try:
            await message.reply_photo(
                drama["poster"] if drama["poster"] else "https://i.ibb.co/6NfYQ7c/kdrama.jpg",
                caption=caption,
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        except Exception as e:
            print(f"Error sending drama info: {e}")
            # Fallback to text message if photo fails
            await message.reply_text(
                caption,
                reply_markup=InlineKeyboardMarkup(buttons)
            )

# ⚡ Command to view user's reminders
@Client.on_message(filters.command("myreminders"))
async def my_reminders_handler(client, message):
    update_user_stats(
        message.from_user.id, 
        message.from_user.username or message.from_user.first_name
    )
    
    reminders = get_user_reminders(message.from_user.id)
    
    if not reminders:
        await message.reply_text("📋 You don't have any active reminders!")
        return
    
    reminder_text = "📅 <b>Your Active Reminders:</b>\n\n"
    for reminder in reminders:
        reminder_text += f"🎬 <b>{reminder['drama_title']}</b>\n"
        reminder_text += f"📅 Release Date: {reminder['release_date']}\n"
        reminder_text += f"⏰ Reminder Set: {reminder['created_at'].strftime('%Y-%m-%d')}\n\n"
    
    await message.reply_text(reminder_text)

# ⚡ Callback Handler for "Remind Me"
@Client.on_callback_query(filters.regex(r"^remind_"))
async def remind_me(client, query):
    try:
        # Parse callback data
        parts = query.data.split("_", 2)
        drama_id = parts[1]
        drama_title = parts[2] if len(parts) > 2 else "Unknown Drama"
        
        user_id = query.from_user.id
        username = query.from_user.username or query.from_user.first_name
        
        # Get drama details to get release date
        dramas = get_coming_soon()
        release_date = "TBA"
        full_title = drama_title
        
        for drama in dramas:
            if str(drama["id"]) == drama_id:
                release_date = drama["release_date"] or "TBA"
                full_title = drama["title"]
                break
        
        # Save reminder to database
        result = save_reminder(user_id, username, drama_id, full_title, release_date)
        
        if result == "exists":
            await query.answer("⚠️ You already have a reminder set for this drama!", show_alert=True)
        elif result:
            await query.answer("📅 Reminder set successfully! Use /myreminders to view all your reminders.", show_alert=True)
        else:
            await query.answer("❌ Failed to set reminder. Please try again later.", show_alert=True)
            
    except Exception as e:
        print(f"Error in remind_me callback: {e}")
        await query.answer("❌ An error occurred. Please try again later.", show_alert=True)

# 📊 Admin command to get database stats (optional)
@Client.on_message(filters.command("statscoming"))
async def stats_handler(client, message):
    if not db:
        await message.reply_text("❌ Database connection not available.")
        return
    
    try:
        total_users = users_collection.count_documents({})
        total_reminders = reminders_collection.count_documents({"notified": False})
        
        stats_text = f"📊 <b>Bot Statistics:</b>\n\n"
        stats_text += f"👥 Total Users: {total_users}\n"
        stats_text += f"📅 Active Reminders: {total_reminders}\n"
        
        await message.reply_text(stats_text)
    except Exception as e:
        print(f"Error fetching stats: {e}")
        await message.reply_text("❌ Error fetching statistics.")

# 🚀 Optional: Background task to send reminders (you can implement this based on your needs)
async def check_reminders():
    """Background task to check for dramas releasing today and send reminders"""
    if not db:
        return
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    try:
        # Find reminders for dramas releasing today
        reminders_due = list(reminders_collection.find({
            "release_date": today,
            "notified": False
        }))
        
        for reminder in reminders_due:
            # Here you would send a message to the user
            # You'll need to implement this based on your bot's client instance
            print(f"Reminder due for user {reminder['user_id']}: {reminder['drama_title']}")
            
            # Mark as notified
            reminders_collection.update_one(
                {"_id": reminder["_id"]},
                {"$set": {"notified": True, "notified_at": datetime.datetime.now()}}
            )
            
    except Exception as e:
        print(f"Error checking reminders: {e}")

# 🎯 Help command
@Client.on_message(filters.command("helpcoming"))
async def help_handler(client, message):
    help_text = """
🌸 <b>K-Drama Bot Commands:</b>

/comingsoon - Get upcoming K-Dramas with trailers
/myreminders - View your active reminders
/help - Show this help message
/stats - View bot statistics

<b>How to use:</b>
1. Use /comingsoon to see upcoming K-Dramas
2. Click "📅 Remind Me" on any drama you're interested in
3. Use /myreminders to see all your reminders

Enjoy discovering new K-Dramas! 🎭✨
    """
    await message.reply_text(help_text)
