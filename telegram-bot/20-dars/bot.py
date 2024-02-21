import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command,and_f
from aiogram import F
from aiogram.types import Message, ChatPermissions
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

# @dp.message(IsCheckSubChannels())
# async def is_check_sub_channel(message:Message):
#     await message.answer(text="Botdan foydalanishingiz mumkin")

# @dp.message(F.chat.func(lambda chat: chat.type == "supergroup"))
# async def test(message:Message):
#     text = f"""
# chat type: {message.chat.type}\n
# chat id: {message.chat.id}\n
# chat name: {message.chat.full_name}
# """
#     await message.answer(text=text)

@dp.message(F.new_chat_member)
async def new_member(message:Message):
    user = message.new_chat_member.get("first_name")
    await message.answer(f"{user} Guruhga xush kelibsiz!")
    await message.delete()

@dp.message(F.left_chat_member)
async def new_member(message:Message):
    # print(message.new_chat_member)
    user = message.left_chat_member.full_name
    await message.answer(f"{user} Xayr!")
    await message.delete()

@dp.message(and_f(F.reply_to_message,F.text=="/ban"))
async def ban_user(message:Message):
    user_id =  message.reply_to_message.from_user.id
    await message.chat.ban_sender_chat(user_id)
    await message.answer(f"{message.reply_to_message.from_user.first_name} guruhdan chiqarib yuborilasiz.")

@dp.message(and_f(F.reply_to_message,F.text=="/unban"))
async def unban_user(message:Message):
    user_id =  message.reply_to_message.from_user.id
    await message.chat.unban_sender_chat(user_id)
    await message.answer(f"{message.reply_to_message.from_user.first_name} guruhga qaytishingiz mumkin.")

from time import time
@dp.message(and_f(F.reply_to_message,F.text=="/mute"))
async def mute_user(message:Message):
    user_id =  message.reply_to_message.from_user.id
    permission = ChatPermissions(can_send_messages=False)

    until_date = int(time()) + 60 # 1minut guruhga yoza olmaydi
    await message.chat.restrict(user_id=user_id,permissions=permission,until_date=until_date)
    await message.answer(f"{message.reply_to_message.from_user.first_name} 1 minutga blocklandingiz")

@dp.message(and_f(F.reply_to_message,F.text=="/unmute"))
async def unmute_user(message:Message):
    user_id =  message.reply_to_message.from_user.id
    permission = ChatPermissions(can_send_messages=True)
    await message.chat.restrict(user_id=user_id,permissions=permission)
    await message.answer(f"{message.reply_to_message.from_user.first_name} guruhga yoza olasiz")


from time import time
xaqoratli_sozlar = {"tentak","jinni"}
@dp.message(and_f(F.chat.func(lambda chat: chat.type == "supergroup"),F.text ))
async def tozalash(message:Message):
    text = message.text
    print(text)
    for soz in xaqoratli_sozlar:
        print(soz,text.lower().find(soz))
        if text.lower().find(soz)!=-1 :
            user_id =  message.from_user.id
            until_date = int(time()) + 60 # 1minut guruhga yoza olmaydi
            permission = ChatPermissions(can_send_messages=False)
            await message.chat.restrict(user_id=user_id,permissions=permission,until_date=until_date)
            await message.answer(text=f"{message.from_user.mention_html()} guruhda so'kinganingiz uchun 1 minutga blokga tushdingiz")
            await message.delete() 
            break
    






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
@dp.startup()
async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)

#bot ishga tushganini xabarini yuborish
@dp.shutdown()
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())