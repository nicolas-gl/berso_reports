import logging, open_xls
from aiogram import Bot, Dispatcher, executor, types
from access import bot_token
 

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """    This handler will be called when user sends `/start` or `/help` command    """
#     await message.reply("Hi!\nI'm BersoTechBot!\nPowered by Nicolas.")


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)



@dp.message_handler(commands=['go'])
async def echo(message: types.Message):
    # await message.answer(message.text)
    await message.answer(open_xls.make_report_text())
    # open_xls.make_report_text()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

