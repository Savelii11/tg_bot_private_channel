from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp, router
from aiogram.filters import Command
from keyboards.inline.products_from_cart import price_markup
from states import Dialogue_state
from aiogram import types, F
import requests
from data.config import SUBSCRIPTONS_SERVICE_API_URL


'''@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)

    await message.answer('Меню', reply_markup=markup)'''

@router.message(Command(commands=['start']))
async def start_dialogue(message: Message, state: FSMContext):
    #await Dialogue_state.view_subscription.set()
    await message.answer("Привет, этот бот дает возможность оплатить доступ в клуб «Баффеты на Уораннах»Наш клуб это не просто место, где вы сможете получить инструменты и идеи, для увеличения своего заработка. Это сообщества, где вы всегда получите обратную связь, поддержку, общение с единомышленниками. Что Вам даст клуб? - Прибыльный долгосрочный портфель- Заработок на торговых сетапахАналитику рынкаЗакрытые материалыОбщениеЕженедельные дайджесты",
                         reply_markup=price_markup())
    
    # Data to send in the POST request
    data = {
        'telegram_id': message.from_user.id,
        'chat_id': message.chat.id,
        'telegram_username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
    }

    # Sending the POST request
    response = requests.post(url=SUBSCRIPTONS_SERVICE_API_URL, data=data)

    # Checking the response status code
    if response.status_code == 201:
        await message.answer("Вы успешно зарегестрированы!")
    else:
        await message.answer("Вы уже в БД")
    
    await state.set_state(Dialogue_state.view_subscription)

@router.callback_query(F.data == 'two_days')
async def process_watch_btn(callback: CallbackQuery):
    await callback.message.answer("Подписка на 2 дня за 19 евро!")

'''@router.callback_query(lambda query: query.data in ['two_days', 'one_week'])
async def handle_subscription_query(query: types.CallbackQuery):
    print("CALLOUT")
    await query.answer()  # Optional: Acknowledge the query
    if query.data == 'two_days':
        await query.message.answer("You chose 2 дня - 19 евро")
    elif query.data == 'one_week':
        await query.message.answer("You chose Неделя - 50 евро")

    await Dialogue_state.next().set()'''