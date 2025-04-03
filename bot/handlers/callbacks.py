__all__ = ()

import aiogram
import aiogram.types
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
