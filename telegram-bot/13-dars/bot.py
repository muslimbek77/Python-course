import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,FSInputFile
from aiogram import F
from insta import insta_save


TOKEN = "6962596717:AAH6EuGxYtxyAidzaVqS1WGezffgktFfvQg"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, Botimiz sizga youtubdan video olib beradi.\nBotdan foydalanish uchun link yuboring")



@dp.message(F.text.contains("instagram"))
async def instagram_download(message:Message):
    link = message.text
    result = insta_save(link)
    if result[0]=="video":
        await message.answer_video(video=result[1])
    elif result[0]=="rasm":
        await message.answer_photo(photo=result[1])
    else:
        await message.answer("Notog'ri link yubordingiz")

async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())