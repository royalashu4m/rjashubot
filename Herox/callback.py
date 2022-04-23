from SJM.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
    START_PIC,
)


@Client.on_callback_query(filters.regex("cb_start"))
async def start_op(_, query: CallbackQuery):
        await query.edit_message_text(
              f"""ʜᴇʟʟᴏ [✨]({START_PIC}) **ᴡᴇʟᴄᴏᴍᴇ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
 **ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏ ᴄᴀʟʟ !!**
 **ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ 💫**
 **ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴊᴏɪɴ @LittelStar_org**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛓ Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ Gʀᴏᴜᴘ ⛓",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("• Cᴏᴍᴍᴀɴᴅs •",  callback_data="cb_cmd"),],
                [
                    InlineKeyboardButton(
                    "• Oᴡɴᴇʀ •", 
                    url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton("• Dᴇᴠᴇʟᴏᴘᴇʀ ", url=f"https://t.me/LittelStar_org"),
                ],
                [
                    InlineKeyboardButton(
                        "• Sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "• Uᴘᴅᴀᴛᴇs •", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "• Sᴏᴜʀᴄᴇ Cᴏᴅᴇ •", url="https://github.com/royalashu4m/rjashubot"
                    )
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cb_cmd"))
async def cbcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**here is some commands**

𝙎𝙞𝙢𝙥𝙡𝙚 𝙘𝙤𝙢𝙢𝙖𝙣𝙙 

•  `/play (song name)` 
•  `/skip` - skip the current song
•  `/end` - stop music play
•  `/pause` - pause song play
•  `/resume` - resume song play
•  `/mute` - mute assistant in vc
•  `/lyrics (song name)`

𝙁𝙪𝙣 𝙘𝙤𝙢𝙢𝙖𝙣𝙙

• `/truth` 🌝
• `/dare`  🌝
• `/sjm`    🌝
• `/abhi`   🌝
• `/tricky` 🌝

𝙀𝙭𝙩𝙧𝙖 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨

• `/ping` pong !!
• `/start` - Alive msg ~group 
• `/id` - Find out your grp and your id // stickers id also
• `/uptime` - 💻
• `/rmd` clean all downloads
• `/clean` - clear storage 


⚡ Powered By [ASHU_ORG](https://t.me/LittelStar_org) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("• ʙᴀᴄᴋ", callback_data="cb_start")]]
        ),
    )







@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)
        
        
        
@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
