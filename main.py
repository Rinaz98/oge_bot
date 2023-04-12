from aiogram import executor, types
from create_bot import dp
import test_10_1_2
import get_images_ids
import test_10_1_2_3
import text10_1_2_3_5
import test_10_1_2_3_5_6
import test_10_1_2_3_5_6_7
import test_10_1_2_3_5_6_7_8

test_10_1_2.register_handlers_test_10_1_2(dp)
get_images_ids.register_handlers_admin_main(dp)
test_10_1_2_3.register_handlers_test_10_1_2_3(dp)
text10_1_2_3_5.register_handlers_test_10_1_2_3_5(dp)
test_10_1_2_3_5_6.register_handlers_test_10_1_2_3_5_6(dp)
test_10_1_2_3_5_6_7.register_handlers_test_10_1_2_3_5_6_7(dp)
test_10_1_2_3_5_6_7_8.register_handlers_test_10_1_2_3_5_6_7_8(dp)


async def on_startup(_):
    print('Bot started')


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer('Добро пожаловать.')
    await message.answer('Используйте команду /help, чтобы получить мини-инструкцию.\n'
                         'Используйте команду /test, чтобы получить спиоск доступных тестов.')


@dp.message_handler(commands='help')
async def bot_help(message: types.Message):
    await message.answer('Для выполнения теста выберите нужный тест.\n'
                         'Команда /test выведет список доступных тестов.\n'
                         'Функция изменения ответов пока недоступна.\n'
                         'Чтобы отменить прохождение теста напишите боту слово "отмена.\n')


@dp.message_handler(commands='test')
async def tests_list(message: types.Message):
    await message.answer('/test3 - тест по 10, 1 и 2 заданиям из ОГЭ\n'
                         '/test4 - тест по 10, 1, 2 и 3 заданиям из ОГЭ\n'
                         '/test5 - тест по 10, 1, 2, 3 и 5 заданиям из ОГЭ\n'
                         '/test6 - тест по 10, 1, 2, 3, 5 и 6 заданиям из ОГЭ\n'
                         '/test7 - тест по 10, 1, 2, 3, 5, 6 и 7 заданиям из ОГЭ\n'
                         '/test8 - тест по 10, 1, 2, 3, 5, 6, 7 и 8 заданиям из ОГЭ\n')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
