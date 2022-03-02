import aiogram
import logging

import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from puk import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
intro = 'Здарова, Че хотел?'

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(intro, reply_markup=mainmenu)

@dp.message_handler(text = 'Начать историю')
async def menuCategories(message: types.Message):
    await message.answer('ПОМОГИТЕ МНЕ', reply_markup=anw11)

@dp.message_handler(text = 'Привет, ты кто?')
async def cat1Menu(message: types.Message):
    await message.answer("Я Пип, и я не знаю где я", reply_markup=anwlist)
@dp.message_handler(text = 'Привет')
async def cat1Menu(message: types.Message):
    await message.answer("Я Пип, и я не знаю где я", reply_markup=anwlist)


@dp.message_handler(text = 'Где ты?')
async def cat1Menu(message: types.Message):
    await message.answer("Я не знаю где я, я потерялся", reply_markup = anwlist1)
@dp.message_handler(text = 'Ты видешь что нибудь?')
async def cat1Menu(message: types.Message):
    await message.answer("Я не знаю где я, я потерялся", reply_markup = anwlist1)



# @dp.message_handler(text= '')
# async def order




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)