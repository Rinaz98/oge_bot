import random


def type_3_1():
    choise = []
    all_answers = []
    task = [['НАИБОЛЬШЕЕ', 'НАИМЕНЬШЕЕ'], ['ИСТИННО', 'ЛОЖНО'], ['И', 'ИЛИ'], ['НЕ', ''], ['ЧЕТНОЕ', 'НЕЧЕТНОЕ'],
            ['<', '\u2264', '>', '\u2265'], ['<', '\u2264', '>', '\u2265'], ['int', 'str']]
    first_comp = random.randint(4, 50)
    sec_comp = random.randint(7, 60)
    for i in range(9):
        if i == 5 or i == 6:
            choise.append(random.randint(0, 3))
        else:
            choise.append(random.randint(0, 1))
    if task[7][choise[7]] == 'int':
        sec_arg = f'(X {task[6][choise[6]]} {sec_comp})'
    else:
        sec_arg = f'(X {task[4][choise[7]]})'
    text = f'Напишите {task[0][choise[0]]} целое число x, для которого {task[1][choise[1]]} высказывание:\n\n' \
           f'{task[3][choise[3]]} (X {task[5][choise[5]]} {first_comp} ) {task[2][choise[2]]} ' \
           f'{task[3][choise[8]]} {sec_arg}'
    if choise[1] == 0:
        if choise[2] == 0:
            if choise[3] == 0:
                if choise[5] == 0:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 1:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 2:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 3:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
            else:
                if choise[5] == 0:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) and not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) and not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) and not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) and not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i < first_comp) and not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i < first_comp) and (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 1:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 2:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) and not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) and not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) and not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) and not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i > first_comp) and not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i > first_comp) and (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 3:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
        else:
            if choise[3] == 0:
                if choise[5] == 0:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 1:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 2:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 3:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
            else:
                if choise[5] == 0:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) or not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) or not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) or not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) or not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i < first_comp) or not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i < first_comp) or (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 1:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 2:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) or not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) or not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) or not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) or not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i > first_comp) or not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i > first_comp) or (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 3:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or not (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or (i < sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or not (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or (i <= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or not (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or (i > sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or not (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or (i >= sec_comp) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or not (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or not (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or (i % 2 == 0) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or (i % 2 == 1) == True:
                                        all_answers.append(i)
                                    else:
                                        continue
    else:
        if choise[2] == 0:
            if choise[3] == 0:
                if choise[5] == 0:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i < first_comp) and (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) and (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 1:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) and (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) and (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 2:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i > first_comp) and (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) and (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 3:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) and (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) and (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
            else:
                if choise[5] == 0:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) and not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) and not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) and not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) and not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i < first_comp) and not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i < first_comp) and (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) and (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 1:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i <= first_comp) and (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) and (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 2:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) and not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) and not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) and not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) and not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i > first_comp) and not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i > first_comp) and (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) and (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 3:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i >= first_comp) and (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) and (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
        else:
            if choise[3] == 0:
                if choise[5] == 0:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i < first_comp) or (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i < first_comp) or (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 1:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i <= first_comp) or (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i <= first_comp) or (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 2:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i > first_comp) or (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i > first_comp) or (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 3:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if not (i >= first_comp) or (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if not (i >= first_comp) or (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
            else:
                if choise[5] == 0:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) or not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) or not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) or not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i < first_comp) or not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i < first_comp) or not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i < first_comp) or (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i < first_comp) or (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 1:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i <= first_comp) or (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i <= first_comp) or (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 2:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) or not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) or not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) or not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i > first_comp) or not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i > first_comp) or not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i > first_comp) or (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i > first_comp) or (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                elif choise[5] == 3:
                    if choise[7] == 0:
                        if choise[6] == 0:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or not (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or (i < sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 1:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or not (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or (i <= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 2:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or not (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or (i > sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        elif choise[6] == 3:
                            if choise[8] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or not (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or (i >= sec_comp) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                    else:
                        if choise[8] == 0:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or not (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or not (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                        else:
                            if choise[7] == 0:
                                for i in range(100):
                                    if (i >= first_comp) or (i % 2 == 0) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
                            else:
                                for i in range(100):
                                    if (i >= first_comp) or (i % 2 == 1) == False:
                                        all_answers.append(i)
                                    else:
                                        continue
    if len(all_answers) == 0:
        return type_3_1()
    else:
        if choise[0] == 0:
            answer = max(all_answers)
        else:
            answer = min(all_answers)
        return text, answer
