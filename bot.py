import logging, open_xls
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
    if str(message.from_user.id) != bot_admin_id:
        try:
            await bot.send_message(bot_admin_id, 'пользователь @{} (id:{}) писал боту'.format(message.from_user.username, message.from_user.id))
        except:
            await bot.send_message(bot_admin_id, message.from_user.full_name)
            await bot.send_message(bot_admin_id, 'пользователь {} (id:{}) писал боту'.format(message.from_user.full_name, message.from_user.id))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
