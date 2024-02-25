import asyncio
import os
import handlers
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, bot
import filters
import logging
from loader import dp
import sys



'''WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.environ.get("PORT", 5000))
user_message = 'Пользователь'
admin_message = 'Админ'''




'''async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()

    await bot.delete_webhook()
    await bot.set_webhook(config.WEBHOOK_URL)'''


'''async def on_shutdown():
    logging.warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")'''


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls

    # And the run events dispatching
    await dp.start_polling(bot, skip_updates=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())