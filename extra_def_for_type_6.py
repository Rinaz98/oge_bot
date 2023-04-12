import random


def type6_1(x, y, xx, yy):
    if y <= yy and x <= xx:
        return '1'
    else:
        return '0'


def type6_2(x, y, xx, yy):
    if y < yy and x <= xx:
        return '1'
    else:
        return '0'


def type6_3(x, y, xx, yy):
    if y < yy and x < xx:
        return '1'
    else:
        return '0'


def type6_4(x, y, xx, yy):
    if y >= yy and x < xx:
        return '1'
    else:
        return '0'


def type6_5(x, y, xx, yy):
    if y >= yy and x >= xx:
        return '1'
    else:
        return '0'


def type6_6(x, y, xx, yy):
    if y > yy and x <= xx:
        return '1'
    else:
        return '0'


def type6_7(x, y, xx, yy):
    if y >= yy and x <= xx:
        return '1'
    else:
        return '0'


def type6_8(x, y, xx, yy):
    if y <= yy and x < xx:
        return '1'
    else:
        return '0'


def type6_9(x, y, xx, yy):
    if y <= yy and x > xx:
        return '1'
    else:
        return '0'


def type6_10(x, y, xx, yy):
    if y <= yy and x >= xx:
        return '1'
    else:
        return '0'


def type6_11(x, y, xx, yy):
    if y < yy and x >= xx:
        return '1'
    else:
        return '0'


def type6_12(x, y, xx, yy):
    if y < yy and x > xx:
        return '1'
    else:
        return '0'


def type6_13(x, y, xx, yy):
    if y > yy and x < xx:
        return '1'
    else:
        return '0'


def type6_14(x, y, xx, yy):
    if y > yy and x > xx:
        return '1'
    else:
        return '0'


def type6_15(x, y, xx, yy):
    if y > yy and x >= xx:
        return '1'
    else:
        return '0'


def type6_16(x, y, xx, yy):
    if y >= yy and x > xx:
        return '1'
    else:
        return '0'


def type6_1_2(x, y, xx, yy):
    if y <= yy or x <= xx:
        return '1'
    else:
        return '0'


def type6_2_2(x, y, xx, yy):
    if y < yy or x <= xx:
        return '1'
    else:
        return '0'


def type6_3_2(x, y, xx, yy):
    if y < yy or x < xx:
        return '1'
    else:
        return '0'


def type6_4_2(x, y, xx, yy):
    if y >= yy or x < xx:
        return '1'
    else:
        return '0'


def type6_5_2(x, y, xx, yy):
    if y >= yy or x >= xx:
        return '1'
    else:
        return '0'


def type6_6_2(x, y, xx, yy):
    if y > yy or x <= xx:
        return '1'
    else:
        return '0'


def type6_7_2(x, y, xx, yy):
    if y >= yy or x <= xx:
        return '1'
    else:
        return '0'


def type6_8_2(x, y, xx, yy):
    if y <= yy or x < xx:
        return '1'
    else:
        return '0'


def type6_9_2(x, y, xx, yy):
    if y <= yy or x > xx:
        return '1'
    else:
        return '0'


def type6_10_2(x, y, xx, yy):
    if y <= yy or x >= xx:
        return '1'
    else:
        return '0'


def type6_11_2(x, y, xx, yy):
    if y < yy or x >= xx:
        return '1'
    else:
        return '0'


def type6_12_2(x, y, xx, yy):
    if y < yy or x > xx:
        return '1'
    else:
        return '0'


def type6_13_2(x, y, xx, yy):
    if y > yy or x < xx:
        return '1'
    else:
        return '0'


def type6_14_2(x, y, xx, yy):
    if y > yy or x > xx:
        return '1'
    else:
        return '0'


def type6_15_2(x, y, xx, yy):
    if y > yy or x >= xx:
        return '1'
    else:
        return '0'


def type6_16_2(x, y, xx, yy):
    if y >= yy or x > xx:
        return '1'
    else:
        return '0'


