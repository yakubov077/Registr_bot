from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✏️ Kursga yozilish", callback_data="kursga_yozilish"), 
        ]
    ]
)

menu1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☎️ Telfon raqam yuborish", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

