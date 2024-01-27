from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

#1-usul
inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Sifat o'quv kurslari",callback_data='course')],

        [InlineKeyboardButton(text="Bizning manzil",callback_data='address'),
         InlineKeyboardButton(text="Biz haqimizda",callback_data='about')
         ],
         [
             InlineKeyboardButton(text="Admin bilan bog'lanish",callback_data="admin")
         ]
    ]
)

# 2-usul

course_button = InlineKeyboardBuilder()
course_button.add(InlineKeyboardButton(text="🖼 Frontend",callback_data="frontend"))
course_button.add(InlineKeyboardButton(text="💻 Backend",callback_data="backend"))
course_button.add(InlineKeyboardButton(text="Online kurslarimiz",url="https://www.youtube.com/watch?v=kqtD5dpn9C8"))
course_button.add(InlineKeyboardButton(text="🔙 ortga",callback_data="back"))
course_button.adjust(2)

#3-usul
ortga_button = InlineKeyboardBuilder()
ortga_button.row(InlineKeyboardButton(text="🔙 ortga",callback_data="course"))
