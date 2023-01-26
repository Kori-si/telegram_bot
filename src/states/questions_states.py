from aiogram.dispatcher.filters.state import State, StatesGroup


class QuestionsState(StatesGroup):
    answer_1 = State()
    answer_2 = State()
    answer_3 = State()
    answer_4 = State()
