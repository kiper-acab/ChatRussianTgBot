import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from database.models import Base, Accents, VocabularyWords, EgeAssignments
import json


import os

import dotenv

dotenv.load_dotenv()


PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
HOST_IP = os.getenv("IP")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")

# DATABASE_URL = "sqlite+aiosqlite:///sqlite.db"  # можно заменить на путь к своей БД
# engine = create_async_engine(DATABASE_URL, echo=True)
engine = create_async_engine(
    f"postgresql+asyncpg://{PGUSER}:{PGPASSWORD}@{HOST_IP}/{DATABASE}",
)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)





with open('other_files/accents.json', 'r', encoding='utf-8') as f:
    accents_data = json.load(f)

with open('other_files/sl_words.json', 'r', encoding='utf-8') as f:
    sl_words_data = json.load(f)

with open('other_files/tasks.json', 'r', encoding='utf-8') as f:
    ege = json.load(f)



async def insert_data():
    # Создаём таблицы, если их ещё нет
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Добавляем данные в сессию
    async with AsyncSessionLocal() as session:
        session.add_all([Accents(**item) for item in accents_data])
        session.add_all([VocabularyWords(**item) for item in sl_words_data])
        session.add_all([EgeAssignments(**item) for item in ege])
        await session.commit()
        print("✅ Данные успешно добавлены!")

# ✅ Запуск
if __name__ == "__main__":
    asyncio.run(insert_data())