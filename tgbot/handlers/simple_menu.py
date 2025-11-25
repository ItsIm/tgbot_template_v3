from aiogram import Router, types, Bot
from aiogram.filters import CommandStart

import logging

from tgbot.config import Config
from tgbot.keyboards.inline import webapp_kb_inline
from tgbot.keyboards.reply import reply_webapp_kb

main_router = Router()
logger = logging.getLogger(__name__)


text = """🛍 <b>Интернет-магазин в формате Telegram-бота и MiniApp для eCommerce</b>

Наше решение сочетает удобство классического интернет-магазина и мобильного приложения — всё внутри Telegram.
Бот приветствует пользователей, переводит в MiniApp, отправляет рассылки и уведомляет о статусах заказов.

✨ <b>Функционал</b>

👤 <b>Клиентская часть</b>  
🔎 Поиск по товарам  
📦 Варианты, фото, описания  
🛒 Корзина, оплата (наличные, карта, ЮMoney)  
🚚 Самовывоз и доставка через apiShip  
👛 Личный кабинет

🛠 <b>Админ-панель</b>  
🎨 Управление баннерами и товарами  
💳 Способы оплаты  
🔗 Интеграции (apiShip, МойСклад — в разработке)  
📢 Рассылки (в разработке)

🚀 Приложение постоянно развивается — появляются новые фичи, улучшения и интеграции.  
💡 Любые доработки и интеграции можно добавить по запросу.

📱 <b>Открывай MiniApp и начинай покупки!</b>

✏️ По всем вопросам, а так же для получения доступа к панели администратора пишите @y_thirteen_y
"""



@main_router.message(CommandStart())
async def cmd_start(message: types.Message, config: Config, bot: Bot):
    logger.info(f"Нажатие {message.from_user.id}")
    logger.info(f"{config.tg_bot.web_app_url}")
    await message.answer(
        text,
        reply_markup=webapp_kb_inline(url=config.tg_bot.web_app_url, admin_panel_url=config.tg_bot.admin_panel_url)
    )

    # await message.answer(
    #     "This is text button webapp!",
    #     reply_markup=reply_webapp_kb(url=config.tg_bot.web_app_url)
    # )

    await bot.set_chat_menu_button(
        chat_id=message.from_user.id,
        menu_button=types.MenuButtonWebApp(
            text="Открыть магазин", web_app=types.WebAppInfo(url=config.tg_bot.web_app_url)
        )
    )


