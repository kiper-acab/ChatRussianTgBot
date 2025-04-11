__all__ = ()

import os

import dotenv
from sqlalchemy import BigInteger, Integer, String
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncAttrs,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


dotenv.load_dotenv()


PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
HOST_IP = os.getenv("IP")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")

engine = create_async_engine(
    f"postgresql+asyncpg://{PGUSER}:{PGPASSWORD}@{HOST_IP}/{DATABASE}",
)


# engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3")

async_session = async_sessionmaker(engine)


class Base(
    AsyncAttrs,
    DeclarativeBase,
):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id = mapped_column(BigInteger)
    first_name: Mapped[str] = mapped_column(String(500))
    points = mapped_column(BigInteger, default=0)
    count_comlited_tasks = mapped_column(Integer, default=0)


class Accents(Base):
    __tablename__ = "accents"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    normal_form: Mapped[str] = mapped_column(String(100))
    accented_form: Mapped[str] = mapped_column(String(100))


class VocabularyWords(Base):
    __tablename__ = "vocabulary_words"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    normal_form: Mapped[str] = mapped_column(String(100))
    missing_form: Mapped[str] = mapped_column(String(100))


class EgeAssignments(Base):
    __tablename__ = "ege_assignments"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number: Mapped[str] = mapped_column(String())
    task: Mapped[str] = mapped_column(String())
    asnwer: Mapped[str] = mapped_column(String())
    explanation: Mapped[str] = mapped_column(String())


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
