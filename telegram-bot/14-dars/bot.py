import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,FSInputFile,InputMediaPhoto
from aiogram import F
from tik_tok import tiktok_save


TOKEN = "6962596717:AAH6EuGxYtxyAidzaVqS1WGezffgktFfvQg"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, Botimiz sizga youtubdan video olib beradi.\nBotdan foydalanish uchun link yuboring")



@dp.message(F.text.contains("tiktok"))
async def tiktok_download(message:Message):
    link = message.text
    tiktok = tiktok_save(link)
    video = tiktok.get("video")
    music = tiktok.get("music")
    rasmlar = tiktok.get("images")

    if rasmlar:
        #1-usul
        # for i,rasm in enumerate(rasmlar):
        #     await message.answer_photo(photo=rasm,caption=f"{i+1}-rasm")

        #2-usul
        rasm = []
        for i,r in enumerate(rasmlar):
            rasm.append(InputMediaPhoto(media=r))
            if (i+1)%10==0:
                await message.answer_media_group(rasm)
                rasm=[]
        if rasm:
            await message.answer_media_group(rasm)
    elif video:
        await message.answer_video(video=video,caption="Bizning bot")
    if music:
        await message.answer_audio(audio=music)
    


        


async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())