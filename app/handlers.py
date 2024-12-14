import os
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv
import asyncio

from app.util import load_message
import app.database.requests  as rq
import app.keyboard as kb
# from main import Bot


load_dotenv()
bot = Bot(os.getenv("TOKEN_TG"))
dp = Dispatcher()

user_router = Router()

group ="https://t.me/+YHO-Nb3YntdkODgy"
ID_GROUP = -1002424887608

class Wait_Subs(StatesGroup):
    waiting_Subscribe = State()

@user_router.message(CommandStart())
async def cmd_start(message:Message,state:FSMContext):
    text = load_message("text1.txt")
    await message.answer(f"Мы рады тебя видеть, {message.from_user.full_name}!")
    await rq.set_id(message.from_user.id)
    await message.answer(text,reply_markup=kb.inline_buttons)

@user_router.callback_query(F.data == "join")
async def cmd_join(callbackQuery: CallbackQuery, state:FSMContext, bot: Bot):
    await state.set_state(Wait_Subs.waiting_Subscribe)
    await callbackQuery.answer('Вы нажали кнопку "присоединиться" ')
    invite_link = await bot.export_chat_invite_link(ID_GROUP)
    await bot.send_message(callbackQuery.from_user.id,f"Вот твоя ссылка для вступления в группу на 3 дня:{invite_link}")
    await callbackQuery.message.answer("Отлично! Ты получишь доступ на три дня. Теперь ты можешь вступить в нашу группу.")
    print("До паузы")
    await asyncio.sleep(259200)
    print("После паузы")
    await bot.ban_chat_member(ID_GROUP, callbackQuery.from_user.id)
    await bot.unban_chat_member(ID_GROUP, callbackQuery.from_user.id)
    await callbackQuery.message.answer("Твой период подписки закончился! Хочешь продлить?")
    await state.clear()
    await send_subscription_offers(callbackQuery.from_user.id)

async def send_subscription_offers(user_id, count=3):
    for i in range(count):
        await bot.send_message(user_id, f"Твое предложение продлить подписку еще на 3 дня. Осталось {count-i} попыток.")
        print("До повтора сообщения")
        await asyncio.sleep(43200)  # Ждем полдня между письмами
        print("После повтора сообщения")
        

# @user_router.message(Command("ID"))
# async def id(message:Message):
#     await message.answer(f"ID of group: {message.chat.id}")

