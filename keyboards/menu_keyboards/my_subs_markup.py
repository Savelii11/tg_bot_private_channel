from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




def view_sub_markup():
    button_1 = KeyboardButton(text='Моя подписка')
    markup = ReplyKeyboardMarkup(keyboard=[[button_1]], resize_keyboard=True, selective=True)


    return markup