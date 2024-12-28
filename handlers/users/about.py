from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("🔹 Biz haqimizda ma'lumot olish uchun <b>👥 BIZ HAQIMIZDA</b> tugmasini bosing 👇",parse_mode='html')

