from .dispatcher_bot import dispatcher

from .callback_keyboard_bot import callback_keyboard
import aiogram

@dispatcher.message()
async def handler(message: aiogram.types.Message):
    if message.text == "START GAME":
        await message.answer(text = "Гру розпочато!", reply_markup= callback_keyboard)