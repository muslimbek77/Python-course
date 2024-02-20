# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,KeyboardButtonPollType
# #yangi
# from aiogram.utils.keyboard import ReplyKeyboardBuilder

# #button yaratish 3-usul

# builder3 = ReplyKeyboardBuilder()
# # Qator usuli sizga aniq qator yaratish imkonini beradi
# # bir yoki bir nechta tugmalardan. Masalan, birinchi qator
# # ikkita tugmadan iborat bo'ladi ...
# builder3.row(
#     KeyboardButton(text="Manzil yuborish", request_location=True),
#     KeyboardButton(text="Kontakt yuborish", request_contact=True)
# )
# # ... ikkinchisi ...
# builder3.row(KeyboardButton(
#     text="Viktorina yaratish",
#     request_poll=KeyboardButtonPollType(type="quiz"))
# )
# button = builder3.as_markup(resize_keyboard=True)


from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="Bizning kurslar",callback_data="courses"),
    InlineKeyboardButton(text="Bizning manzil",callback_data="location"),],

    [InlineKeyboardButton(text="Biz haqimizda",callback_data="about-us"),],

    [InlineKeyboardButton(text="Admin bilan bog'lanish",callback_data="contact-admin"),]

    ]
)

courses_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="Frontend",callback_data="frontend"),
    InlineKeyboardButton(text="Backend",callback_data="backend"),],

    [InlineKeyboardButton(text="Online kurslar",url="https://www.youtube.com/watch?v=D9LwKc223t4"),],

    ]
)

#ikkinchi usul
# numbers = InlineKeyboardBuilder()

# for number in range(1,16):
#     numbers.add(InlineKeyboardButton(text=f"{number}",callback_data=f"{number}"))

# numbers.adjust(2)

# num_inline_menu = numbers.as_markup()