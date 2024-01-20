from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#button yaratish
menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Maktab 🎒"),
            #5ta maktab qo'shishilar kerak misol:1-Maktab, 4-Maktab
        ],
        [   #Bu tugmani bosganda o'ziz xaqizda ma'lumot chiqsin
            KeyboardButton(text="Biz haqimizda👨🏻‍💻"),
        ],
    ],
    resize_keyboard=True,
)