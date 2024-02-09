import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from cat import get_cat
from design import art_image

TOKEN = "6841416417:AAEGzxAPm0JHbr48dwYKy_Vw9C28coSeXYk"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = message.from_user.full_name
    print(message.text)
    await message.reply(f"Hello.{full_name}")


@dp.message(F.text.contains("/cat"))
async def cat_image_send(message:Message):
        photo = get_cat(message.text[4:])
        await message.answer_document(document=types.input_file.BufferedInputFile(photo,filename="cat.png"))


@dp.message(Command(commands="art"))
async def art_design_photo(message:Message):
     data = art_image()
     image = data.get("image")
     culture = data.get("culture")
     museum = data.get("museum")
     text = f"Culture:{culture}\nMuseum:{museum}"
     text = f"<tg-spoiler>{text}</tg-spoiler>"
     #country,dimensions,geographyType,accessionYear

     if image:
          await message.answer_photo(photo=image,caption=text,has_spoiler=True)
     else:
          await message.answer(text=text)




async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())