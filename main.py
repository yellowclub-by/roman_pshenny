import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from pyexpat.errors import messages

TOKEN= "8042387585:AAHQN_VLraqQD1ZqeCBA82757Tw2COsK-WU"

bot = Bot(token = TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await (message.answer("привет тут есть скрипт и тут не надо подписыватся на каждый второй канал чтобы получить скрипт"))


@dp.message()
async def echo(message: types.Message):
    await(message.answer("бот в разроботке"))
    user_text=message.text
    await (message.answer(user_text))



async def main():
    print("бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())