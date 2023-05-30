import logging
from config import bot_token
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token=bot_token)
# Диспетчер для бота
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Готов тебя дразнить! Напиши, что-нибудь.")


@dp.message_handler(content_types=["text"])
async def send_answer(message: types.Message):
    await message.answer(message.text + "🤡")

executor.start_polling(dp, skip_updates=True)
