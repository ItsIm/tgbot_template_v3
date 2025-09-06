Этот шаблон используется для разработки Telegram ботов с использованием библиотеки [`aiogram v3.0+`](https://github.com/aiogram/aiogram/tree/dev-3.x).

## SQLAlchemy + Alembic
В коде есть примеры таблички User с использованием SQLAlchemy 2.0, и скрипты для алембика (инициализация алембик, создание и применение миграций).

Но, если вы с этими инструментами никогда не работали, то обратитесь к документации и узнайте об этих инструментах.

### Для того, чтобы начать использовать:
1. Скопируйте `.env.dist` в `.env` и заполните необходимые данные.
2. Создайте новые хендлеры.
3. **Docker:**
   1. Можете сразу запускать проект с Docker, а если у вас его нет, то [загрузите, и установите](https://docs.docker.com/get-docker/).
   2. Запустите проект командой `docker-compose up`
4. **Без Docker:**
   1. Создайте [venv](https://docs.python.org/3/library/venv.html)
   2. Установите зависимости из requirements.txt: `pip install -r requirements.txt --pre`
   3. Запустите проект командой `python3 bot.py`


### Как делать и регистрировать хендлеры:
Создайте модуль `you_name.py` в папке `handlers`.

Создайте роутер в `you_name.py`.
```python
from aiogram import Router
user_router = Router()
```
Можно делать несколько роутеров в одном модуле, и на каждый из них навешивать хендлеры.
Можно регистрировать хендлеры декораторами:
```python
@user_router.message(commands=["start"])
async def user_start(message):
    await message.reply("Привет, обычный пользователь!")
```

Заходим в файл `handlers/__init__.py` и добавляем все роутеры в него:
```python
from .admin import admin_router
from .echo import echo_router
from .user import user_router

...


routers_list = [
    admin_router,
    user_router,
    echo_router,  # echo_router must be last
]

```
### Как добавить хендлеры к нашему боту:
Переходим к файлу `bot.py` и распаковываем наши хендлеры:
```python
from tgbot.handlers import routers_list

...

async def main():
   
    ...

   dp.include_routers(*routers_list)

    ...


```

### Как запустить Базу Данных и провести свою первую миграцию:
1. Перейдите к файлу `.env` и заполните данные для базы данных, если вы не сделали этого ранее.

2. Перейдите к файлу `docker-compose.yml` и раскомментируйте секции: `api`, `pg_database` і `volumes`, чтобы начать работу.

3. Перейдите к `config.py` и выполните `TODO` в функции `construct_sqlalchemy_url`. Также найдите раздел функции `load_config` и раскомментируйте строку, отвечающую за инициализацию конфигурации базы данных `db=DbConfig.from_env(env)`, чтобы активировать подключение к базе данных.

4. Теперь можем перезапустить Docker с новыми контейнерами, используя команду:

    `docker-compose up --build.`

5. Все готово! Теперь можем провести миграцию!
Откройте терминал и введите следующую команду:

    `docker-compose exec api alembic upgrade head`

### Туториалы по aiogram v3
Видео пока что нет, но @Groosha уже начал делать [свое руководство](https://mastergroosha.github.io/aiogram-3-guide).
