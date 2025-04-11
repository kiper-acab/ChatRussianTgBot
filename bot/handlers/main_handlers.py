__all__ = ()

import aiogram
import aiogram.filters
import aiogram.fsm.context
import aiogram.fsm.state
import database.requests
import keyboards


router = aiogram.Router()


class AnswerDictionaryWords(aiogram.fsm.state.StatesGroup):
    user_answer = aiogram.fsm.state.State()
    correct_answer = aiogram.fsm.state.State()


class AnswerAccentWord(aiogram.fsm.state.StatesGroup):
    user_answer = aiogram.fsm.state.State()
    correct_answer = aiogram.fsm.state.State()


class EgeTask(aiogram.fsm.state.StatesGroup):
    user_answer = aiogram.fsm.state.State()
    correct_answer = aiogram.fsm.state.State()


@router.message(aiogram.filters.CommandStart())
async def command_start(message: aiogram.types.Message):
    await database.requests.set_user(
        message.from_user.id,
        message.from_user.first_name,
    )
    await message.answer(
        (
            f"👋 Привет, {message.from_user.first_name}! "
            "Я <b>Руся</b> — твой персональный "
            "помощник по русскому языку! 📚✨\n\n"
            "Я помогу тебе улучшить орфографию, разобраться "
            "с пунктуацией и понять сложные правила. "
            "А ещё — устрою небольшие тесты, "
            "чтобы ты мог проверить свои знания! 🔥\n\n"
            "Вот что я умею:\n"
            "  ✅ <b>Проверять знания орфографии</b>\n"
            "  ✅ <b>Проверять правильность написания словарных слов</b>\n"
            "  ✅ <b>Давать задания ЕГЭ</b>\n\n"
            "Готов начать? Жми на кнопки ниже! 👇"
        ),
        reply_markup=keyboards.main,
        parse_mode="HTML",
    )


@router.message(aiogram.F.text == keyboards.main.keyboard[0][0].text)
async def dictionary_word(
    message: aiogram.types.Message,
    state: aiogram.fsm.context.FSMContext,
):
    random_word = await database.requests.get_vocabulary_word()
    await state.update_data(correct_answer=random_word.normal_form)
    await state.set_state(AnswerDictionaryWords.user_answer)
    await message.answer(
        f"Как правильно пишется слово: <b>{random_word.missing_form}</b>?",
        parse_mode="HTML",
    )


@router.message(aiogram.F.text == keyboards.main.keyboard[0][1].text)
async def accent_words(
    message: aiogram.types.Message,
    state: aiogram.fsm.context.FSMContext,
):
    random_word = await database.requests.get_accent_word()
    await state.update_data(correct_answer=random_word.accented_form)
    await state.set_state(AnswerAccentWord.user_answer)
    await message.answer(
        (
            "\n<pre>Напишите слово с маленькой буквы, "
            "где заглавной будет только та, на которую "
            "ставить ударение</pre>"
            "Куда падает ударение в слове: "
            f"<b>{random_word.normal_form}</b>?"
        ),
        parse_mode="HTML",
    )


@router.message(aiogram.F.text == keyboards.main.keyboard[1][0].text)
async def command_profile(message: aiogram.types.Message):
    user = await database.requests.get_user(message.from_user.id)
    await message.answer(
        f"👤Имя пользователя: {message.from_user.first_name}\n"
        "\n"
        f"⭐️ Количество баллов: {user.points}\n"
        "\n"
        f"✅ Решено заданий: {user.count_comlited_tasks}",
    )


@router.message(AnswerDictionaryWords.user_answer)
async def get_answer(
    message: aiogram.types.Message,
    state: aiogram.fsm.context.FSMContext,
):
    await state.update_data(user_answer=message.text)
    data = await state.get_data()
    if data["user_answer"].lower().strip() == data["correct_answer"]:
        await database.requests.update_user_points(message.from_user.id, 100)
        user = await database.requests.get_user(message.from_user.id)

        await message.answer(
            "Это правильный ответ!\n\n"
            "🏆 Награда: 100 баллов\n\n"
            f"⭐️ Баллы: {user.points}",
            reply_markup=keyboards.keyboard_after_dictionary_answer,
        )

    else:
        await message.answer(
            "Это неверно😴\n\n"
            f"👉 Правильный ответ: {data['correct_answer']}",
            reply_markup=keyboards.keyboard_after_dictionary_answer,
        )

    await state.clear()


@router.message(AnswerAccentWord.user_answer)
async def get_answer_accent_words(
    message: aiogram.types.Message,
    state: aiogram.fsm.context.FSMContext,
):
    await state.update_data(user_answer=message.text)
    data = await state.get_data()
    if data["user_answer"].strip() == data["correct_answer"]:
        await database.requests.update_user_points(message.from_user.id, 100)
        user = await database.requests.get_user(message.from_user.id)

        await message.answer(
            "Это правильный ответ!\n\n"
            "🏆 Награда: 100 баллов\n\n"
            f"⭐️ Баллы: {user.points}",
            reply_markup=keyboards.keyboard_after_accent_answer,
        )

    else:
        await message.answer(
            "Это неверно😴\n\n"
            f"👉 Правильный ответ: {data['correct_answer']}",
            reply_markup=keyboards.keyboard_after_accent_answer,
        )

    await state.clear()


@router.message(aiogram.F.text == keyboards.main.keyboard[1][2].text)
async def get_leaders(message: aiogram.types.Message):
    leaders = await database.requests.get_top_users()
    message_for_user = "Таблица лидеров: \n"
    for leader in range(1, len(leaders) + 1):
        message_for_user += (
            f"{leader}. {leaders[leader - 1].points} - "
            f"{leaders[leader - 1].first_name}\n"
        )

    await message.answer(f"`{message_for_user}`", parse_mode="MarkdownV2")


@router.message(aiogram.F.text == keyboards.main.keyboard[1][1].text)
async def ege_tasks(message: aiogram.types.Message):
    await message.answer(
        "Выберите задание для нарешивания✍️",
        reply_markup=keyboards.ege_tasks_keyboard,
    )


@router.message(aiogram.F.text == keyboards.main.keyboard[2][0].text)
async def theory_for_assignments(message: aiogram.types.Message):
    await message.answer(
        "Выберите то, чтобы хотели узнать:",
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[0][0].text,
)
async def return_to_main(message: aiogram.types.Message):
    await message.answer(
        "Вы вернулись в главное меню!",
        reply_markup=keyboards.main,
    )
