import logging
import open_xls
from aiogram import Bot, Dispatcher, executor, types
from access import bot_token, bot_admin_id


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['долг', 'долги'])
async def send_report(message: types.Message):
    await message.answer(open_xls.make_report_text())
    if str(message.from_user.id) not in bot_admin_id.split(' '):
        await bot.send_message(bot_admin_id.split(' ')[0],
                               "‼ {} (@{}, id:{}) писал боту".format(
                                   message.from_user.full_name,
                                   message.from_user.username,
                                   message.from_user.id))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
