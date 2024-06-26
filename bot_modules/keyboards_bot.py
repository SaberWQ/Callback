import aiogram
from .buttons_bot import button_game_start

keboards_start = aiogram.types.ReplyKeyboardMarkup(
    keyboard = [
        [button_game_start]
    ]
)