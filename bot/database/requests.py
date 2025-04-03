__all__ = ()

import database.models
from sqlalchemy import select


async def set_user(tg_id, first_name):
    async with database.models.async_session() as session:
        user = await session.scalar(
            select(database.models.User).where(
                database.models.User.tg_id == tg_id,
            ),
        )

        if not user:
            session.add(
                database.models.User(tg_id=tg_id, first_name=first_name),
            )
            await session.commit()


async def update_user_points(tg_id, points):
    async with database.models.async_session() as session:
        user = await session.scalar(
            select(database.models.User).where(
                database.models.User.tg_id == tg_id,
            ),
        )
        if user:
            user.points += points
            user.count_comlited_tasks += 1
            await session.commit()


async def get_user(tg_id):
    async with database.models.async_session() as session:
        return await session.scalar(
            select(database.models.User).where(
                database.models.User.tg_id == tg_id,
            ),
        )


async def get_top_users():
    async with database.models.async_session() as session:
        people = await session.scalars(
            select(database.models.User)
            .order_by(database.models.User.points.desc())
            .limit(50),
        )

        return people.fetchall()
