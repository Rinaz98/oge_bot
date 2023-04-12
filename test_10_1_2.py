from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot
from questions import type_10_quest, type_1_quest, type_2_quest
from aiogram.dispatcher.filters import Text


class FSMTest_10_1_2(StatesGroup):
    name = State()
    grade = State()
    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()
    question_6 = State()
    question_7 = State()
    question_8 = State()
    question_9 = State()
    mark = State()


name = 'name'
grade = 'grade'


async def set_start(message: types.Message):
    await FSMTest_10_1_2.name.set()
    await message.answer('Введите свои фамилию и имя')


async def get_student_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMTest_10_1_2.next()
    await message.answer('Укажите ваш класс')


async def get_grade(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['grade'] = message.text
    text, answer = type_10_quest()
    async with state.proxy() as data:
        data['answer_1'] = str(answer)
    await FSMTest_10_1_2.next()
    await message.answer(text)
    # await message.answer(answer)  # потом убрать


async def quest_n1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_1'] = message.text
    text, answer = type_10_quest()
    async with state.proxy() as data:
        data['answer_2'] = str(answer)
    await FSMTest_10_1_2.next()
    await message.answer(text)
    # await message.answer(answer)  # потом убрать


async def quest_n2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_2'] = message.text
    text, answer = type_10_quest()
    async with state.proxy() as data:
        data['answer_3'] = str(answer)
    await FSMTest_10_1_2.next()
    await message.answer(text)
    # await message.answer(answer)  # потом убрать


async def quest_n3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_3'] = message.text
    text, answer = type_1_quest()
    async with state.proxy() as data:
        data['answer_4'] = str(answer)
    await FSMTest_10_1_2.next()
    await message.answer(text)
    # await message.answer(answer)  # потом убрать


async def quest_n4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_4'] = message.text
    text, answer = type_1_quest()
    async with state.proxy() as data:
        data['answer_5'] = str(answer)
    await FSMTest_10_1_2.next()
    await message.answer(text)
    # await message.answer(answer)  # потом убрать


async def quest_n5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_5'] = message.text
    text, image, answer = type_2_quest()
    async with state.proxy() as data:
        data['answer_6'] = str(answer).lower()
    await FSMTest_10_1_2.next()
    await message.answer(text)
    await message.answer_photo(image)
    # await message.answer(answer)  # потом убрать


async def quest_n6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_6'] = message.text.lower()
    text, image, answer = type_2_quest()
    async with state.proxy() as data:
        data['answer_7'] = str(answer).lower()
    await FSMTest_10_1_2.next()
    await message.answer(text)
    await message.answer_photo(image)
    # await message.answer(answer)  # потом убрать


async def quest_n7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_7'] = message.text.lower()
    text, image, answer = type_2_quest()
    async with state.proxy() as data:
        data['answer_8'] = str(answer).lower()
    await FSMTest_10_1_2.next()
    await message.answer(text)
    await message.answer_photo(image)


# await message.answer(answer)  # потом убрать


async def quest_n8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_8'] = message.text.lower()
    text, image, answer = type_2_quest()
    async with state.proxy() as data:
        data['answer_9'] = str(answer).lower()
    await FSMTest_10_1_2.next()
    await message.answer(text)
    await message.answer_photo(image)
    # await message.answer(answer)  # потом убрать


async def quest_n9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_9'] = message.text.lower()
        data['mark'] = 0
        if data['question_1'] == data['answer_1']:
            data['mark'] += 2
        if data['question_2'] == data['answer_2']:
            data['mark'] += 2
        if data['question_3'] == data['answer_3']:
            data['mark'] += 2
        if data['question_4'] == data['answer_4']:
            data['mark'] += 1
        if data['question_5'] == data['answer_5']:
            data['mark'] += 1
        if data['question_6'] == data['answer_6']:
            data['mark'] += 2
        if data['question_7'] == data['answer_7']:
            data['mark'] += 2
        if data['question_8'] == data['answer_8']:
            data['mark'] += 2
        if data['question_9'] == data['answer_9']:
            data['mark'] += 2
    end_mark = data['mark'] // 2.7
    await state.finish()
    await message.answer(f'Ваша оценка {end_mark}')
    if end_mark <= 2:
        await message.answer_photo(
            'AgACAgIAAxkBAAIBF2P7dwfh6TpCBSPeIlK_oPJUP-LRAAJ-xTEbaD7hS4nsiot36EP6AQADAgADcwADLgQ')
        await message.answer_voice('AwACAgIAAxkBAAIKwWP_KWMNh1TQJzIrQYjBdT5SUaVrAAL1JgACz3v4S-lSR7xBn6g4LgQ')
    elif end_mark == 3:
        await message.answer_sticker('CAACAgIAAxkBAAIBFmP7dufLoVNUa9I7Zdv2g9fAOp6-AAJSDwACCz85SFRWYSU_4GJbLgQ')
        await message.answer_voice('AwACAgIAAxkBAAIKw2P_Kavdc5bkjs5rjYl8OMPKrb_SAAL3JgACz3v4S47QocHAmCgtLgQ')
    elif end_mark == 4:
        await message.answer_photo(
            'AgACAgIAAxkBAAIBGWP7dzsp7LxB4KOPDxlJR6qWsiNzAAJlyTEb_6sZSUsnFLLKfoZ_AQADAgADcwADLgQ')
        await message.answer_voice('AwACAgIAAxkBAAIKwmP_KYpt0YtRGvhEieIXZMuZaCm-AAL2JgACz3v4S2BXaHDABJIiLgQ')
    else:
        await message.answer_photo(
            'AgACAgIAAxkBAAIBG2P7d6yvf6Lsc6xYJjgiWOkOXoXjAAKDxTEbaD7hS4xL055Xh6-qAQADAgADcwADLgQ')
        await message.answer_voice('AwACAgIAAxkBAAIKwGP_KRVw-iIMxrbjRLp4NtkDvtzzAALbKQACdov5S-VKgNwb_UVRLgQ')
    await bot.send_message(287660359,
                           f'{data[name]} из класса {data[grade]} получил оценку {end_mark}. \n'
                           f'Вся инфа по ученику {data}')


async def cancel_test(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Прохождение теста отменено.')
    await message.answer('Используйте команду /test, чтобы начать тест.')


def register_handlers_test_10_1_2(dp: Dispatcher):
    dp.register_message_handler(set_start, commands='test3', state=None)
    dp.register_message_handler(get_student_name, state=FSMTest_10_1_2.name)
    dp.register_message_handler(cancel_test, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(get_grade, state=FSMTest_10_1_2.grade)
    dp.register_message_handler(quest_n1, state=FSMTest_10_1_2.question_1)
    dp.register_message_handler(quest_n2, state=FSMTest_10_1_2.question_2)
    dp.register_message_handler(quest_n3, state=FSMTest_10_1_2.question_3)
    dp.register_message_handler(quest_n4, state=FSMTest_10_1_2.question_4)
    dp.register_message_handler(quest_n5, state=FSMTest_10_1_2.question_5)
    dp.register_message_handler(quest_n6, state=FSMTest_10_1_2.question_6)
    dp.register_message_handler(quest_n7, state=FSMTest_10_1_2.question_7)
    dp.register_message_handler(quest_n8, state=FSMTest_10_1_2.question_8)
    dp.register_message_handler(quest_n9, state=FSMTest_10_1_2.question_9)
