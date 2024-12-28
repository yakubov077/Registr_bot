from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

add = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 KURSLAR")
        ],
        [
            KeyboardButton(text="👥 BIZ HAQIMIZDA"),
            KeyboardButton(text="📍 MANZILIMIZ")
        ]
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

add_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📔 PYTHON"),
        ],
        [
            KeyboardButton(text="🔙 ORQAGA QAYTISH")
        ]
    ],
   resize_keyboard=True
)

