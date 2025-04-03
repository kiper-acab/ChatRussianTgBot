__all__ = ()

from sqlalchemy import BigInteger, Integer, String
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncAttrs,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3")

async_session = async_sessionmaker(engine)


class Base(
    AsyncAttrs,
    DeclarativeBase,
):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    first_name: Mapped[str] = mapped_column(String(500))
    points = mapped_column(BigInteger, default=0)
    count_comlited_tasks = mapped_column(Integer, default=0)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
