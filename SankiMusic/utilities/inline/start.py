from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🔧 𝐇ᴇʟᴘ 🔧️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️ 𝐒ᴇᴛᴛɪɴɢs ⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🔧 𝐇ᴇʟᴘ & 𝐂ᴏᴍᴍᴀɴᴅ 🔧", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐒ᴜᴘᴘᴏʀᴛ 💥", url="https//t.me/timepassgroup01")
            ),
            InlineKeyboardButton(
                text="🥀 𝐆ʀᴏᴜᴘ 💥", url="https://t.me/dangerous_fighter_clan_0")
        ],
        [
            InlineKeyboardButton(
                text="♕︎ 𝐎ᴡɴᴇʀ ♕", url="https//t.me/taitangamer")
            )
        ],
     ]
    return buttons
