from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove


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

course_button = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Frontend"),
        KeyboardButton(text="Backend"),
            
        ],
        
    ],
    resize_keyboard=True,
    input_field_placeholder="Tugmalardan birini tanlang"
)

