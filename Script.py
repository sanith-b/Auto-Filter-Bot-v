class script(object):
    START_TXT = """
🌸 <b>Welcome to My K-Drama Bot!</b> 🌸

🎬 Discover, watch, and download thousands of K-Dramas right here on Telegram!

✨ Features you’ll love:

🔍 <b>Smart Search & Trending</b> – Find dramas instantly and see what’s hot.
📥 <b>Easy Downloads & Episode Management</b> – Save episodes to watch anytime.
👥 <b>Group Support & Sharing</b> – Use the bot in groups to share dramas with friends.
⏰ <b>24/7 Availability</b> – Your K-Drama companion is always online.

💌 Get started now:

Tap <b>Help</b> for assistance and guidance

🌟 Your ultimate K-Drama companion is here! Enjoy!"""

    FEATURES_TXT = """<b>ʜᴇʀᴇ ɪꜱ ᴀʟʟ ᴍʏ ꜰᴜɴᴛɪᴏɴꜱ.</b>"""

    ABOUT_TXT = """🌸 About My K-Drama Bot 🌸

My K-Drama Bot is your <b>go-to Telegram companion for all things K-Drama!</b> Whether you’re looking for the latest hits, timeless classics, or hidden gems, this bot brings the entire K-Drama world to your fingertips.

📚 <b>Massive Library</b> – Thousands of episodes, from trending shows to beloved favorites.
🔍 <b>Smart Search</b> – Find dramas instantly with easy filters.
🎥 <b>IMDb Info</b> – Check ratings, cast, and details without leaving Telegram.
📥 <b>Easy Downloads</b> – Save episodes to watch anytime.
📝 <b>Request Favorites</b> – Missing a show? Request it, and it might appear soon!
⏰ <b>24/7 Availability</b> – Your K-Drama companion is always online, ready to entertain.
👥 <b>Group Support</b> – Use the bot in groups to share dramas with friends and communities.

Experience K-Drama like never before, all in <b>one seamless, fun, and easy-to-use bot!</b>"""

    FORCESUB_TEXT="""<b>
ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ʀᴇᴏ̨ᴜᴇsᴛᴇᴅ ʙʏ ʏᴏᴜ.

ʏᴏᴜ ᴡɪʟʟ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ.

ғɪʀsᴛ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ "Jᴏɪɴ ᴜᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ" ʙᴜᴛᴛᴏɴ, ᴛʜᴇɴ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ "ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ Jᴏɪɴ" ʙᴜᴛᴛᴏɴ.

ᴀғᴛᴇʀ ᴛʜᴀᴛ, ᴛʀʏ ᴀᴄᴄᴇssɪɴɢ ᴛʜᴀᴛ ᴍᴏᴠɪᴇ ᴛʜᴇɴ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ "ᴛʀʏ ᴀɢᴀɪɴ" ʙᴜᴛᴛᴏɴ.
    </b>"""
           
    MULTI_STATUS_TXT = """<b>╭────[ ᴅᴀᴛᴀʙᴀsᴇ 1 ]────⍟</b>
│
├⋟ ᴀʟʟ ᴜsᴇʀs ⋟ <code>{}</code>
├⋟ ᴀʟʟ ɢʀᴏᴜᴘs ⋟ <code>{}</code>
├⋟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ ⋟ <code>{}</code>
├⋟ ᴀʟʟ ꜰɪʟᴇs ⋟ <code>{}</code>
├⋟ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ ⋟ <code>{}</code>
├⋟ ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ ⋟ <code>{}</code>
│
<b>├────[ ᴅᴀᴛᴀʙᴀsᴇ 2 ]────⍟</b>   
│
├⋟ ᴀʟʟ ꜰɪʟᴇs ⋟ <code>{}</code>
├⋟ ꜱɪᴢᴇ ⋟ <code>{}</code>
├⋟ ꜰʀᴇᴇ ⋟ <code>{}</code>
│
<b>├────[ 🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖 ]────⍟</b>   
│
├⋟ ᴜᴘᴛɪᴍᴇ ⋟ {}
├⋟ ʀᴀᴍ ⋟ <code>{}%</code>
├⋟ ᴄᴘᴜ ⋟ <code>{}%</code>   
│
├⋟ ʙᴏᴛʜ ᴅʙ ꜰɪʟᴇ'ꜱ: <code>{}</code>
│
<b>╰─────────────────────⍟</b>"""

    STATUS_TXT = """<b>╭────[ ᴅᴀᴛᴀʙᴀsᴇ 1 ]────⍟</b>
│
├⋟ ᴀʟʟ ᴜsᴇʀs ⋟ <code>{}</code>
├⋟ ᴀʟʟ ɢʀᴏᴜᴘs ⋟ <code>{}</code>
├⋟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ ⋟ <code>{}</code>
├⋟ ᴀʟʟ ꜰɪʟᴇs ⋟ <code>{}</code>
├⋟ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ ⋟ <code>{}</code>
├⋟ ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ ⋟ <code>{}</code>
│
<b>├────[ 🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖 ]────⍟</b>   
│
├⋟ ᴜᴘᴛɪᴍᴇ ⋟ {}
├⋟ ʀᴀᴍ ⋟ <code>{}%</code>
├⋟ ᴄᴘᴜ ⋟ <code>{}%</code>   
│
<b>╰─────────────────────⍟</b>"""

    EARN_INFO = """<b>📬 Contact @myKdrama_bot</b>
If you want to reach the bot team anonymously, here are the safest options:

💬 <strong>Telegram (Anonymous)</strong>
      Use a secondary Telegram account to contact:
      Bot: <a href="https://t.me/myKdrama_bot" target="_blank">@myKdrama_bot</a>
      Developer/Admin: <a href="https://t.me/SupMyKDramaBot" target="_blank">@admin</a>
"""    
   
    
    VERIFICATION_TEXT = """<b><i>👋 ʜᴇʏ {},

📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪꜰʏ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 1/3 ✓

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ).</i></b>"""
    

    VERIFY_COMPLETE_TEXT = """<b><i>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.</i></b>"""

    SECOND_VERIFICATION_TEXT = """<b><i>👋 ʜᴇʏ {},

📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/3 ✓

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ).</i></b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b><i>👋 ʜᴇʏ {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.</i></b>"""

    THIRDT_VERIFICATION_TEXT = """<b><i>👋 ʜᴇʏ {},
    
📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 3/3 ✓

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</i></b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b><i>👋 ʜᴇʏ {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 3ʀᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</i></b>"""

    VERIFIED_LOG_TEXT = """ᴜꜱᴇʀ ᴠᴇʀɪꜰɪᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓

👤 ɴᴀᴍᴇ:- {} [ <code>{}</code> ]

📆 ᴅᴀᴛᴇ:- <code>{} </code>

#Verificaton_{}_Completed"""    
       
    LOG_TEXT_G = """#NewGroup
    
Gʀᴏᴜᴘ = {}
Iᴅ = <code>{}</code>
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}
"""

    LOG_TEXT_P = """#NewUser
    
Iᴅ - <code>{}</code>
Nᴀᴍᴇ - {}
"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ,
ʀᴇǫᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ ?"""

    I_CUDNT = """<b><i>ᴛʜɪꜱ ᴍᴏᴠɪᴇ ɪꜱ ɴᴏᴛ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ.

ɪᴛ ʜᴀꜱ ᴇɪᴛʜᴇʀ ɴᴏᴛ ʙᴇᴇɴ ʀᴇʟᴇᴀꜱᴇᴅ ᴏʀ ʜᴀꜱ ɴᴏᴛ ʏᴇᴛ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴅᴀᴛᴀʙᴀꜱᴇ.</i></b>"""
    
    I_CUD_NT = """<b><i>ᴛʜɪꜱ ᴍᴏᴠɪᴇ ɪꜱ ɴᴏᴛ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ.

ɪᴛ ʜᴀꜱ ᴇɪᴛʜᴇʀ ɴᴏᴛ ʙᴇᴇɴ ʀᴇʟᴇᴀꜱᴇᴅ ᴏʀ ʜᴀꜱ ɴᴏᴛ ʏᴇᴛ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴅᴀᴛᴀʙᴀꜱᴇ.</i></b>"""
    
    MVE_NT_FND = """<b><i>ᴛʜɪꜱ ᴍᴏᴠɪᴇ ɪꜱ ɴᴏᴛ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ.

ɪᴛ ʜᴀꜱ ᴇɪᴛʜᴇʀ ɴᴏᴛ ʙᴇᴇɴ ʀᴇʟᴇᴀꜱᴇᴅ ᴏʀ ʜᴀꜱ ɴᴏᴛ ʏᴇᴛ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴅᴀᴛᴀʙᴀꜱᴇ.</i></b>"""
    
    TOP_ALRT_MSG = """ꜱᴇᴀʀᴄʜɪɴɢ ꜰᴏʀ ǫᴜᴇʀʏ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    MELCOW_ENG = """<b>👋 ʜᴇʏ {},\n\n🍁 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ\n🌟 {} \n\n🔍 ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴇᴀʀᴄʜ ʏᴏᴜʀ ꜰᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ ʙʏ ᴊᴜꜱᴛ ᴛʏᴘɪɴɢ ɪᴛ'ꜱ ɴᴀᴍᴇ 🔎\n\n⚠️ ɪꜰ ʏᴏᴜ'ʀᴇ ʜᴀᴠɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʀᴇɢᴀʀᴅɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴏʀ ꜱᴏᴍᴇᴛʜɪɴɢ ᴇʟꜱᴇ ᴛʜᴇɴ ᴍᴇꜱꜱᴀɢᴇ ʜᴇʀᴇ 👇</b>"""
    
    DISCLAIMER_TXT = """
