from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_webapp_kb(url: str):
    kb = ReplyKeyboardBuilder()
    kb.button(
        text="Открыть магазин",
        web_app=WebAppInfo(url=url)
    )
    return kb.as_markup(resize_keyboard=True)
