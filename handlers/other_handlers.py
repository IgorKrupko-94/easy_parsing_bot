from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()


@router.message(StateFilter(default_state))
async def send_other_answer(message: Message):
    """Хэндлер, срабатывающий на любое другое сообщение от пользователя,
    которое не было перехвачено другими хэндлерами."""
    await message.answer(text=LEXICON_RU['other_answer'])