<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. 
</b>"""

    PREMIUM_TEXT = """<blockquote>🎖️ <b>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</b></blockquote>

◉ 07 ᴅᴀʏꜱ - 15 ₹ / 15 ꜱᴛᴀʀ 
◉ 15 ᴅᴀʏꜱ - 30 ₹ / 30 ꜱᴛᴀʀ 
◉ 01 ᴍᴏɴᴛʜꜱ - 60 ₹ / 60 ꜱᴛᴀʀ 
◉ 02 ᴍᴏɴᴛʜꜱ - 120 ₹ / 120 ꜱᴛᴀʀ 
◉ 03 ᴍᴏɴᴛʜꜱ - 220 ₹ / 220 ꜱᴛᴀʀ

•─────•─────────•─────•
🏷️ <a href='https://t.me/+blcE2jS-iGtkMjNl'>ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ᴘʀᴏᴏꜰ</a>

‼️ ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.
‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇꜱ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ."""

    PREMIUM_STAR_TEXT = """<b><blockquote>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ: ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛᴀʀꜱ ⭐</blockquote>

ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ꜱᴇʀᴠɪᴄᴇ ᴜꜱɪɴɢ ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛᴀʀꜱ.  

ɪꜰ ʏᴏᴜ ꜰᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ᴛᴀᴋᴇ ᴀ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀɴᴅ ꜱᴇɴᴅ ɪᴛ ᴛᴏ - @SilentXBotz

ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ᴀᴍᴏᴜɴᴛ ᴀɴᴅ ᴘᴜʀᴄʜᴀꜱᴇ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 👇.</b>
"""
    USDT_TEXT = """
