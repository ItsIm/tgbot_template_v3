from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def webapp_kb_inline(url: str):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Открыть магазин",
        web_app=WebAppInfo(
            url=url,
        ),
    )
    return keyboard.as_markup()
