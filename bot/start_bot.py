__all__ = ()

import asyncio
import logging
import os

import aiogram
import aiogram.fsm.storage.memory
import database.models
import dotenv
import handlers.callbacks
import handlers.file_handlers
import handlers.main_handlers


dotenv.load_dotenv()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

admins = [int(admin_id) for admin_id in os.getenv("ADMINS").split(",")]


async def main():
    await database.models.async_main()
    bot = aiogram.Bot(token=os.getenv("BOT_TOKEN"))
    dp = aiogram.Dispatcher(storage=aiogram.fsm.storage.memory.MemoryStorage())
    dp.include_routers(
        handlers.main_handlers.router,
        handlers.file_handlers.router,
        handlers.callbacks.router,
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        logger.info("Exit")
