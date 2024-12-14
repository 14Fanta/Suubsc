from aiogram.types import (KeyboardButton,ReplyKeyboardMarkup,
                            InlineKeyboardButton, InlineKeyboardMarkup)

inline_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Присоединиться', callback_data="join",)]])