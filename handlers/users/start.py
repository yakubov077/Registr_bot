from aiogram.types import Message,CallbackQuery,ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.default.keyboard import add, add_2
from aiogram import F
from keyboard_buttons.inline.menu import menu,menu1
from states.help_stt import Registor
from loader import ADMINS, bot

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text=f"Assalomu alaykum {full_name}\nKerakli tugmani tanlang 👇🏻", reply_markup=add)
    except:
        await message.answer(text=f"Assalomu alaykum {full_name}\nKerakli tugmani tanlang 👇🏻", reply_markup=add)

@dp.message(F.text == "📚 KURSLAR")
async def register_yosh(message: Message):
    text = "<b>📙 Kurslardan birini tanlang</b>"
    await message.answer(text,parse_mode='html',reply_markup=add_2)

@dp.message(F.text == "📍 MANZILIMIZ")
async def location(message: Message): 
    text = """📌 <b>Bizning manzilimiz: </b>Sifat IT Akademiyasi\n
Navoiy sh. G'alabashox ko'chasi 77 | 7 uy, 
Bizning ofisimiz quyidagi xaritada ko'rsatilgan joyda joylashgan."""

    await message.answer_location(latitude=40.102545165025, longitude=65.3734143754646)
    await message.answer(text, parse_mode='html')

@dp.message(F.text == "👥 BIZ HAQIMIZDA")
async def register_yosh(message: Message):
    text = """<b>👥 BIZ HAQIMIZDA</b>
Sifatedu – bu dasturlash va IT sohasida ta'lim beruvchi yetakchi o'quv markazi. Bizning maqsadimiz – sizga eng so'nggi texnologiyalar va dasturlash tillari bo'yicha chuqur bilim va ko'nikmalar berishdir.

🌐 <b>Nimalarni taklif qilamiz:</b>
- Python dasturlash kurslari
- Django va boshqa web dasturlash framework-lari
- Ma'lumotlar tahlili va Data Science
- IT sohasida malaka oshirish kurslari
"""
    await message.answer(text,parse_mode='html')

@dp.message(F.text == "📔 PYTHON")
async def register_yosh(message: Message):
    text = """
<b>Sizni Python dunyosiga taklif qilamiz!</b> 🐍

🔹 Dasturlashning asosiy tillaridan biri bo'lgan Pythonni o'rganing  
🔹 Loyihalar yaratish orqali amaliy ko'nikmalar hosil qiling  
🔹 IT sohasi uchun mustahkam poydevor yarating  

🚀 Sifatedu bilan birgalikda bilim olishni boshlang!
"""
    await message.answer(text,parse_mode='html',reply_markup=menu)

@dp.message(F.text == "🔙 ORQAGA QAYTISH")
async def register_yosh(message: Message):
    text = "<b>🏠 Siz bosh menudasiz</b>"
    await message.answer(text,parse_mode='html',reply_markup=add)

@dp.callback_query(F.data == "kursga_yozilish")
async def reklama_urtacha(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    text = "ismingizni kiriting ✍🏻"
    await callbeck.message.answer(text,reply_markup=ReplyKeyboardRemove())
    await state.set_state(Registor.ism)
    
@dp.message(F.text, Registor.ism)
async def register_ism(message: Message, state: FSMContext):
    ism = message.text
    # Ismda faqat harflar bo'lishi kerak
    if ism.isdigit():
        await message.delete()
        await message.answer(text="Ism faqat harflardan iborat bo'lishi kerak ❗️")
    else:
        await state.update_data(ism=ism)
        await state.set_state(Registor.familiya)
        await message.answer("Familiyangizni kiriting ✍🏻")

@dp.message(Registor.ism)
async def register_ism_del(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(text="Ismingizni to'g'ri kiriting ❗️")


@dp.message(F.text, Registor.familiya)
async def register_familiya(message: Message, state: FSMContext):
    familiya = message.text
    # Familiyada faqat harflar bo'lishi kerak
    if familiya.isdigit():
        await message.delete()
        await message.answer(text="Familiya faqat harflardan iborat bo'lishi kerak ❗️")
    else:
        await state.update_data(familiya=familiya)
        await state.set_state(Registor.tel)
        await message.answer("Telfon raqamingizni kiriting 📞", reply_markup=menu1)

@dp.message(Registor.familiya)
async def register_ism_del(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(text="Familiyangizni to'g'ri kiriting ❗️")

@dp.message(F.contact, Registor.tel)
async def register_kurs(message: Message, state: FSMContext):
    data = await state.get_data()

    ism = data.get("ism")
    familiya = data.get("familiya")
    tel = message.contact.phone_number

    text = f"Ism: {ism}\nFamiliya: {familiya}\nTelefon: {tel}"
    await message.answer("Siz ro'yxatdan o'tdingiz 🎉")
    await message.answer("<b>🏠 Bosh menu</b>",parse_mode='html',reply_markup=add)

    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=text)

    await state.clear()

@dp.message(Registor.tel)
async def register_ism_del(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(text="Pastdagi tugmani bosing ❗️")