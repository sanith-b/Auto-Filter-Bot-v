# plugins/user_personalization.py
import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.ia_filterdb import *
import random

# =========================
# Load all dramas from database
# =========================
def load_dramas():
    dramas = {}
    for doc in db_dramas.find():  # Each document should have title, year, rating, episodes
        title = doc.get("title")
        dramas[title] = {
            "year": doc.get("year", "N/A"),
            "rating": doc.get("rating", "N/A"),
            "episodes": doc.get("episodes", 0)
        }
    return dramas

DRAMA_DB = load_dramas()

# =========================
# Add to Watchlist
# =========================
@app.on_message(filters.command("add_watchlist") & filters.private)
async def add_watchlist(client, message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /add_watchlist <Drama Name>")
        return
    drama_name = " ".join(message.command[1:])
    if drama_name not in DRAMA_DB:
        await message.reply_text("Drama not found.")
        return

    user = db_users.find_one({"user_id": message.from_user.id})
    if not user:
        db_users.insert_one({"user_id": message.from_user.id, "watchlist": [], "history": {}})

    db_users.update_one(
        {"user_id": message.from_user.id},
        {"$addToSet": {"watchlist": drama_name}}
    )
    await message.reply_text(f"✅ '{drama_name}' added to your Watchlist!")

# =========================
# View Watchlist
# =========================
@app.on_message(filters.command("watchlist") & filters.private)
async def view_watchlist(client, message):
    DRAMA_DB = load_dramas()  # Refresh dramas from database
    user = db_users.find_one({"user_id": message.from_user.id})
    watchlist = user.get("watchlist", []) if user else []

    if watchlist:
        text = "📌 Your Watchlist:\n\n"
        for drama in watchlist:
            info = DRAMA_DB.get(drama, {})
            text += f"🎬 {drama} ({info.get('year','N/A')}) ⭐ {info.get('rating','N/A')}\n"
        await message.reply_text(text)
    else:
        await message.reply_text("Your watchlist is empty. Use /add_watchlist to add dramas.")

# =========================
# Progress Tracking
# =========================
@app.on_message(filters.command("mark_episode") & filters.private)
async def mark_episode(client, message):
    if len(message.command) < 3:
        await message.reply_text("Usage: /mark_episode <Drama Name> <Episode Number>")
        return

    drama_name = message.command[1]
    episode = int(message.command[2])

    DRAMA_DB = load_dramas()  # Refresh dramas from database
    if drama_name not in DRAMA_DB:
        await message.reply_text("Drama not found.")
        return

    db_users.update_one(
        {"user_id": message.from_user.id},
        {"$set": {f"history.{drama_name}": episode}},
        upsert=True
    )
    await message.reply_text(f"✅ Marked episode {episode} of '{drama_name}' as watched.")

# =========================
# AI Recommendations (Basic)
# =========================
@app.on_message(filters.command("recommend") & filters.private)
async def recommend_drama(client, message):
    DRAMA_DB = load_dramas()  # Refresh dramas from database
    user = db_users.find_one({"user_id": message.from_user.id})
    watched = list(user.get("history", {}).keys()) if user else []

    # Recommend dramas not yet watched
    recommendations = [d for d in DRAMA_DB.keys() if d not in watched]
    if recommendations:
        suggestion = random.choice(recommendations)
        info = DRAMA_DB[suggestion]
        text = f"🎬 Recommended for you:\n\n{suggestion} ({info.get('year')}) ⭐ {info.get('rating')}"
    else:
        text = "No new recommendations! You've watched all dramas in the database."

    await message.reply_text(text)
