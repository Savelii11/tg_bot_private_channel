from aiogram.fsm.state import State, StatesGroup

class Dialogue_state(StatesGroup):
    start = State()
    view_subscription = State()
    pay_for_subscription = State()
