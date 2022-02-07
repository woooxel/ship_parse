from aiogram import Bot,types
from aiogram import Dispatcher
from aiogram import executor
from aiogram.dispatcher.filters import Text
import botconf
import mparse
import os



bot = Bot(token=botconf.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="NS Clipper")
    keyboard.add(button_1)
    button_2 = "NS Captain"
    keyboard.add(button_2)
    await message.answer("Какое твое судно?", reply_markup=keyboard)

@dp.message_handler(Text(equals='NS Clipper'))#обозначает событие, когда в наш чат кто-то что то пишет
async def echo_send(message : types.Message):
    await message.answer(mparse.parse('https://www.vesselfinder.com/ru/vessels/NS-CLIPPER-IMO-9341081-MMSI-636012661'))

@dp.message_handler(Text(equals='NS Captain'))#обозначает событие, когда в наш чат кто-то что то пишет
async def echo_send(message : types.Message):
    await message.answer(mparse.parse('https://www.vesselfinder.com/ru/vessels/NS-CAPTAIN-IMO-9341067-MMSI-636012659'))


async def echo_send(message : types.Message): #отправляем сюда
    await message.answer(mparse.parse('https://www.vesselfinder.com/ru/vessels/NS-CAPTAIN-IMO-9341067-MMSI-636012659'))#подождать пока в потоке не появится свободное место для выполнения этой команды
   # await message.reply(message.text) #Такой же метод, позволяет ответить неважно куда написал бот
   # await bot.send_message(message.from_user.id, message.text) #сработает, если пользователь уже писал боту



executor.start_polling(dp, skip_updates=True) #Наш бот не будет реагировать на те сообщения, которые ему пришли, когда он был не онлайн
