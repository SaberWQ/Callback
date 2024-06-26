import aiogram
from .callback_buttons_bot import button_left, button_right

callback_keyboard = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard = [
        [button_left, button_right]
    ]
)