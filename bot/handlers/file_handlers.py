__all__ = ()

import os

import aiogram
import aiogram.types
import keyboards


router = aiogram.Router()


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[1][0].text,
)
async def suffics(message: aiogram.types.Message):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "sufficses.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[2][0].text,
)
async def write_personal_end_words_and_suffices_participles(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "glaogli_i_suffecsi_prechastiy.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[3][0].text,
)
async def type_writing_words(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "vidi_napisanya_slov.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[4][0].text,
)
async def write_n_and_nn(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "pravopisanie_n_i_nn.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[5][0].text,
)
async def punctuation_spp_ssp(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "punktuacia_v_ssp_spp.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[6][0].text,
)
async def punctuation_marks(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "znaki_prepinania.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[7][0].text,
)
async def offer_links(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "sredstvo_svyazen_v_predlozenii.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[8][0].text,
)
async def expressive_means(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "virazitelnie_sredstva.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[9][0].text,
)
async def types_of_speech(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "tipi_rechi.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[10][0].text,
)
async def accents(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "udarenya.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[11][0].text,
)
async def paronyms(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "paronimi.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[12][0].text,
)
async def lexical_norms(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "leksicheskie_normi.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )


@router.message(
    aiogram.F.text == keyboards.keyboard_teory_to_task.keyboard[13][0].text,
)
async def formation_of_grammatical_forms(
    message: aiogram.types.Message,
):
    document = aiogram.types.FSInputFile(
        path=os.path.join(
            "other_files",
            "theory_for_assignments",
            "grammaticheskie_formi.docx",
        ),
    )
    await message.answer_document(
        document=document,
        reply_markup=keyboards.keyboard_teory_to_task,
    )
