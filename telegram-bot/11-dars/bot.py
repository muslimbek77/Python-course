import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.context import FSMContext
from inlinebutton import inline_menu,course_button,ortga_button #new
from aiogram.types import ReplyKeyboardRemove,input_file
from keyboard_button import main_menu_button #new
from aiogram.types import FSInputFile
ADMIN = 999588837 # Bu yerga id kiriting

TOKEN = "6962596717:AAH6EuGxYtxyAidzaVqS1WGezffgktFfvQg" #Token kiriting
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def start_bot(message:Message):
    # await message.answer_video(video = FSInputFile("video.mp4"))
    await message.answer("Bizning botimizga hush kelibsiz!",reply_markup=main_menu_button)

#new
@dp.message(F.text=="Menu")
async def my_menu(message:Message):
    photo = "https://i.pinimg.com/736x/e5/94/02/e594028fbe30b388e76a49d4d19523a5.jpg"
    # await message.answer(text="Asosiy menu",reply_markup=inline_menu)
    await message.answer_photo(photo=photo,caption="Sifat o'quv markazi",reply_markup=inline_menu)

#ortga qaytarish
@dp.callback_query(F.data=="back")
async def ortga_funksiyasi(callback:CallbackQuery):
    photo = "https://i.pinimg.com/736x/e5/94/02/e594028fbe30b388e76a49d4d19523a5.jpg"
    
    await callback.message.answer_photo(photo=photo,caption="Sifat o'quv markazi",reply_markup=inline_menu)
    await callback.message.delete()



@dp.callback_query(F.data=="address")
async def my_address(callback:CallbackQuery):
    await callback.answer("Sifat Manzil")
    latitude=40.102467
    longitude=65.373444
    await callback.message.answer("Sifat o'quv markazi manzili")
    await callback.message.answer_location(latitude=latitude,longitude=longitude)

@dp.callback_query(F.data=="course")
async def me_course(callback:CallbackQuery):
    
    await callback.message.edit_caption(caption = "Sifat o'quv kurslari, Kurslardan birini tanlang",reply_markup=course_button.as_markup())

@dp.callback_query(F.data=="frontend")
async def frontend_course(callback:CallbackQuery):
    frontend_photo = "https://s.dou.ua/storage-files/how-to-front-end.jpg"
    await callback.message.answer_photo(photo=frontend_photo,caption="Frontend haqida ma'lumot",reply_markup=ortga_button.as_markup())
    await callback.message.delete()




async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())