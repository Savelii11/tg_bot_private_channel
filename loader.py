import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.fsm.storage.memory import MemoryStorage
from utils.db.storage import DatabaseManager
from aiogram.enums.parse_mode import ParseMode
from data import config

load_dotenv()

bot_token = str(os.getenv('BOT_TOKEN'))
print(bot_token)
bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode=ParseMode.HTML)
storage = MemoryStorage()
router = Router()
# Dispatcher is a root router
# ... and all other routers should be attached to Dispatcher
dp = Dispatcher(bot = bot,storage=storage)
dp.include_router(router)



#db = DatabaseManager('data/database.db')