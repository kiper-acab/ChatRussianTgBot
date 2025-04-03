__all__ = ()

import aiogram.types


main = aiogram.types.ReplyKeyboardMarkup(
    keyboard=[
        [
            aiogram.types.KeyboardButton(text="🙂Словарные слова"),
            aiogram.types.KeyboardButton(text="УдарЕ́ния"),
        ],
        [
            aiogram.types.KeyboardButton(text="👤Профиль"),
            aiogram.types.KeyboardButton(text="📚Задания ЕГЭ"),
            aiogram.types.KeyboardButton(text="💪Лидеры"),
        ],
        [
            aiogram.types.KeyboardButton(text="📋Теория к заданиям"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)

keyboard_after_dictionary_answer = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            aiogram.types.InlineKeyboardButton(
                text="Далее",
                callback_data="more_dictionary_word",
            ),
        ],
        [
            aiogram.types.InlineKeyboardButton(
                text="Выйти",
                callback_data="keyboard_to_main",
            ),
        ],
    ],
    resize_keyboard=True,
)

keyboard_after_accent_answer = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            aiogram.types.InlineKeyboardButton(
                text="Далее",
                callback_data="more_accent_word",
            ),
        ],
        [
            aiogram.types.InlineKeyboardButton(
                text="Выйти",
                callback_data="keyboard_to_main",
            ),
        ],
    ],
    resize_keyboard=True,
)

ege_tasks_keyboard = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            aiogram.types.InlineKeyboardButton(
                text="1",
                callback_data="ege_task_1",
            ),
            aiogram.types.InlineKeyboardButton(
                text="2",
                callback_data="ege_task_2",
            ),
            aiogram.types.InlineKeyboardButton(
                text="3",
                callback_data="ege_task_3",
            ),
            aiogram.types.InlineKeyboardButton(
                text="4",
                callback_data="ege_task_4",
            ),
        ],
        [
            aiogram.types.InlineKeyboardButton(
                text="5",
                callback_data="ege_task_5",
            ),
            aiogram.types.InlineKeyboardButton(
                text="6",
                callback_data="ege_task_6",
            ),
            aiogram.types.InlineKeyboardButton(
                text="7",
                callback_data="ege_task_7",
            ),
            aiogram.types.InlineKeyboardButton(
                text="8",
                callback_data="ege_task_8",
            ),
        ],
        [
            aiogram.types.InlineKeyboardButton(
                text="9",
                callback_data="ege_task_9",
            ),
            aiogram.types.InlineKeyboardButton(
                text="10",
                callback_data="ege_task_10",
            ),
            aiogram.types.InlineKeyboardButton(
                text="11",
                callback_data="ege_task_11",
            ),
            aiogram.types.InlineKeyboardButton(
                text="12",
                callback_data="ege_task_12",
            ),
        ],
        [
            aiogram.types.InlineKeyboardButton(
                text="13",
                callback_data="ege_task_13",
            ),
            aiogram.types.InlineKeyboardButton(
                text="14",
                callback_data="ege_task_14",
            ),
            aiogram.types.InlineKeyboardButton(
                text="15",
                callback_data="ege_task_15",
            ),
            aiogram.types.InlineKeyboardButton(
                text="16",
                callback_data="ege_task_16",
            ),
        ],
        [
            aiogram.types.InlineKeyboardButton(
                text="17",
                callback_data="ege_task_17",
            ),
            aiogram.types.InlineKeyboardButton(
                text="18",
                callback_data="ege_task_18",
            ),
            aiogram.types.InlineKeyboardButton(
                text="19",
                callback_data="ege_task_19",
            ),
            aiogram.types.InlineKeyboardButton(
                text="20",
                callback_data="ege_task_20",
            ),
        ],
        [
            aiogram.types.InlineKeyboardButton(
                text="21",
                callback_data="ege_task_21",
            ),
            aiogram.types.InlineKeyboardButton(
                text="22",
                callback_data="ege_task_22",
            ),
            aiogram.types.InlineKeyboardButton(
                text="23",
                callback_data="ege_task_23",
            ),
            aiogram.types.InlineKeyboardButton(
                text="24",
                callback_data="ege_task_24",
            ),
        ],
        [
            aiogram.types.InlineKeyboardButton(
                text="25",
                callback_data="ege_task_25",
            ),
            aiogram.types.InlineKeyboardButton(
                text="26",
                callback_data="ege_task_26",
            ),
        ],
    ],
)


keyboard_teory_to_task = aiogram.types.ReplyKeyboardMarkup(
    keyboard=[
        [
            aiogram.types.KeyboardButton(
                text="Отменить",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Правописание суффиксов",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text=(
                    "Правописание личных окончаний "
                    "глаголов и суффиксов причастий"
                ),
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text=(
                    "Различные виды написания слов "
                    "(слитные, дефисные, раздельные)"
                ),
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Правописание н и нн",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Пунктуация в СПП и ССП",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Знаки препинания в предложениях с обособленными членами",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Средства связей предложений",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Выразительные средства",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Типы речи",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Ударения",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Паронимы",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Лексические нормы",
            ),
        ],
        [
            aiogram.types.KeyboardButton(
                text="Образовние грамматических форм",
            ),
        ],
    ],
)
