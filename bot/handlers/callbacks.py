__all__ = ()

import aiogram
import aiogram.fsm.context
import aiogram.types
import database.requests
import handlers.main_handlers
import keyboards


router = aiogram.Router()


@router.callback_query(
    aiogram.F.data
    == (
        keyboards.keyboard_after_dictionary_answer.inline_keyboard[1][
            0
        ].callback_data
    ),
)
async def exit_to_main(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "Вы вернулись в главное меню!",
        reply_markup=keyboards.main,
    )


@router.callback_query(
    aiogram.F.data
    == (
        keyboards.keyboard_after_dictionary_answer.inline_keyboard[0][
            0
        ].callback_data
    ),
)
async def more_dictionary_word(
    callback: aiogram.types.CallbackQuery,
    state: aiogram.fsm.context.FSMContext,
):
    await callback.answer()
    await handlers.main_handlers.dictionary_word(callback.message, state)


@router.callback_query(
    aiogram.F.data
    == keyboards.keyboard_after_accent_answer.inline_keyboard[0][
        0
    ].callback_data,
)
async def more_accent_word(
    callback: aiogram.types.CallbackQuery,
    state: aiogram.fsm.context.FSMContext,
):
    await callback.answer()
    await handlers.main_handlers.accent_words(callback.message, state)


@router.callback_query(lambda c: c.data.startswith("ege_task_"))
async def handle_ege_task(
    callback_query: aiogram.types.CallbackQuery,
    state: aiogram.fsm.context.FSMContext,
):
    task_number = callback_query.data.split('_')[-1]
    task = await database.requests.get_ege_task(task_number)
    task_text = task.task

    await state.update_data(correct_answer=task.asnwer)
    await state.set_state(handlers.main_handlers.EgeTask.user_answer)

    await callback_query.message.answer(task_text, parse_mode="HTML")

