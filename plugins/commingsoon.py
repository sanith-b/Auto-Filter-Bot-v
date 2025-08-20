import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Your Kuryana API base URL
KURYANA_API_URL = "https://kuryana.tbdh.app"

# Initialize the Pyrogram client
app = Client("kdrama_bot")

# Command to fetch upcoming K-Dramas
@app.on_message(filters.command("comingsoon"))
async def comingsoon(client, message):
    # Fetch seasonal K-Dramas for the current year and quarter
    response = requests.get(f"{KURYANA_API_URL}/seasonal/2025/3")
    if response.status_code == 200:
        dramas = response.json()
        if dramas:
            # Process and send the first drama's details
            drama = dramas[0]
            title = drama.get("title", "Unknown Title")
            synopsis = drama.get("synopsis", "No synopsis available.")
            poster = drama.get("images", {}).get("poster", "https://i.ibb.co/6NfYQ7c/kdrama.jpg")
            drama_url = f"https://mydramalist.com/{drama.get('slug', '')}"

            caption = f"🎬 {title}\n\n{synopsis}\n\nMore info: {drama_url}"

            buttons = [
                [InlineKeyboardButton("🔔 Remind Me", callback_data="remind_me")]
            ]

            await message.reply_photo(
                photo=poster,
                caption=caption,
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        else:
            await message.reply("No upcoming K-Dramas found.")
    else:
        await message.reply("Failed to fetch upcoming K-Dramas.")

# Run the bot
app.run()
