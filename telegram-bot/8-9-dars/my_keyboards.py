from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,KeyboardButtonPollType
#yangi
from aiogram.utils.keyboard import ReplyKeyboardBuilder



#button yaratish 1-usul
# menu_button = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Maktab"),
#             #5ta maktab qo'shishilar kerak misol:1-Maktab, 4-Maktab
#         ],
        

#         [   #Bu tugmani bosganda o'ziz xaqizda ma'lumot chiqsin
#             KeyboardButton(text="Biz haqimizda👨🏻‍💻"),
            
#         ],
#     ],
#    resize_keyboard=True,
#    input_field_placeholder="Menudan birini tanlang"
# )

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Fayozbek"),KeyboardButton(text="1"),KeyboardButton(text="1")],
        [KeyboardButton(text="2"),KeyboardButton(text="2")],

        [KeyboardButton(text="3"),KeyboardButton(text="3")],


    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)




#button yaratish 2-usul
names = [
    "Ozodbek",
    "Asliddin",
    "Qobil",
    "Asilbek",
    "Sardor",
    "Boburjon",
    "Otabek",
    "Shuhrat",
    "Gulhayo",
    "Sunnat",
    "Maqsud",
    "Nurbek",
    "Behruz",
    "Sitora"
]

eng_uz_colors = {
    "red": "qizil",
    "blue": "ko'k",
    "green": "yashil",
    "yellow": "sariq",
    "orange": "orol",
    "purple": "binafsha",
    "pink": "pushti",
    "brown": "jigarrang",
    "gray": "kulrang",
    "black": "qora",
    "white": "oq"
    # Add more colors as needed
}

def auto_keyboard():
    builder2 = ReplyKeyboardBuilder()

    for color in eng_uz_colors.keys():

        builder2.add(KeyboardButton(text=color))

    builder2.adjust(2)

    return builder2


#button yaratish 3-usul

builder3 = ReplyKeyboardBuilder()
# Qator usuli sizga aniq qator yaratish imkonini beradi
# bir yoki bir nechta tugmalardan. Masalan, birinchi qator
# ikkita tugmadan iborat bo'ladi ...
builder3.row(
    KeyboardButton(text="Manzil yuborish", request_location=True),
    KeyboardButton(text="Kontakt yuborish", request_contact=True)
)
# ... ikkinchisi ...
builder3.row(KeyboardButton(
    text="Viktorina yaratish",
    request_poll=KeyboardButtonPollType(type="quiz"))
)