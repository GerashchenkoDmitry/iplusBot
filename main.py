import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6067846317:AAHxfPCNawHxS8vbInaXI8ijcYyXUsTERi0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    sdfgdsafdasF
    SADSADASD
    """
    await message.reply("First string!\nSecond String!\nAll right its ok! I'm understood it!")

if __name__ == '__main__':  
    executor.start_polling(dp, skip_updates=True)


