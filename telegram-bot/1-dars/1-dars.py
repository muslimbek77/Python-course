# import asyncio
# import logging
# import sys
# import cat
# from aiogram import Bot, Dispatcher
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart,Command
# from aiogram.types import Message

# TOKEN = "6962596717:AAGws9oAuKEpz9m4zwp3K_Y7CnAJbV4_L1c"
# dp = Dispatcher()

# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     await message.answer(f"Hello")

# @dp.message(Command(commands="cat"))
# async def cat_image_send(message:Message):
#     photo = cat.get_cat_image()
#     await message.answer_photo(photo="https://cataas.com/cat")
    

# async def main() -> None:

#     bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())



import requests

# response = requests.get("https://api.telegram.org/bot6841416417:AAEGzxAPm0JHbr48dwYKy_Vw9C28coSeXYk/getMe")

# if response.status_code==200:
#     print(response.content.decode())

# message = input("xabar kiriting: ")

# url = f"https://api.telegram.org/bot6841416417:AAEGzxAPm0JHbr48dwYKy_Vw9C28coSeXYk/sendMessage?chat_id=-1002022943392&text={message}"


# requests.get(url)

#rasm yuborish
API_KEY = "------"
chat_id = 999588837
photo = "https://www.linearity.io/blog/content/images/2023/06/how-to-create-a-car-NewBlogCover.png"
url = f"https://api.telegram.org/bot{API_KEY}/sendPhoto?chat_id={chat_id}&photo={photo}"
requests.get(url)
