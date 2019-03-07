import random
import sys
from functools import reduce

from memory_profiler import profile


def task_section(task):
    print(f'\n{"":-^10} №{task} {"":-^10}')


# №1 ------------------------------------------------------------------------------------
task_section(1)
"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

# разрадность ОС - 64bit, версия Python - 3.6


@profile
def find_idx():
    numbers = [random.randint(0, 200) for i in range(60000)]
    multiples_idx = [idx for idx, num in enumerate(numbers) if num % 2 == 0]

    print(numbers)
    print('Индексы четных элементов,', multiples_idx)
    print(sys.getrefcount(multiples_idx))


find_idx()

"""
Line #    Mem usage    Increment   Line Contents
================================================
    25     12.9 MiB     12.9 MiB   @profile
    26                             def find_idx():
    31     13.3 MiB      0.1 MiB       numbers = [random.randint(0, 200) for i in range(60000)]
    32     14.0 MiB      0.1 MiB       multiples_idx = [idx for idx, num in enumerate(numbers) if num % 2 == 0]
    33
    34     13.8 MiB      0.0 MiB       print(numbers)
    35     13.7 MiB      0.0 MiB       print('Индексы четных элементов,', multiples_idx)
    36     13.7 MiB      0.0 MiB       print(sys.getrefcount(multiples_idx))
"""


@profile
def replace_digits():
    numbers = [random.randint(0, 200) for i in range(60000)]

    num_min = min(numbers)
    num_max = max(numbers)

    idx_min = numbers.index(num_min)
    idx_max = numbers.index(num_max)

    replace_numbers = numbers[:]
    replace_numbers[idx_min], replace_numbers[idx_max] = replace_numbers[idx_max], replace_numbers[idx_min]
    print(numbers)
    print(replace_numbers)
    print(sys.getrefcount(replace_numbers))


replace_digits()

"""
Line #    Mem usage    Increment   Line Contents
================================================
    54     13.1 MiB     13.1 MiB   @profile
    55                             def replace_digits():
    59     13.5 MiB      0.1 MiB       numbers = [random.randint(0, 200) for i in range(60000)]
    60
    61     13.5 MiB      0.0 MiB       num_min = min(numbers)
    62     13.5 MiB      0.0 MiB       num_max = max(numbers)
    63
    64     13.5 MiB      0.0 MiB       idx_min = numbers.index(num_min)
    65     13.5 MiB      0.0 MiB       idx_max = numbers.index(num_max)
    66
    67     13.6 MiB      0.1 MiB       replace_numbers = numbers[:]
    68     13.6 MiB      0.0 MiB       replace_numbers[idx_min], replace_numbers[idx_max] = replace_numbers[idx_max], replace_numbers[idx_min]
    69     13.6 MiB      0.0 MiB       print(numbers)
    70     13.6 MiB      0.0 MiB       print(replace_numbers)
    71     13.6 MiB      0.0 MiB       print(sys.getrefcount(replace_numbers))
"""


idx = 100


@profile
def eratosfen(idx):
    n = idx * 100
    a = [i for i in range(n + 1)]

    a[1] = 0
    i = 2

    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j += i
        i += 1

    b = [i for i in a if i != 0]
    print(sys.getrefcount(i))
    print(sys.getrefcount(a))
    return b, f'{idx} по счету простое число: {b[idx - 1]}'


eratosfen(idx)

"""
Line #    Mem usage    Increment   Line Contents
================================================
    94     13.0 MiB     13.0 MiB   @profile
    95                             def eratosfen(idx):
    96     13.0 MiB      0.0 MiB       n = idx * 100
    97     13.1 MiB      0.0 MiB       a = [i for i in range(n + 1)]
    98
    99     13.1 MiB      0.0 MiB       a[1] = 0
   100     13.1 MiB      0.0 MiB       i = 2
   101
   102     13.1 MiB      0.0 MiB       while i <= n:
   103     13.1 MiB      0.0 MiB           if a[i] != 0:
   104     13.1 MiB      0.0 MiB               j = i + i
   105     13.1 MiB      0.0 MiB               while j <= n:
   106     13.1 MiB      0.0 MiB                   a[j] = 0
   107     13.1 MiB      0.0 MiB                   j += i
   108     13.1 MiB      0.0 MiB           i += 1
   109
   110     13.1 MiB      0.0 MiB       b = [i for i in a if i != 0]
   111     13.1 MiB      0.0 MiB       return b, f'{idx} по счету простое число: {b[idx - 1]}'

"""

# №2 ------------------------------------------------------------------------------------
task_section(2)
"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

num_1 = 'A2'
num_1 = list(num_1)


class Hexadecimal:
    def __init__(self, num_lst):
        self._hex_codes = '0123456789ABCDEF'
        self.dec_num = reduce(lambda x, y: x * 16 + (self._hex_codes.find(y)), num_lst, 0)


class HexadecimalTwo:
    __slots__ = ['_hex_codes', 'dec_num']

    def __init__(self, num_lst):
        self._hex_codes = '0123456789ABCDEF'
        self.dec_num = reduce(lambda x, y: x * 16 + (self._hex_codes.find(y)), num_lst, 0)


hex_1 = Hexadecimal(num_1)
hex_2 = HexadecimalTwo(num_1)

print(sys.getsizeof(hex_1.__dict__), hex_1.__dict__)
print(sys.getsizeof(hex_2.__slots__), hex_2.__slots__)

"""
68 {'_hex_codes': '0123456789ABCDEF', 'dec_num': 162}
44 ['_hex_codes', 'dec_num']
"""