▪️Coin - <code>USDT<?code>
▪️Network - <code>TRX (TRC20)</code>

▪️Address - <code>rNRyjPaHonNcMjt7fM1UGG8gfxaD8AtZ6L</code>
    """
    TON_TEXT = """
▪️Coin - <code>TON</code>
▪️Network  - <code>TON</code>
▪️Memo - <code>157072592</code>
▪️Address - <code>EQD5mxRgCuRNLxKxeOjG6r14iSroLF5FtomPnet-sgP5xNJb</code>
    """
    BITCOIN_TEXT = """
▪️Coin - <code>BTC (Bitcoin)</code>
▪️Network - <code>BSC (BEP20)</code>
▪️Address - <code>0xDC432295B69c9DC3c83D22BEbb048446E27e2598</code>
    """
    SCANQR_TEXT = """
Scan QR Code
    """
    
    PREMIUM_UPI_TEXT = """<b><blockquote>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ: ᴜᴘɪ</blockquote>

ʏᴏᴜ ᴄᴀɴ ᴘᴜʀᴄʜᴀꜱᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜʀᴏᴜɢʜ ᴜᴘɪ , ɴᴇᴛ ʙᴀɴᴋɪɴɢ.

💳 ᴜᴘɪ ɪᴅ - <code>ɴᴏ ᴀᴠᴀɪʟᴀʙʟᴇ ʀɪɢʜᴛ ɴᴏᴡ</code>

