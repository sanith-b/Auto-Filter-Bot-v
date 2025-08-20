# plugins/request_drama.py

from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters

# Private channel ID for forwarding drama requests
PRIVATE_CHANNEL_ID = "-1003028947753"

@app.on_message(filters.command("request_drama") & filters.private)
async def request_drama(client, message: Message):
    """
    Users can request a drama, and the request is automatically forwarded
    to the private channel for admin review.
    """
    if len(message.command) < 2:
        await message.reply_text("Usage: /request_drama <Drama Name>")
        return

    drama_name = " ".join(message.command[1:])
    user_info = f"@{message.from_user.username}" if message.from_user.username else message.from_user.id

    # Forward request to private channel
    await client.send_message(
        PRIVATE_CHANNEL_ID,
        f"📩 Drama Request from {user_info}:\n🎬 {drama_name}"
    )

    # Confirm to user
    await message.reply_text(f"✅ Your request for '{drama_name}' has been sent to the admin.")
