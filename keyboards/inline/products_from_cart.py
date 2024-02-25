from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData



def price_markup():

    two_days = 'two_days'
    one_week= 'one_week'

    two_days_button = InlineKeyboardButton(text='2 дня - 19 евро', callback_data=two_days)
    one_week_button = InlineKeyboardButton(text='Неделя - 50 евро', callback_data=one_week)


    markup = InlineKeyboardMarkup(
        inline_keyboard=[[two_days_button],
                         [one_week_button]]
    )


    return markup