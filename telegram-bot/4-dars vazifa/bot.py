import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession #new
from wiki import wiki_malumot

session = AiohttpSession(proxy='http://proxy.server:3128') #new

TOKEN = "6962596717:AAH6EuGxYtxyAidzaVqS1WGezffgktFfvQg"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name}\n Bu bot ismingizni ma'nosini topib beradi. Isminigizni kiriting !!!"
    await message.reply(text=text)

@dp.message(F.text)
async def name(message:Message):
    malumot = message.text
    natija = wiki_malumot(malumot=malumot)

    await message.answer(text=natija)

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML,session=session) #new
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())