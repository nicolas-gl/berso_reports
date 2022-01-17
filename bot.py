import logging
from aiogram import Bot, Dispatcher, executor, types
from access import bot_token
 
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """    This handler will be called when user sends `/start` or `/help` command    """
    await message.reply("Hi!\nI'm BersoTechBot!\nPowered by Nicolas.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer(message.text)


@dp.message_handler(commands=['go'])
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
