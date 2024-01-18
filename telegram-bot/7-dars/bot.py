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

ADMIN = 999588837
TOKEN = "6962596717:AAH8rK6QXNil4On5IeRbp5MfCSxIXf8cmbs"
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message,state:FSMContext) -> None:
    await state.set_state(Form.first_name)
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name} Sifat botiga hush kelibsiz\nRo'yhatdan o'tish uchun ismingizni kiriting!"
    await message.reply(text=text)

@dp.message(Form.first_name)
async def get_first_name(message:Message,state:FSMContext):

    first_name = message.text
    await state.update_data(first_name=first_name)

    await state.set_state(Form.last_name)
    text = f"Familyangizni kiriting!"
    await message.reply(text=text)

@dp.message(Form.last_name)
async def get_last_name(message:Message,state:FSMContext):

    last_name = message.text
    await state.update_data(last_name=last_name)

    await state.set_state(Form.phone_number)
    text = f"Telefon nomeringizni kiriting!"
    await message.reply(text=text)

@dp.message(Form.phone_number)
async def get_phone_number(message:Message,state:FSMContext):

    phone_number = message.text
    await state.update_data(phone_number=phone_number)

    await state.set_state(Form.address)
    text = f"Manzilingizni kiriting!"
    await message.reply(text=text)

@dp.message(Form.address)
async def get_address(message:Message,state:FSMContext):

    address = message.text
    await state.update_data(address=address)

    data = await state.get_data()
    
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    phone_number = data.get("phone_number")
    address = data.get("address")
    text = f"Ariza:\nIsmi:{first_name}\nFamilyasi:{last_name}\nTel:{phone_number}\nManzil:{address}"
    await bot.send_message(ADMIN,text)
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