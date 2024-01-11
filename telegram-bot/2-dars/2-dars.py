import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from cat import get_cat
TOKEN = "6962596717:AAGws9oAuKEpz9m4zwp3K_Y7CnAJbV4_L1c"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = message.from_user.full_name
    print(message.text)
    await message.reply(f"Hello,{full_name}")


@dp.message(F.text.contains("/cat"))
async def cat_image_send(message:Message):
        photo = get_cat(message.text[4:])
        await message.answer_photo(photo=types.input_file.BufferedInputFile(photo,filename="cat.png"))
    

async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())