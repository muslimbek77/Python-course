import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,CallbackQuery
from mybuttons import inline_menu,courses_menu



TOKEN = "6161514516:AAH6BjrgxVh2w-zx3pxQIOBxPuyUMmFckpQ" #Token kiriting
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Assalomu alaykum",reply_markup=inline_menu)


@dp.callback_query(F.data=="courses")
async def bizning_kurslar(callback:CallbackQuery):
    

    await callback.answer("Bizning kurslar")

    await callback.message.answer("Bizning kurslar: ",reply_markup=courses_menu)
    await callback.message.delete()


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
