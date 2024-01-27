from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menu")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Asosiy menu"
)
