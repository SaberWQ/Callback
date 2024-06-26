import aiogram
import aiogram.dispatcher
import aiogram.filters
from .dispatcher_bot import dispatcher
from .keyboards_bot import keboards_start

@dispatcher.message(aiogram.filters.CommandStart())
async def bot_start(message: aiogram.types.Message):
    await message.answer(text= "Hello", reply_markup = keboards_start)
