from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def webapp_kb_inline(url: str, admin_panel_url: str):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Открыть магазин",
        web_app=WebAppInfo(
            url=url,
        ),
    )

    keyboard.button(
        text="Открыть панель администратора",
        web_app=WebAppInfo(
            url=admin_panel_url,
        ),
    )

    keyboard.adjust(1, 1)
    return keyboard.as_markup()
