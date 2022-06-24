from time import strftime
import goros as gr
import random as rd
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import datetime as dt
import button
#from func import *
from config import TOKEN


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)




time=strftime("%H:%M:%S")


@dp.message_handler(commands="start")
async def process_start_command(message: types.Message):
    await message.answer(f"{message.from_user.first_name} Приветствую я тестовый бот для  обучения ")
    await message.answer(f"Настоящие Время:{time}",reply_markup=button.replykb)

@dp.message_handler(text="Овен")
async def process_start_command(message: types.Message):
    ov = "".join(rd.choice(gr.oven))
    await message.answer(f'{ov}')

@dp.message_handler(text="Телец")
async def process_start_command(message: types.Message):
    ov = "".join(rd.choice(gr.telec))
    await message.answer(f'{ov}')


@dp.message_handler(content_types="text")
async def process_start_command(message: types.Message):
    ov = "".join(rd.choice(gr.kub))
    await message.answer(f'{message.from_user.first_name}-{ov}')


@dp.message_handler(text="Кубик")
async def process_start_command(message: types.Message):
    ov = "".join(rd.choice(gr.kub))
    await message.answer(f'{message.from_user.first_name}-{ov}')


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)