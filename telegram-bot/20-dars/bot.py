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
from filters.check_sub_channel import IsCheckSubChannels

ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN

dp = Dispatcher()

#forward qilingan xabarlar chat id sini oladi
# @dp.message(F.forward_from_chat)
# async def check_channel_id(message:Message):
#     await message.answer(f"CHannel id: {message.forward_from_chat.id}")

@dp.message(IsCheckSubChannels())
async def is_check_sub_channel(message:Message):
    await message.answer(text="Botdan foydalanishingiz mumkin")



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

#bot ishga tushganini xabarini yuborish
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await on_startup_notify(bot)
    await dp.start_polling(bot)
    await off_startup_notify(bot)
    
    


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())