from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.inlines.callback_data import questions_callback
from keyboards.defoults.commands import commands_keyboard
from keyboards.inlines.user_keyboards import basket_keyboards
from loader import dp, db, bot
from states.questions_states import QuestionsState




@dp.callback_query_handler(questions_callback.filter(action=question))
async def start_buy(call: CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer(text='Оцените качество оформления заказа от 1 до 10: ')
    await QuestionsState.answer_1.set()

@dp.message_handler(state=QuestionsState.answer_1)
async def get_date(message: Message, state: FSMContext):
    await state.update_data({'one': message.text})
    await message.answer(text='Оцените удобство оформления заказа от 1 до 10: ')
    await QuestionsState.answer_2.set()

@dp.message_handler(state=QuestionsState.answer_2)
async def get_time(message: Message, state: FSMContext):
    await state.update_data({'two': message.text})
    await message.answer(text='Оцените удобство использования нашего бота от 1 до 10: ')
    await QuestionsState.answer_3.set()

@dp.message_handler(state=QuestionsState.answer_3)
async def get_time(message: Message, state: FSMContext):
    await state.update_data({'three': message.text})
    await message.answer(text='Укажите Ваше имя.')
    await QuestionsState.answer_4.set()

@dp.message_handler(state=QuestionsState.answer_4)
async def get_name(message: Message, state: FSMContext):
    data = await state.get_data()
    text = f'Заявка' \
           f'\nВаше имя: {message.text}' \
           f'\nПервый вопрос: {data["one"]}' \
           f'\nВторой вопрос: {data["two"]}' \
           f'\nТретий вопрос: {data["three"]}'
    await message.answer(text=text,
                         reply_markup=commands_keyboard)
    await state.reset_state()