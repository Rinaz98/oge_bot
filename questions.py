import random

import texts
from texts import *
import type_2
from extra_def_for_questions import type_3_1
from extra_def_for_type_6 import type_6


def type_10_quest():
    type = random.randint(1, 3)
    min_max = ['МИНИМАЛЬНОЕ', 'МАКСИМАЛЬНОЕ']
    binary_int = random.randint(20, 150)
    binary_s = str(bin(binary_int))
    binary_s = binary_s[2:] + '\u2082'
    oct_int = random.randint(20, 150)
    oct_s = str(oct(oct_int))
    oct_s = oct_s[2:] + '\u2088'
    hex_int = random.randint(20, 150)
    hex_s = str(hex(hex_int))
    hex_s = hex_s[2:] + '\u2081' + '\u2086'
    if type == 1:
        min_or_max = random.randint(0, 1)
        if min_or_max == 0:
            quest_answer = min(binary_int, oct_int, hex_int)
            quest_text = f'Среди приведённых ниже трёх чисел, записанных в различных системах счисления, найдите ' \
                         f'{min_max[0]} и запишите его в ответе в десятичной системе счисления. В ответе запишите ' \
                         f'только число, основание системы счисления указывать не нужно. \n\n{binary_s}, {oct_s}, {hex_s}'
        elif min_or_max == 1:
            quest_answer = max(binary_int, oct_int, hex_int)
            quest_text = f'Среди приведённых ниже трёх чисел, записанных в различных системах счисления, найдите ' \
                         f'{min_max[1]} и запишите его в ответе в десятичной системе счисления. В ответе запишите ' \
                         f'только число, основание системы счисления указывать не нужно. \n\n{binary_s}, {oct_s}, {hex_s}'
    elif type == 3:
        quest_text = f'Найдите значение выражения \n\n{binary_s} - {oct_s} + {hex_s}'
        quest_answer = binary_int - oct_int + hex_int
    elif type == 2:
        if oct_int > hex_int:
            quest_text = f'Сколько натуральных чисел расположено в интервале \n\n{hex_s} \u2264 X \u2264 {oct_s}'
            quest_answer = oct_int - hex_int + 1
        else:
            quest_text = f'Сколько натуральных чисел расположено в интервале \n\n{oct_s} \u2264 X \u2264 {hex_s}'
            quest_answer = hex_int - oct_int + 1
    return quest_text, quest_answer


def type_1_quest():
    coding_types = [8, 16]
    coding = random.randint(0, 1)
    random_text = random.randint(0, 3)
    quest_type = random.randint(0, 1)
    byte = [8, 10, 12, 14, 16, 18, 20, 22, 24]
    bytes_count = random.choice(byte)
    quest_text = f'В одной из кодировок каждый символ кодируется {coding_types[coding]} битами. ' \
                 f'Вова написал текст (в нём нет лишних пробелов):\n\n{type_1_texts[random_text]}\n\nЗатем ' \
                 f'он добавил в список ещё одно название. Заодно он добавил необходимые запятые и ' \
                 f'пробелы. При этом размер нового предложения в данной кодировке оказался на {bytes_count} байт больше, ' \
                 f'чем размер исходного предложения. Напишите в ответе длину добавленного названия в символах.'
    quest_answer = int((bytes_count - coding_types[coding] / 8 * 2) / (coding_types[coding] / 8))
    return quest_text, quest_answer