def type_6():
    tasks = [['<', '\u2264', '>', '\u2265'], ['<', '\u2264', '>', '\u2265'], ['or', 'and'], ['ДА', 'НЕТ']]
    choices = []
    result = ''
    task_ints = [random.randint(10, 200) for i in range(2)]
    test_ints = [random.randint(10, 200) for i in range(20)]
    for i in range(4):
        if i == 0 or i == 1:
            choices.append(random.randint(0, 3))
        else:
            choices.append(random.randint(0, 1))
    if choices[2] == 0:
        if choices[0] == 0:
            if choices[1] == 0:
                for i in range(0, 10, 2):
                    result += type6_3_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 1:
                for i in range(0, 10, 2):
                    result += type6_2_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 2:
                for i in range(0, 10, 2):
                    result += type6_12_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 3:
                for i in range(0, 10, 2):
                    result += type6_11_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
        elif choices[0] == 1:
            if choices[1] == 0:
                for i in range(0, 10, 2):
                    result += type6_8_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 1:
                for i in range(0, 10, 2):
                    result += type6_1_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 2:
                for i in range(0, 10, 2):
                    result += type6_9_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 3:
                for i in range(0, 10, 2):
                    result += type6_10_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
        elif choices[0] == 2:
            if choices[1] == 0:
                for i in range(0, 10, 2):
                    result += type6_13_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 1:
                for i in range(0, 10, 2):
                    result += type6_6_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 2:
                for i in range(0, 10, 2):
                    result += type6_14_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 3:
                for i in range(0, 10, 2):
                    result += type6_15_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
        elif choices[0] == 3:
            if choices[1] == 0:
                for i in range(0, 10, 2):
                    result += type6_16_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 1:
                for i in range(0, 10, 2):
                    result += type6_7_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 2:
                for i in range(0, 10, 2):
                    result += type6_4_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 3:
                for i in range(0, 10, 2):
                    result += type6_5_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
    else:
        if choices[0] == 0:
            if choices[1] == 0:
                for i in range(0, 10, 2):
                    result += type6_3(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 1:
                for i in range(0, 10, 2):
                    result += type6_2(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 2:
                for i in range(0, 10, 2):
                    result += type6_12(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 3:
                for i in range(0, 10, 2):
                    result += type6_11(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
        elif choices[0] == 1:
            if choices[1] == 0:
                for i in range(0, 10, 2):
                    result += type6_8(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 1:
                for i in range(0, 10, 2):
                    result += type6_1(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 2:
                for i in range(0, 10, 2):
                    result += type6_9(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 3:
                for i in range(0, 10, 2):
                    result += type6_10(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
        elif choices[0] == 2:
            if choices[1] == 0:
                for i in range(0, 10, 2):
                    result += type6_13(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 1:
                for i in range(0, 10, 2):
                    result += type6_6(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 2:
                for i in range(0, 10, 2):
                    result += type6_14(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 3:
                for i in range(0, 10, 2):
                    result += type6_15(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
        elif choices[0] == 3:
            if choices[1] == 0:
                for i in range(0, 10, 2):
                    result += type6_16(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 1:
                for i in range(0, 10, 2):
                    result += type6_7(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 2:
                for i in range(0, 10, 2):
                    result += type6_4(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
            elif choices[1] == 3:
                for i in range(0, 10, 2):
                    result += type6_5(task_ints[1], task_ints[0], test_ints[i + 1], test_ints[i])
    text = f'Дана программа:\n\nx = int(input())\ny = int(input())\n' \
           f'if y {tasks[0][choices[0]]} {task_ints[0]} {tasks[2][choices[2]]} x {tasks[1][choices[1]]} {task_ints[1]}:\n' \
           f'       print("ДА")\nelse:\n     print("НЕТ")\n\n' \
           f'Было проведено 10 запусков этой программы, при которых в качестве значений переменных x и y ' \
           f'вводились следующие пары чисел:\n' \
           f'({test_ints[0]}, {test_ints[1]}); ({test_ints[2]}, {test_ints[3]}); ({test_ints[4]}, {test_ints[5]}); ' \
           f'({test_ints[6]}, {test_ints[7]}); ({test_ints[8]}, {test_ints[9]}); ({test_ints[10]}, {test_ints[11]}); ' \
           f'({test_ints[12]}, {test_ints[13]}); ({test_ints[14]}, {test_ints[15]}); ({test_ints[16]}, {test_ints[17]}); ' \
           f'({test_ints[18]}, {test_ints[19]})\n\nСколько было запусков, при которых программа напечатала ' \
           f'«{tasks[3][choices[3]]}»?'
    if choices[3] == 0:
        answer = result.count('1')
    else:
        answer = result.count('0')
    return text, answer
