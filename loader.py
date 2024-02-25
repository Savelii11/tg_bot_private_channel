from aiogram import Bot, Dispatcher, Router, types
from aiogram.fsm.storage.memory import MemoryStorage
from utils.db.storage import DatabaseManager
from aiogram.enums.parse_mode import ParseMode
from data import config


bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
router = Router()
# Dispatcher is a root router
# ... and all other routers should be attached to Dispatcher
dp = Dispatcher(bot = bot,storage=storage)
dp.include_router(router)



db = DatabaseManager('data/database.db')