def type_2_quest():
    type = random.randint(0, 2)
    question = random.randint(0, 9)
    if type == 0:
        quest_answer = type_2.answers_0[question]
        quest_text = f'От разведчика было получено сообщение:\n\n {type_2.secret_code_0[question]}\n\n В этом сообщении ' \
                     f'зашифрован пароль – последовательность русских букв. В пароле использовались только буквы ' \
                     f'А, Б, К, Л, О, С; каждая буква кодировалась двоичным словом по таблице, показанной на рисунке. ' \
                     f'Расшифруйте сообщение. Запишите в ответе пароль.'
        image = type_2.images[type]
    elif type == 1:
        quest_answer = type_2.answers_1[question]
        quest_text = f'От разведчика было получено сообщение:\n\n {type_2.secret_code_1[question]}\n\n В этом сообщении ' \
                     f'зашифрован пароль – последовательность русских букв. В пароле использовались только буквы ' \
                     f'А, Б, К, Л, О, С; каждая буква кодировалась двоичным словом по таблице, показанной на рисунке. ' \
                     f'Расшифруйте сообщение. Запишите в ответе пароль.'
        image = type_2.images[type]
    elif type == 2:
        quest_answer = type_2.answers_2[question]
        secret_code = ''
        for i in type_2.secret_code_2[question]:
            secret_code += str(i) + '\n'
        quest_text = f'Ваня шифрует русские слова, записывая вместо каждой буквы её номер в алфавите (без пробелов). ' \
                     f'Номера букв даны в таблице.\nНекоторые шифровки можно расшифровать несколькими способами. ' \
                     f'Например, 311333 может означать «ВАЛЯ», может — «ЭЛЯ», а может — «ВААВВВ». Даны четыре шифровки:' \
                     f'\n\n{secret_code}\nТолько одна из них расшифровывается единственным способом. Найдите её и ' \
                     f'расшифруйте. Получившееся слово запишите в качестве ответа.'
        image = type_2.images[type]
    return quest_text, image, quest_answer


def type_3_quest():
    text, answer = type_3_1()
    return text, answer


def type_5_quest():
    start_int = random.randint(2, 27)
    quest_type = random.randint(0, 1)
    mult_int = random.randint(2, 3)
    add_int = random.randint(1, 2)
    secret_add = random.randint(5, 20)
    secret_mult = random.randint(2, 7)
    commands_sum = 0
    end_int = start_int
    while not (6 < commands_sum < 9):
        commands = [random.randint(1, 2) for i in range(5)]
        commands_sum = sum(commands)
    commands_str = ''.join(map(str, commands))
    if quest_type == 0:  # найти значение в команде сложения
        for j in commands:
            if j == 1:
                end_int += secret_add
            elif j == 2:
                end_int *= mult_int
        text = f'У исполнителя Бета две команды, которым присвоены номера:\n\n' \
               f'1.прибавь b\n2. умножь на {mult_int}\n\n(b – неизвестное натуральное число)\n' \
               f'Выполняя первую из них, Бета увеличивает число на экране на b, а выполняя вторую, ' \
               f'умножает это число на {mult_int}. Программа для исполнителя Бета – это последовательность номеров команд. ' \
               f'Известно, что программа \n\n{commands_str}\n\nпереводит число {start_int} в число {end_int}. Определите значение b.'
        answer = secret_add
    elif quest_type == 1:  # найти значение в команде умножения
        for j in commands:
            if j == 1:
                end_int += add_int
            elif j == 2:
                end_int *= secret_mult
        text = f'У исполнителя Альфа две команды, которым присвоены номера:\n\n' \
               f'1. прибавь {add_int}\n2. умножь на b\n\n(b - неизвестное натуральное число; b ≥ 2)' \
               f'Выполняя первую из них, Альфа увеличивает число на экране на {add_int}, а выполняя вторую, ' \
               f'умножает это число на b. Известно, что программа \n\n{commands_str}\n\nпереводит число {start_int} в число ' \
               f'{end_int}. Определите значение b.'
        answer = secret_mult
    return text, answer


def type_6_quest():
    text, answer = type_6()
    return text, answer


