__all__ = ()

import asyncio
import logging
import os

import aiogram
import aiogram.filters
import aiogram.fsm.storage.memory
import aiogram.types
import dotenv


dotenv.load_dotenv()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

admins = [int(admin_id) for admin_id in os.getenv("ADMINS").split(",")]

bot = aiogram.Bot(token=os.getenv("BOT_TOKEN"))
dp = aiogram.Dispatcher(storage=aiogram.fsm.storage.memory.MemoryStorage())


@dp.message(aiogram.filters.CommandStart())
async def command_start(message: aiogram.types.Message):
    await message.answer(
        "Привет! Я Руся — твой помощник в подготовке к русскому языку! 📚✍️ \n"
        "Я помогу тебе улучшить орфографию, пунктуацию, разберу \n"
        "сложные правила и даже устрою небольшие тесты. Вот что я умею: \n"
        "  ✅ Проверять знания орфографии\n"
        "  ✅ Проверять правильность написания словарных слов\n"
        "  ✅ Давать полезные упражнения\n",
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        logger.info("Exit")
