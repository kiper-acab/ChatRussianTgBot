__all__ = ()

import random

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


async def get_accent_word():
    async with database.models.async_session() as session:
        accents = await session.scalars(
            select(database.models.Accents),
        )
        accents_list = accents.all()
        return random.choice(accents_list)


async def get_vocabulary_word():
    async with database.models.async_session() as session:
        accents = await session.scalars(
            select(database.models.VocabularyWords),
        )
        accents_list = accents.all()
        return random.choice(accents_list)


async def get_ege_task(number):
    async with database.models.async_session() as session:
        tasks = await session.scalars(
            select(database.models.EgeAssignments).where(
                database.models.EgeAssignments.number == number,
            ),
        )
        task = tasks.all()
        return random.choice(task)