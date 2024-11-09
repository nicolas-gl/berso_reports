import logging
from random import randint
import open_xls
from aiogram import Bot, Dispatcher, executor, types
from access import bot_token, bot_admin_id


logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

keyboard = types.InlineKeyboardMarkup()
keyboard.add(types.InlineKeyboardButton(text="Уточнить долги", callback_data="get_debts_value"))


@dp.message_handler(commands=['долг', 'долги'])
async def send_report(message: types.Message):
    if str(message.from_user.id) in bot_admin_id.split(' '):
        await message.answer("загрузка...")
        await message.answer(open_xls.make_report_text()) 
        await message.answer('Введите "/долги" или нажмите на кнопку, чтобы получить список новых долгов', reply_markup=keyboard)
    else: 
        await bot.send_message(bot_admin_id.split(' ')[0],
                            "‼ {} (@{}, id:{}) писал боту".format(
                                message.from_user.full_name,
                                message.from_user.username,
                                message.from_user.id))


@dp.callback_query_handler(text="get_debts_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer("загрузка...")
    await call.message.answer(open_xls.make_report_text())
    await call.message.answer('Введите "/долги" или нажмите на кнопку, чтобы получить список новых долгов', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