def type_7_quest():
    task_ints = [random.randint(0, 4), random.randint(0, 5), random.randint(0, 11), random.randint(0, 14),
                 random.randint(0, 10), random.randint(0, 7)]
    text = f'Файл <b>{texts.type_7_filename[task_ints[3]]}{texts.type_7_fileextension[task_ints[4]]}</b> был выложен в каталоге ' \
           f'<b>{texts.type_7_catalogs[task_ints[5]]}</b> на сайте <b>{texts.type_7_domen_2[task_ints[2]]}</b>' \
           f'<b>{texts.type_7_domen_1[task_ints[1]]}</b>, доступ к котрому осуществляется по протоколу ' \
           f'<b>{texts.type_7_protocols[task_ints[0]]}</b>. Ниже даны фрагменты адреса файла, закодированные числами от 1 до 8.' \
           f'Запишите последовательность этих цифр, кодирующая адрес указанного файла в сети Интернет.\n'
    quest = random.sample(range(1, 9), 8)
    quest_dict = dict(zip([texts.type_7_protocols[task_ints[0]], '://', texts.type_7_domen_1[task_ints[1]],
                           texts.type_7_domen_2[task_ints[2]], texts.type_7_catalogs[task_ints[5]],
                           texts.type_7_filename[task_ints[3]], texts.type_7_fileextension[task_ints[4]], '/'],
                          [quest[0], quest[1], quest[2], quest[3], quest[4], quest[5], quest[6], quest[7]]))
    answer = str(quest[0]) + str(quest[1]) + str(quest[3]) + str(quest[2]) + str(quest[7]) + str(quest[4])
    answer += str(quest[7]) + str(quest[5]) + str(quest[6])
    text_next = []
    for i in quest_dict:
        text_next.append(str(quest_dict[i]) + ') ' + str(i))
    text_next.sort()
    for i in text_next:
        text += i + '\n'
    return text, answer


def type_8_quest():
    a = random.randint(2000, 20000)
    b = random.randint(2000, 20000)
    a_and_b = random.randint(100, min(a, b))
    a_or_b = a + b - a_and_b
    quest_type = random.randint(1, 5)
    if quest_type == 1:
        text = 'Ниже приведены запросы и количество страниц, которые нашел поисковый сервер по этим запросам в ' \
               f'некотором сегменте Интернета:\n\nбархатистый  |  бархатный  {a_or_b}\n\n бархатистый  {a}\n\n' \
               f'бархатистый  &  бархатный  {a_and_b}\nСколько страниц будет найдено по запросу\nбархатный'
        answer = b
    elif quest_type == 2:
        text = 'Ниже приведены запросы и количество страниц, которые нашел поисковый сервер по этим запросам в ' \
               f'некотором сегменте Интернета:\n\nбархатистый  |  бархатный  {a_or_b}\n\n бархатный  {b}\n\n' \
               f'бархатистый  &  бархатный  {a_and_b}\nСколько страниц будет найдено по запросу\nбархатистый'
        answer = a
    elif quest_type == 3:
        text = 'Ниже приведены запросы и количество страниц, которые нашел поисковый сервер по этим запросам в ' \
               f'некотором сегменте Интернета:\n\nбархатистый  {a}\n\n бархатный  {b}\n\n' \
               f'бархатистый  &  бархатный  {a_and_b}\nСколько страниц будет найдено по запросу\nбархатистый  |  бархатный'
        answer = a_or_b
    elif quest_type == 4:
        text = 'Ниже приведены запросы и количество страниц, которые нашел поисковый сервер по этим запросам в ' \
              f'некотором сегменте Интернета:\n\nбархатистый  {a}\n\n бархатный  {b}\n\n' \
              f'бархатистый  |  бархатный  {a_or_b}\nСколько страниц будет найдено по запросу\nбархатистый  &  бархатный'
        answer = a_and_b
    elif quest_type == 5:
        text = f'Ниже приведены запросы и количество страниц, которые нашел поисковый сервер по этим запросам в ' \
               f'некотором сегменте Интернета:\n\nбархатистый  &  (бархатный  |  кристалл)  {max(a, b)}\n\n' \
               f'бархатистый  &  бархатный  {min(a, b)}\n\n бархатистый  &  бархатный  &  кристалл  50\n\n' \
               f'Сколько страниц будет найдено по запросу\n бархатистый  &  кристалл'
        answer = max(a, b) - min(a, b) - 50
    return text, answer