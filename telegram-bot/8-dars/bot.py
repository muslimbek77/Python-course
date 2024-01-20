import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from my_keyboards import menu_button
ADMIN = 999588837 # Bu yerga id kiriting
TOKEN = "6962596717:AAH8rK6QXNil4On5IeRbp5MfCSxIXf8cmbs" #Token kiriting
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)




@dp.message(CommandStart())
async def command_start_handler(message: Message,state:FSMContext) -> None:
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name} Sifat botiga hush kelibsiz\nRo'yhatdan o'tish uchun ismingizni kiriting!"
    await message.answer(text=text,reply_markup=menu_button)


#maktab tugmasi bosilganda yuboriladigon habar
@dp.message(F.text=="Maktab 🎒")
async def maktab_menu(message:Message,state:FSMContext):
    #maktabingiz haqida ma'lumot
    text = """Maktab 1978- yil Zomin tumanga qarashli 39-maktab ochilgan. Maktab moslashtirilgan binoda joylashgan. Unga 130 ta 15 ta o’qituvchi maktab direktorii Nurmatov I.

     1979- yil 1- sentyabrdan Yangi qurilgan binoda 200 o’quvchi 20 nafar o’qiituvchi ko’p millatli maktab bo’lib asosiy o’quvchilarni rusiyzabon o’quvchilar tashkil etilgan.

     Maktab direktori:  Baratov Bolbek  Umarovich. 1980-yildan boshlab maktab  10-yillik bo’lib maktabda 400 o’quvchi 40 nafar o’qituvchi faoliyat ko’rsatgan.

         Maktab direktori:  Eshboev Mamat

1981- yildan boshlab maktab direktori:  Tovboev Bosim  360 nafar o’quvchi 45 nafar o’qituvchi faoliyat ko’rsatgan."""
    #maktab rasmini olish 
    photo = types.FSInputFile("telegram-bot/8-dars/maktab.jpg",filename="maktab.jpg")
    
    #maktab haqidagi ma'lumotni yuborish
    await message.answer_photo(photo=photo,caption=text)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())