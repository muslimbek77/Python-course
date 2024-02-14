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
from my_keyboards import menu_button,auto_keyboard,builder3,eng_uz_colors
from ism_manosi import ismlar_manosi

ADMIN = 999588837 # Bu yerga id kiriting

TOKEN = "6841416417:AAEGzxAPm0JHbr48dwYKy_Vw9C28coSeXYk" #Token kiriting
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name} Sifat Maktablar botiga hush kelibsiz\nBu yerda maktablar haqida ma'lumot olishingiz mumkin!"
    await message.answer(text=text,reply_markup=menu_button)


@dp.message(F.text)
async def ism_funksiyasi(message:Message):
     ism = message.text
     natija = ismlar_manosi(ism)

     await message.answer(text=natija)


#maktab tugmasi bosilganda yuboriladigon habar
@dp.message(F.text=="Maktab 🎒")
async def maktab_menu(message:Message):
    #maktabingiz haqida ma'lumot
    text = """Maktab 1978- yil Zomin tumanga qarashli 39-maktab ochilgan. Maktab moslashtirilgan binoda joylashgan. Unga 130 ta 15 ta o’qituvchi maktab direktorii Nurmatov I.

     1979- yil 1- sentyabrdan Yangi qurilgan binoda 200 o’quvchi 20 nafar o’qiituvchi ko’p millatli maktab bo’lib asosiy o’quvchilarni rusiyzabon o’quvchilar tashkil etilgan.

     Maktab direktori:  Baratov Bolbek  Umarovich. 1980-yildan boshlab maktab  10-yillik bo’lib maktabda 400 o’quvchi 40 nafar o’qituvchi faoliyat ko’rsatgan.

         Maktab direktori:  Eshboev Mamat

1981- yildan boshlab maktab direktori:  Tovboev Bosim  360 nafar o’quvchi 45 nafar o’qituvchi faoliyat ko’rsatgan."""
    #maktab rasmini olish  #telegram-bot/8-9-dars/maktab.jpg
    photo = types.FSInputFile("telegram-bot/8-9-dars/maktab.jpg",filename="Fayozbek.jpg")
    
    #maktab haqidagi ma'lumotni yuborish
    await message.answer_photo(photo=photo,caption=text)

    
@dp.message(F.text=="/tugma3")
async def tugma_menu3(message:Message,state:FSMContext):
        await message.answer(text="3-tugma",reply_markup=builder3.as_markup(resize_keyboard=True))



@dp.message(Command(commands="colors"))
async def tugma_menu2(message:Message,state:FSMContext):
        
        await message.answer(text="My colors",reply_markup=auto_keyboard().as_markup(resize_keyboard=True))

@dp.message(F.text)
async def my_color(message:Message):
     text = message.text
     if text in eng_uz_colors.keys():
          result = eng_uz_colors[text]
          await message.answer(text=result)
     else:
          await message.answer(text="not")


@dp.message(F.text)
async def name(message:Message):
    ism = message.text
    natija = ismlar_manosi(ism=ism)

    await message.answer(text=natija)







async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