💢 ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.

‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴘʟᴇᴀꜱᴇ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ.</b>"""
    
    
    BPREMIUM_TXT = """<blockquote>🎁 <b>ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ</b> :</blockquote>

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ   
○ ᴀᴅ-ꜰʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-ꜱᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ ꜱᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋꜱ                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ                                                                        
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ ꜱᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

• ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ ʙʏ ʀᴇꜰᴇʀɪɴɢ ʏᴏᴜʀ ꜰʀɪᴇɴᴅꜱ ᴏʀ ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ꜱᴇʀᴠɪᴄᴇ 

•─────•─────────•─────•
◉ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ : /myplan

‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇꜱ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ."""   
    
      
    NORSLTS = """ 
#NoResults

Iᴅ : <code>{}</code>
Nᴀᴍᴇ : {}

Mᴇꜱꜱᴀɢᴇ : <b>{}</b>"""
    
    CAPTION = """<b>{file_name}\nUploaded By: <a herf="https://t.me/SilentXBotz">[SilentXBotz]</a></b>"""

    IMDB_TEMPLATE_TXT = """
<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
� Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
📀 RunTime: {runtime} Minutes

⏰Result Shown in: {remaining_seconds} <i>seconds</i> 🔥
Requested by : {message.from_user.mention}</b>"""    

    RESTART_TXT = """
<b>{} ʙᴏᴛ ʀᴇꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ !

📅 ᴅᴀᴛᴇ : <code>{}</code>
⏰ ᴛɪᴍᴇ : <code>{}</code>
🌐 ᴛɪᴍᴇᴢᴏɴᴇ : <code>ᴀꜱɪᴀ/ᴋᴏʟᴋᴀᴛᴀ</code>
🛠️ ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ : <code>V4.2 [ ꜱᴛᴀʙʟᴇ ]</code>
</b>"""
    LOGO = """
  ____  _ _            _  __  ______        _       
 / ___|(_) | ___ _ __ | |_\ \/ / __ )  ___ | |_ ____
 \___ \| | |/ _ \ '_ \| __|\  /|  _ \ / _ \| __|_  /
  ___) | | |  __/ | | | |_ /  \| |_) | (_) | |_ / / 
 |____/|_|_|\___|_| |_|\__/_/\_\____/ \___/ \__/___|
                                                                                                                                                                            
𝙱𝙾𝚃 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈...."""

    ADMIN_CMD = """ʜᴇʏ 👋,

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴀᴅᴍɪɴꜱ ⇊

• /movie_update - <code>ᴏɴ / ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code> 
• /pm_search - <code>ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ / ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code>
• /verifyon - <code>ᴛᴜʀɴ ᴏɴ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ (ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ)</code>
• /verifyoff - <code>ᴛᴜʀɴ ᴏꜰꜰ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ (ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ)</code>
• /logs - <code>ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.</code>
• /delete - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /leave  - <code>ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘꜱ.</code>
• /broadcast - <code>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.</code>
• /grp_broadcast - <code>ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /gfilters - <code>ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /send - <code>ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.</code>
• /add_premium - <code>ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.</code>
• /remove_premium - <code>ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.</code>
• /premium_users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.</code>
• /get_premium - <code>ɢᴇᴛ ɪɴꜰᴏ ᴏꜰ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ.</code>
• /restart - <code>ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</code>"""

    GROUP_CMD = """ʜᴇʏ 👋,
📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴄᴜꜱᴛᴏᴍɪᴢᴇᴅ ɢʀᴏᴜᴘꜱ ⇊

• /settings - ᴄʜᴀɴɢᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.
• /set_shortner - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_time - ꜱᴇᴛ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_time_2 - ꜱᴇᴛ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_log_channel - ꜱᴇᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.
• /set_fsub - ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /remove_fsub - ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /reset_group - ʀᴇꜱᴇᴛ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ.
• /details - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ."""    

    PAGE_TXT = """ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ꜱᴏ ᴄᴜʀɪᴏᴜꜱ ⁉️"""    
   
    SOURCE_TXT = """<b>ՏOᑌᖇᑕᗴ ᑕOᗪᗴ :</b> 👇\nThis Is An Open-Source Project. You Can Use It Freely, But Selling The Source Code Is Strictly Prohibited."""
