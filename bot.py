import logging, open_xls
from aiogram import Bot, Dispatcher, executor, types
from access import bot_token


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['долг', 'долги'])
async def send_report(message: types.Message):
    await message.answer(open_xls.make_report_text())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
