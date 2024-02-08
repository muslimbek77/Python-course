import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import Form
import sqlite3

#regular expression uchun
import re # yangi qo'shildi e'tibor bering


ADMIN = 999588837 # Bu yerga id kiriting
TOKEN = "6841416417:AAEGzxAPm0JHbr48dwYKy_Vw9C28coSeXYk" #Token kiriting
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message,state:FSMContext) -> None:
    await state.set_state(Form.first_name)
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name} Sifat botiga hush kelibsiz\nRo'yhatdan o'tish uchun ismingizni kiriting!"
    await message.reply(text=text)

@dp.message(Form.first_name,F.text)
async def get_first_name(message:Message,state:FSMContext):

    first_name = message.text
    await state.update_data(first_name=first_name)

    await state.set_state(Form.last_name)
    text = f"Familyangizni kiriting!"
    await message.reply(text=text)

@dp.message(Form.last_name, F.text)
async def get_last_name(message:Message,state:FSMContext):

    last_name = message.text
    await state.update_data(last_name=last_name)

    await state.set_state(Form.photo)
    text = f"Rasmingizni yuboring!"
    await message.reply(text=text)


#rasm uchun dispacher handler state 
@dp.message(Form.photo,F.photo)
async def get_photo(message:Message,state:FSMContext):

    photo = message.photo[-1].file_id #rasmni file id sini saqlab olamiz
    await state.update_data(photo=photo)
    await state.set_state(Form.phone_number)
    text = f"Telefon nomeringizni kiriting!"
    await message.reply(text=text)

#rasmdan boshqa narsa yuborilsa javob qaytaramiz
@dp.message(Form.photo)
async def not_get_photo(message:Message,state:FSMContext):
    text = f"Iltimos rasm yuboring!"
    await message.reply(text=text)


#telefon nomer uchun
@dp.message(Form.phone_number)
async def get_phone_number(message:Message,state:FSMContext):
    pattern = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    #shart beramiz
    #telefon nomer to'g'ri kiritilgan bo'lsa ishlaydi
    if re.match(pattern,message.text):

        phone_number = message.text
        await state.update_data(phone_number=phone_number)

        await state.set_state(Form.home_number)
        text = f"Uy raqamingizni kiriting!"
        await message.reply(text=text)
    #aks holda esa telefon nomerni to'g'ri kiritishini so'raymiz.
    else:
        await message.reply(text="telefon nomeringizni noto'g'ri kiritdingiz")

#Vazifa [photo,kurs_nomi,email....... va hokazo] 15 tacha filterdan foydalanib ro'yhatdan o'tish uchun, kiritilishi kerak bo'lgan ma'lumotlarga state tuzib kelasilar.
#photo va telefon raqam to'g'ri kiritilganligini tekshirib keyin o'tkazuvchi stateni qilib ko'rsataman.

@dp.message(Form.home_number,F.text)
async def home_number_get(message:Message,state:FSMContext):
    number = message.text
    if number.isdigit():
        await state.update_data(home_number=number)

        await state.set_state(Form.address)
        text = f"Manzilingizni kiriting!"
        await message.reply(text=text)
    else:
        await message.reply("Noto'g'ri")

@dp.message(Form.home_number)
async def not_hom_number(message:Message,state:FSMContext):
    await message.reply("Text ko'rinishida ma'lumot kiriting")



@dp.message(Form.address)
async def get_address(message:Message,state:FSMContext):

    address = message.text
    await state.update_data(address=address)

    data = await state.get_data()
    
    my_photo = data.get("photo") #rasmni qabul qilib olish
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    phone_number = data.get("phone_number")
    address = data.get("address")
    telegram_id = message.from_user.id
    try:
        connection = sqlite3.connect("sqlite.db")
        cursor = connection.cursor()
        command = f"""
            INSERT INTO USERS('first_name','last_name','phone_number','telegram_id')
            VALUES('{first_name}','{last_name}','{phone_number}','{telegram_id}');
        """
        cursor.execute(command)
        connection.commit()
    except:
        pass
    
    text = f"<b>Ariza</b>\nIsmi:  {first_name}\nFamilyasi:  {last_name}\nTel:  {phone_number}\nManzil:  {address}"
    
    #adminga ariza ma'lumotlarini yuboramiz

    await bot.send_photo(ADMIN,photo=my_photo,caption=text)
    # print(first_name,last_name,phone_number,address)
    
    await state.clear()
    text = f"Siz muvaffaqiyatli tarzda ro'yhatdan o'tdingiz🎉"
    await message.reply(text=text)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())