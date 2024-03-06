from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




def view_sub_markup():
    button_1 = KeyboardButton(text='Моя подписка')
    button_2 = KeyboardButton(text='Закрытый канал')
    markup = ReplyKeyboardMarkup(keyboard=[[button_1],[button_2]], resize_keyboard=True, selective=True)


    return markup