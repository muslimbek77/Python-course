import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,FSInputFile
from aiogram import F
from my_yutube import yutube_save
from my_insta import insta_save


TOKEN = "6962596717:AAH6EuGxYtxyAidzaVqS1WGezffgktFfvQg"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, Botimiz sizga youtubdan video olib beradi.\nBotdan foydalanish uchun link yuboring")


@dp.message(F.text.contains("www.youtube.com"))
async def yutube_download(message:Message):
    result = yutube_save(message.text)
    video = FSInputFile(result)
    await message.answer_video(video=video,caption="@uz12345_bot")
    # await message.answer("siz yutube link yubordingiz")

@dp.message(F.text.contains("instagram"))
async def instagram_download(message:Message):
    result = insta_save(message.text)
    # photo = FSInputFile(result)
    await message.answer_photo(photo=result,caption="@uz12345_bot")
    # await message.answer("siz yutube link yubordingiz")

@dp.message()
async def other_thins(message:Message):
    await message.answer("Youtube link yuboring")

async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())