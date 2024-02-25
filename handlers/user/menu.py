from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp, router
from aiogram.filters import Command, StateFilter
from keyboards.inline.dialogue_markup import subscription_markup, subscription_showing_markup, payed_for_sub_markup
from states import Dialogue_state
from aiogram import types, F
from lexicon.lexicon_ru import LEXICON_RU



@router.message(Command(commands=['start']))
async def start_dialogue(message: Message, state: FSMContext):
    await state.set_state(Dialogue_state.view_subscription)
    await message.answer(LEXICON_RU['/start'])
    await message.answer(text = LEXICON_RU['choose_subscription'],reply_markup=subscription_markup())


@router.callback_query(StateFilter(Dialogue_state.view_subscription) and F.data=="subs_two_days")
async def two_day_subs(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text = (LEXICON_RU['two_day_sub']+LEXICON_RU['paying_for_subscription']), reply_markup=subscription_showing_markup())
    await state.set_state(Dialogue_state.pay_for_subscription)


@router.callback_query(StateFilter(Dialogue_state.view_subscription), F.data=="subs_one_month")
async def one_month_subs(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text = (LEXICON_RU['one_month_sub']+LEXICON_RU['paying_for_subscription']), reply_markup=subscription_showing_markup())
    await state.set_state(Dialogue_state.pay_for_subscription)


@router.callback_query(StateFilter(Dialogue_state.view_subscription), F.data=="subs_three_months")
async def three_months_subs(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text = (LEXICON_RU['three_months_sub']+LEXICON_RU['paying_for_subscription']), reply_markup=subscription_showing_markup())
    await state.set_state(Dialogue_state.pay_for_subscription)

@router.callback_query(StateFilter(Dialogue_state.view_subscription), F.data=="subs_six_months")
async def six_months_subs(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text = (LEXICON_RU['six_months_sub']+LEXICON_RU['paying_for_subscription']), reply_markup=subscription_showing_markup())
    await state.set_state(Dialogue_state.pay_for_subscription)

@router.callback_query(StateFilter(Dialogue_state.view_subscription), F.data=="subs_one_year")
async def one_year_subs(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text = (LEXICON_RU['one_year_sub']+LEXICON_RU['paying_for_subscription']), reply_markup=subscription_showing_markup())
    await state.set_state(Dialogue_state.pay_for_subscription)



@router.callback_query(F.data=="back")
async def one_year_subs(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text = LEXICON_RU['choose_subscription'], reply_markup=subscription_markup())
    await state.set_state(Dialogue_state.view_subscription)

@router.callback_query(F.data=="payed_for")
async def one_year_subs(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text = LEXICON_RU["payed_for_subscription"], reply_markup=payed_for_sub_markup())
    await state.set_state(Dialogue_state.view_subscription)


