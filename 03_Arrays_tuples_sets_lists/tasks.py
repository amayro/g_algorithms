import random


def task_section(task):
    print(f'\n{"":-^10} №{task} {"":-^10}')


# №1 ------------------------------------------------------------------------------------
task_section(1)
"""
1.	В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

count_multiples = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            count_multiples[j-2] += 1

for idx, num in enumerate(count_multiples):
    print(idx + 2, num)


# №2 ------------------------------------------------------------------------------------
task_section(2)
"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

numbers = [random.randint(0, 20) for i in range(6)]
multiples_idx = [idx for idx, num in enumerate(numbers) if num % 2 == 0]

print(numbers)
print('Индексы четных элементов,', multiples_idx)


# №3 ------------------------------------------------------------------------------------
task_section(3)
"""
3.	В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы.
"""

numbers = [random.randint(0, 20) for i in range(6)]

num_min = min(numbers)
num_max = max(numbers)

idx_min = numbers.index(num_min)
idx_max = numbers.index(num_max)

replace_numbers = numbers[:]
replace_numbers[idx_min], replace_numbers[idx_max] = replace_numbers[idx_max], replace_numbers[idx_min]
print(numbers)
print(replace_numbers)


# №4 ------------------------------------------------------------------------------------
task_section(4)
"""
4.	Определить, какое число в массиве встречается чаще всего.
"""

numbers = [random.randint(0, 10) for i in range(5)]

max_frq = 0
for i in numbers:
    frq = 0
    for j in numbers:
        if j == i:
            frq += 1
    if max_frq < frq:
        max_frq = frq
        num = i

print(numbers)
if max_frq > 1:
    print(f"Число {num}, Кол-во повторений {max_frq}")
else:
    print('Все числа уникальны')


# №5 ------------------------------------------------------------------------------------
task_section(5)
"""
5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
"""

numbers = [random.randint(-10, 10) for i in range(6)]

negative_numbers = list(filter(lambda x: x < 0, numbers))
num_negative_max = max(negative_numbers) if negative_numbers else None

print(numbers)
if num_negative_max:
    print(f'Число {num_negative_max}, Индекс {numbers.index(num_negative_max)}')
else:
    print('Отрицательных чисел нет')

# # №6 ------------------------------------------------------------------------------------
task_section(6)
"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

numbers = [random.randint(0, 20) for i in range(6)]

num_min = min(numbers)
num_max = max(numbers)

idx_min = numbers.index(num_min)
idx_max = numbers.index(num_max)

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

sum_numbers = numbers[idx_min+1:idx_max]
summa = sum(sum_numbers) if sum_numbers else None
print(numbers)
if summa:
    print(f'Искомые числа {sum_numbers}, Их сумма {summa}')
else:
    print('Максимальный и минимальный элемент соседи', num_min, num_max)


# №7 ------------------------------------------------------------------------------------
task_section(7)
"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

numbers = [random.randint(0, 20) for i in range(6)]
print(numbers)

min_numbers = []
for i in range(2):
    min_numbers.append(min(numbers))
    numbers.remove(min(numbers))

print('Два минимальных числа', ' '.join(map(str, min_numbers)))


# №8 ------------------------------------------------------------------------------------
task_section(8)
"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

col = 5
row = 4
arr = []
for i in range(row):
    arr.append([])
    arr[i] = [random.randint(0, 10) for j in range(col - 1)]
    arr[i].append(sum(arr[i]))
    print(arr[i])


# # №9 ------------------------------------------------------------------------------------
task_section(9)
"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

col = 5
row = 4
arr = []
min_numbers = []

for i in range(row):
    arr.append([])
    arr[i] = [random.randint(0, 20) for j in range(col)]
    print(''.join(map(lambda x: str(x).rjust(5), arr[i])))

print()
t_arr = []
min_numbers_col = []

for j in range(col):
    t_arr.append([])
    for i in range(row):
        t_arr[j].append(arr[i][j])
        print(f"{t_arr[j][i]:>5}", end='')
    print()
    min_numbers_col.append(min(t_arr[j]))

print('\nИскомый элемент', max(min_numbers_col))
