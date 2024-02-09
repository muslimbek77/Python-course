import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F

TOKEN = "6841416417:AAEGzxAPm0JHbr48dwYKy_Vw9C28coSeXYk"
dp = Dispatcher()

@dp.message(F.text)
async def start_handler(message: Message):
    user = message.from_user.full_name
    await message.answer(text=f"{user} siz tekst yubordingiz")

@dp.message(F.dice)
async def send_dice(message:Message):
    user = message.from_user.full_name
    dice = message.dice.emoji
    await message.answer(text=f"{user} siz {dice} emoji yubordingiz")

#vazifa(video,photo,contact,game,poll,location,sticker,animation,document,mp3)

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())



# import requests

# response = requests.get("https://api.telegram.org/bot6841416417:AAEGzxAPm0JHbr48dwYKy_Vw9C28coSeXYk/getMe")

# if response.status_code==200:
#     print(response.content.decode())

# message = input("xabar kiriting: ")

# url = f"https://api.telegram.org/bot6841416417:AAEGzxAPm0JHbr48dwYKy_Vw9C28coSeXYk/sendMessage?chat_id=-1002022943392&text={message}"


# requests.get(url)

# #rasm yuborish
# # API_KEY = "------"
# # chat_id = 999588837
# # photo = "https://www.linearity.io/blog/content/images/2023/06/how-to-create-a-car-NewBlogCover.png"
# # url = f"https://api.telegram.org/bot{API_KEY}/sendPhoto?chat_id={chat_id}&photo={photo}"
# # requests.get(url)

