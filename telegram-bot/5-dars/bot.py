import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
import io
from remove_bg import removebg

TOKEN = "6962596717:AAGws9oAuKEpz9m4zwp3K_Y7CnAJbV4_L1c"
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name}\nBu bot rasm orqa fonini o'chirib beradi. Botdan foydalanish uchun rasm yuboring!!!"
    await message.reply(text=text)



@dp.message(F.photo)
async def name(message:Message):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = removebg(photos_url)
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-remove.png"))
        await message.answer_document(document=types.input_file.BufferedInputFile(rasm,filename="no-remove.png"))

@dp.message()
async def text_message(message:Message):
    message.answer("Iltimos, rasm yuboring!!!")

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())