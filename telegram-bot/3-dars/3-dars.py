import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from cat import get_cat
TOKEN = "6885421621:AAFGJ-bCA0w3uSLkNIiOPZpXdQp8CxS5XdY"
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

# @dp.message()
# async def message_txt(message:Message):
#      text = message.text
#      await message.answer(text=text)

@dp.message(Command(commands="help"))
async def command_help_handler(message: Message) -> None:
    
    text = "bot kamandalari\n /start-botni ishga tushirish\n /cat-rasm chiqaradi"
    await message.reply(text)

@dp.message(F.dice)
async def message_dice(message:Message):
     
     await message.answer("BU BOTGA DICE EMOJI YUBORILDI(🎲)")

@dp.message(F.video)
async def message_video(message:Message):
     
     await message.answer("BU BOTGA VIDEO YUBORILDI(📹)")

@dp.message(F.audio)
async def message_audio(message:Message):
     
     await message.answer("BU BOTGA AUDIO YUBORILDI(🎵)")

@dp.message(F.photo)
async def message_photo(message:Message):
     
     await message.answer("BU BOTGA RASM YUBORILDI(🖻)")


@dp.message(F.location)
async def message_location(message:Message):
     
     await message.answer("BU BOTGA LOKATSIYA YUBORILDI(✆)")

@dp.message(F.animation)
async def message_animation(message:Message):
     
     await message.answer("BU BOTGA ANIMATSIYA YUBORILDI(🐿)")

@dp.message(F.document)
async def message_document(message:Message):
     
     await message.answer("BU BOTGA DOCUMENT YUBORILDI(🖺)")
     
@dp.message(F.contact)
async def message_contact(message:Message):
     
     await message.answer("BU BOTGA CONTACT YUBORILDI(📞)")

@dp.message(F.game)
async def message_game(message:Message):
     
     await message.answer("BU BOTGA O'YIN YUBORILDI(🎮)")

@dp.message(F.poll)
async def message_poll(message:Message):
     
     await message.answer("BU BOTGA POLL YUBORILDI(🈪)")

@dp.message(F.sticker)
async def message_sticker(message:Message):
     
     await message.answer("BU BOTGA STICKER YUBORILDI(😂)")

async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())