import botconf
import logging

from aiogram import Bot, Dispatcher, executor, types

#log level

logging.basicConfig(level=logging.INFO)

#bot init
bot = Bot(token=botconf.TOKEN)
dp = Dispatcher(bot)


#echo
@dp.message_handler()
async def echo(message: types.message):
    await message.answer(message.text)


