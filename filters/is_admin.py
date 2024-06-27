from aiogram.filters import BaseFilter
from aiogram.types import Message

from config_data.config import config


class IsAdmin(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == config.tg_bot.admin_ids[0]
