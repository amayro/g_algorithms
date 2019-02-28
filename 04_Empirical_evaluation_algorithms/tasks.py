import random
import timeit
import cProfile


def task_section(task):
    print(f'\n{"":-^10} №{task} {"":-^10}')


# №1 ------------------------------------------------------------------------------------
task_section(1)
"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(random.random() * pow(10, 10))
print('Число:', number)


def method_1():
    count_even = 0
    count_odd = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f'Четных {count_even}\nНечетных:{count_odd}')


def method_2(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        n = num % 10
        num = num // 10
        if n % 2 == 0:
            even += 1
            return method_2(num, even, odd)
        else:
            odd += 1
            return method_2(num, even, odd)


def memorize(func):
    def wrapper(n, memory={}):
        value = memory.get(n)
        if value is None:
            value = func(n)
            memory[n] = value
        return value
    return wrapper


@memorize
def method_3(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        n = num % 10
        num = num // 10
        if n % 2 == 0:
            even += 1
            return method_2(num, even, odd)
        else:
            odd += 1
            return method_2(num, even, odd)


method_1()
print(method_2(number))
time_meth_1 = timeit.timeit("method_1", setup="from __main__ import method_1")
time_meth_2 = timeit.timeit("method_2(number)", setup="from __main__ import method_2, number")
time_meth_3 = timeit.timeit("method_3(number)", setup="from __main__ import method_3, number")

print('\nЗатраченное время на исполнение с помощью'
      f'\n{"- цикла:":25} {time_meth_1}'
      f'\n{"- рекурсии:":25} {time_meth_2}'
      f'\n{"- рекурсия + мемоизация:":25} {time_meth_3}')

# ------------------------------------------------------------------------------------
print('\nЗамеры объединения чисел в строку')
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))

# ------------------------------------------------------------------------------------
print('\nЗамеры c помощью cProfile')


def cprofile_test():
    method_1()

    method_2(number)
    method_3(number)


cProfile.run('cprofile_test()')


# №2 ------------------------------------------------------------------------------------
task_section(2)
"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Используя алгоритм «Решето Эратосфена»
Без использования «Решета Эратосфена»;
"""

# idx = int(input())
idx = 100


def simple_method_1(idx):
    n = idx * idx
    a = []
    for i in range(n + 1):
        a.append(i)

    a[1] = 0
    i = 2

    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
            if len(b) == idx:
                break
    return b, f'{idx} по счету простое число: {b[idx - 1]}'


def simple_method_2(idx):
    n = idx
    lst = []
    first = 2
    while len(lst) != idx:
        for i in range(first, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lst.append(i)
        n += 1
        first = n
    return lst, f'{idx} по счету простое число: {lst[idx - 1]}'


print(simple_method_1(idx)[0])
print(simple_method_1(idx)[1])
print(simple_method_2(idx)[0])
print(simple_method_2(idx)[1])


time_meth_1 = timeit.timeit("simple_method_1(idx)", setup="from __main__ import simple_method_1, idx", number=1000)
time_meth_2 = timeit.timeit("simple_method_2(idx)", setup="from __main__ import simple_method_2, idx", number=1000)

print('\nЗатраченное время на исполнение '
      f'\n{"- Используя алгоритм «Решето Эратосфена»:":25} {time_meth_1}'
      f'\n{"- Без использования «Решета Эратосфена»:":25} {time_meth_2}')
