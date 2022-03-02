import logging

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types

#Telegram bot token
API_TOKEN = '5169760657:AAEC2yGT1JHV8ZqWIg3eBrSMAE0gWhHIVdk'


#Main menu buttons
menu = KeyboardButton('Начать историю')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(menu)

#Questions or phrases
hi = KeyboardButton('Привет')
name = KeyboardButton('Привет, ты кто?')
anw11 = ReplyKeyboardMarkup(resize_keyboard=True).add(hi).add(name)

anw1 = KeyboardButton('Где ты?')
anw2 = KeyboardButton('Ты видешь что нибудь?')
anwlist = ReplyKeyboardMarkup(resize_keyboard=True).add(anw2).add(anw1)

anw12 = KeyboardButton('ЧТО то ')
anw22 = KeyboardButton('ЧТО то')
anwlist1 = ReplyKeyboardMarkup(resize_keyboard=True).add(anw12).add(anw12)