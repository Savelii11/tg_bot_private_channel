from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData



def subscription_markup():

    two_days = 'subs_two_days'
    one_month = 'subs_one_month'
    three_months = 'subs_three_months'
    six_months = 'subs_six_months'
    one_year = 'subs_one_year'

    two_days_button = InlineKeyboardButton(text='2 дня - 19 долларов', callback_data=two_days)
    one_month_button = InlineKeyboardButton(text='Месяц - 150 долларов', callback_data=one_month)
    three_months_button = InlineKeyboardButton(text='3 месяца - 400 долларов', callback_data=three_months)
    six_months_button = InlineKeyboardButton(text='6 месяцев - 600 долларов', callback_data=six_months)
    one_year_button = InlineKeyboardButton(text='1 год - 1000 долларов', callback_data=one_year)

    markup = InlineKeyboardMarkup(
        inline_keyboard=[[two_days_button],
                         [one_month_button],
                         [three_months_button],
                         [six_months_button],
                         [one_year_button]]
    )


    return markup


def subscription_showing_markup():

    payed_for = 'payed_for'
    go_back = 'back'


    pay_button = InlineKeyboardButton(text='Я оплатил подписку', callback_data=payed_for)
    go_back_button= InlineKeyboardButton(text='Вернуться назад', callback_data=go_back)

    markup = InlineKeyboardMarkup(
        inline_keyboard=[[pay_button],
                         [go_back_button]]
    )


    return markup

def payed_for_sub_markup():
    go_back = 'back'
    go_back_button = InlineKeyboardButton(text='Вернуться назад', callback_data=go_back)

    markup = InlineKeyboardMarkup(
        inline_keyboard=[[go_back_button]]
    )

    return markup
