import os
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp, router
from aiogram.filters import Command, StateFilter
from keyboards.inline.dialogue_markup import subscription_markup, subscription_showing_markup, payed_for_sub_markup
from keyboards.menu_keyboards.my_subs_markup import view_sub_markup
from states import Dialogue_state
from aiogram import types, F
from lexicon.lexicon_ru import LEXICON_RU
import requests
from data.config import SUBSCRIPTONS_SERVICE_API_URL, USERS_SERVICE_API_URL
import telegram
from aiogram.enums.parse_mode import ParseMode
import aiofiles
from aiogram.types import InputFile
import json


load_dotenv()
class Plan:
    subscription = ''

    def __init__(self, subscription):
        self.subscription = subscription

SUBSCRIPTONS_SERVICE_API_URL = os.getenv("SUBSCRIPTONS_SERVICE_API_URL")
USERS_SERVICE_API_URL = os.getenv("USERS_SERVICE_API_URL")
users_sub = Plan(subscription='null')

@router.message(F.text=='Закрытый канал')
async def show_private_channel(message: Message, state: FSMContext):
    await message.answer_photo(photo=types.FSInputFile(path='media/description.JPG'),
                               caption = LEXICON_RU['present_private_channel'])

    await state.set_state(Dialogue_state.view_subscription)

@router.message(F.text == "Моя подписка")
async def show_my_subscription(message: Message, state: FSMContext):
    await state.set_state(Dialogue_state.view_subscription)
    url = f"https://buffetsbot.com/api/v1/subscriptions/?telegram_username={message.from_user.username}"
    print(url)
    print(message.from_user.username)
    request = requests.get(url=url)

    response_details = json.loads(request.text)
    print(response_details)
    if request.text[12:24] == "Subscription":

        await message.answer_photo(photo=types.FSInputFile(path='media/personal.JPG'), caption=LEXICON_RU["no_subscription"])


    else:
        subs_info = (
            LEXICON_RU["present_subscription"]
            + "\n"
            + "Дата начала: "
            + response_details["start_date"]
            + "\n"
            + "Дата окончания подписки: "
            + response_details["end_date"]
            + "\n"
            + "Цена: "
            + str(response_details["price"])
            + "$"
        )
        await message.answer_photo(photo=types.FSInputFile(path='media/personal.JPG'),
                                   caption=subs_info)

@router.message(Command(commands=['start']))
async def start_dialogue(message: Message, state: FSMContext):
    await state.set_state(Dialogue_state.view_subscription)
    data = {
        'telegram_id': message.from_user.id,
        'chat_id': message.chat.id,
        'telegram_username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
    }
    users_sub.subscription = 'null'
    # Sending the POST request

    response = requests.post(url=USERS_SERVICE_API_URL, data=data)
    print(response.text)
    await message.answer_photo(photo =types.FSInputFile(path='media/main_image.JPG'), caption = LEXICON_RU['/start'], reply_markup=view_sub_markup())
    await message.answer(text = LEXICON_RU['additional_help'])

    await message.answer(text = LEXICON_RU['choose_subscription'],reply_markup=subscription_markup())





@router.callback_query(StateFilter(Dialogue_state.view_subscription) and F.data=="subs_two_days")
async def two_day_subs(callback: CallbackQuery, state: FSMContext):
    users_sub.subscription = '2 days'

    await callback.message.edit_text(text = (LEXICON_RU['two_day_sub']+LEXICON_RU['paying_for_subscription']), reply_markup=subscription_showing_markup())
    await state.set_state(Dialogue_state.pay_for_subscription)


@router.callback_query(StateFilter(Dialogue_state.view_subscription), F.data=="subs_one_month")
async def one_month_subs(callback: CallbackQuery, state: FSMContext):
    users_sub.subscription = '1 month'
    await callback.message.edit_text(text = (LEXICON_RU['one_month_sub']+LEXICON_RU['paying_for_subscription']), reply_markup=subscription_showing_markup(), parse_mode=ParseMode.HTML)
    await state.set_state(Dialogue_state.pay_for_subscription)


@router.callback_query(StateFilter(Dialogue_state.view_subscription), F.data=="subs_three_months")
async def three_months_subs(callback: CallbackQuery, state: FSMContext):
    users_sub.subscription = '3 months'
    await callback.message.edit_text(text = (LEXICON_RU['three_months_sub']+LEXICON_RU['paying_for_subscription']), reply_markup=subscription_showing_markup())
    await state.set_state(Dialogue_state.pay_for_subscription)

@router.callback_query(StateFilter(Dialogue_state.view_subscription), F.data=="subs_six_months")
async def six_months_subs(callback: CallbackQuery, state: FSMContext):
    users_sub.subscription = '6 months'
    await callback.message.edit_text(text = (LEXICON_RU['six_months_sub']+LEXICON_RU['paying_for_subscription']), reply_markup=subscription_showing_markup())
    await state.set_state(Dialogue_state.pay_for_subscription)

@router.callback_query(StateFilter(Dialogue_state.view_subscription), F.data=="subs_one_year")
async def one_year_subs(callback: CallbackQuery, state: FSMContext):
    users_sub.subscription = '1 year'
    await callback.message.edit_text(text = (LEXICON_RU['one_year_sub']+LEXICON_RU['paying_for_subscription']), reply_markup=subscription_showing_markup())

    await state.set_state(Dialogue_state.pay_for_subscription)



@router.callback_query(F.data=="back")
async def one_year_subs(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text = LEXICON_RU['choose_subscription'], reply_markup=subscription_markup())
    await state.set_state(Dialogue_state.view_subscription)

@router.callback_query(F.data=="payed_for")
async def one_year_subs(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text = LEXICON_RU["payed_for_subscription"], reply_markup=payed_for_sub_markup(), parse_mode=ParseMode.HTML)
    print(users_sub.subscription)
    await state.set_state(Dialogue_state.check_hash)

@router.message(StateFilter(Dialogue_state.check_hash) and F.text!='Закрытый канал' and F.text != "Моя подписка")
async def waiting_for_confirmation(message: Message, state: FSMContext):
    transaction_hash = message.text
    print(transaction_hash)
    data = {
        'telegram_username': message.from_user.username,
        'transaction_hash' : transaction_hash,
        'plan':users_sub.subscription,
    }
    response = requests.post(url=SUBSCRIPTONS_SERVICE_API_URL, data=data)
    print(response.text)
    await message.answer(text=LEXICON_RU['checking_hash'], reply_markup=payed_for_sub_markup())

    response_details = json.loads(response.text)
    if(response_details['status']==400):
        await message.answer(text = LEXICON_RU['subs_unsuccessful'])
    else:
        await message.answer(text=LEXICON_RU['subs_successful'])
    await state.set_state(Dialogue_state.waiting_message)

@router.message(Command(commands=['help']))
async def show_private_channel(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['contacts'])