import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.context import FSMContext
from inlinebutton import inline_menu,course_button #new
from aiogram.types import ReplyKeyboardRemove

ADMIN = 999588837 # Bu yerga id kiriting

TOKEN = "6962596717:AAH6EuGxYtxyAidzaVqS1WGezffgktFfvQg" #Token kiriting
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

#new
@dp.message(F.text=="/menu")
async def my_menu(message:Message):
    photo = "https://i.pinimg.com/736x/e5/94/02/e594028fbe30b388e76a49d4d19523a5.jpg"
    # await message.answer(text="Asosiy menu",reply_markup=inline_menu)
    await message.answer_photo(photo=photo,caption="Sifat o'quv markazi",reply_markup=inline_menu)

# @dp.message(F.location)
# async def my_location(message:Message):
#     latitude = message.location.latitude
#     longitude = message.location.longitude
#     text = f"latitude={latitude},longitude={longitude}"
#     await message.answer(text)

@dp.callback_query(F.data=="address")
async def my_address(callback:CallbackQuery):
    await callback.answer("Sifat Manzil")
    latitude=40.102467
    longitude=65.373444
    await callback.message.answer("Sifat o'quv markazi manzili")
    await callback.message.answer_location(latitude=latitude,longitude=longitude)

@dp.callback_query(F.data=="course")
async def me_course(callback:CallbackQuery):
    
    await callback.message.answer(text = "Sifat o'quv kurslari, Kurslardan birini tanlang",reply_markup=course_button)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())