import os
import sys
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import logging

from app.handlers import user_router , bot
from app.handlers import dp
from app.database.models import async_main

async def main():
    load_dotenv()

    await async_main()

    dp.include_router(user_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        print("Bot turned on...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot turned off...")