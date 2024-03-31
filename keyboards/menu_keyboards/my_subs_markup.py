from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




def view_sub_markup():
    button_1 = KeyboardButton(text='ЛИЧНЫЙ КАБИНЕТ')
    button_2 = KeyboardButton(text='БАФФЕТЫ НА УОРАННАХ')
    button_3 = KeyboardButton(text='ВАЖНОЕ')
    button_4 = KeyboardButton(text='Вернуться в главное меню')
    markup = ReplyKeyboardMarkup(keyboard=[[button_1],[button_2], [button_3], [button_4]], resize_keyboard=True, selective=True)


    return markup