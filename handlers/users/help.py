from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("""Salom ushbu botdan foydalanish bo'yicha yordam:

▪️ /start - Botni ishga tushirish va menyuni ko'rish.

▪️ /about - Bot haqida to'liq ma'lumot.

▪️ /xabar - Adminga xabar yuborish uchun.

Agar qo'shimcha yordam kerak bo'lsa yoki muammo yuzaga kelsa, /xabar orqali admin bilan bog'lanishingiz mumkin.""")
