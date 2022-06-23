from time import strftime

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import datetime as dt
#import buttons
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
    await message.answer(f"{message.from_user.first_name} Приветствую я тестовый бот для ")
    await message.answer(f"Настоящие Время:{time}")


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)