from aiogram import Bot,types
from aiogram import Dispatcher
from aiogram import executor
from aiogram.dispatcher.filters import Text
import botconf
import mparse
import logging
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import wikiparse
import os


class DataInput(StatesGroup):
    r = State()



bot = Bot(token=botconf.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="NS Clipper")
    keyboard.add(button_1)
    button_2 = "NS Captain"
    keyboard.add(button_2)
    button_3 = "/wiki"
    keyboard.add(button_3)
    await message.answer("Какое твое судно?", reply_markup=keyboard)


@dp.message_handler(Text(equals='/wiki'))
async def askme(message : types.Message):
    await bot.send_message(message.from_user.id,"Спроси у меня что то")
    await DataInput.r.set()

@dp.message_handler(state=DataInput.r)
async def answeryou(message : types.Message, state: FSMContext):
    r = message.text
    await message.answer(wikiparse.wikiparse(r))
    await state.finish()



@dp.message_handler(Text(equals='NS Clipper'))#обозначает событие, когда в наш чат кто-то что то пишет
async def echo_send(message : types.Message):
    await message.answer(mparse.parse('https://www.vesselfinder.com/ru/vessels/NS-CLIPPER-IMO-9341081-MMSI-636012661'))

@dp.message_handler(Text(equals='NS Captain'))#обозначает событие, когда в наш чат кто-то что то пишет
async def echo_send(message : types.Message):
    await message.answer(mparse.parse('https://www.vesselfinder.com/ru/vessels/NS-CAPTAIN-IMO-9341067-MMSI-636012659'))







executor.start_polling(dp, skip_updates=True) #Наш бот не будет реагировать на те сообщения, которые ему пришли, когда он был не онлайн
