import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from data import config
from filters.admin import IsBotAdminFilter 


ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN

dp = Dispatcher()
# bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    print(message.from_user.id)
    await message.answer(text="Assalomu alaykum")

@dp.message(F.text,IsBotAdminFilter(ADMINS))
async def user_funksiyasi(message:Message):
    await message.answer("Tabriklaymiz siz adminsiz⭐️")

@dp.message(F.text)
async def admin_funksiyasi(message:Message):
    await message.answer("Afsuski siz admin emassiz😔")


#bot ishga tushganini xabarini yuborish

async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await on_startup_notify(bot)
    await dp.start_polling(bot)
    
    


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())