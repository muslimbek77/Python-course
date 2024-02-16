import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext #new
from states import Form #new
import re


TOKEN = "6161514516:AAFDc54ZGIIj83aqgPkH1mvAWpD-H35vaI8" #Token kiriting
ADMIN = 999588837
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message,state:FSMContext):
    
    await state.set_state(Form.first_name)
    await message.answer(text="Assalomu alaykum, Ro'yhatdan o'tish uchun ismingizni kiriting")

@dp.message(F.text,Form.first_name)
async def first_name_register(message:Message,state:FSMContext):
    ism = message.text
    await state.update_data(first_name=ism)
    await state.set_state(Form.last_name)

    await message.answer(text="Familyangizni kiriting")

@dp.message(F.text,Form.last_name)
async def last_name_register(message:Message,state:FSMContext):
    familya = message.text
    await state.update_data(last_name = familya)
    await state.set_state(Form.phone_number)

    await message.answer(text="Tel nomeringizni kiriting")

@dp.message(F.text,Form.phone_number)
async def phone_number_register(message:Message,state:FSMContext):
    tel = message.text
    pattern = re.compile("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
    if pattern.match(tel):
        await state.update_data(phone_number = tel)
        await state.set_state(Form.address)
        await message.answer(text="Manzilingizni kiriting")
    else:
        await message.answer(text="Tel nomeringiz noto'g'ri, Iltimos qayta kiriting")

    


@dp.message(F.text,Form.address)
async def address_register(message:Message,state:FSMContext):
    manzil = message.text
    await state.update_data(address = manzil)
    data = await state.get_data()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    phone_number = data.get("phone_number")
    address = data.get("address")
    await state.clear()

    text = f"Yangi foydalanuvchi ro'yhatdan o'tdi\n\nIsmi:{first_name}\nFamilyasi:{last_name}\nTel:{phone_number}\nManzil:{address}"

    await message.answer(text="Siz muvafaqiyatli ro'yhatdan o'tdingiz")
    await bot.send_message(chat_id=ADMIN,text=text)


    





async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())