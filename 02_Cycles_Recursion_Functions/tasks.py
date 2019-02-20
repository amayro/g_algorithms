# Решить задачи без использования массивов.

import random


def task_section(task):
    print(f'\n{"":-^10} №{task} {"":-^10}')


# №1 ------------------------------------------------------------------------------------
task_section(1)
"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""

# while True:
#     data = input('Введите числа и знак операции через пробел (3 2 -). 0 для выхода качестве знака операции: ')
#     arg_1, arg_2, operation = data.split(" ")
#     arg_1, arg_2 = int(arg_1), int(arg_2)
#
#     if operation == '0':
#         break
#
#     if operation in ('+', '-', '*', '/'):
#         if operation == '+':
#             result = arg_1 + arg_2
#         elif operation == '-':
#             result = arg_1 - arg_2
#         elif operation == '*':
#             result = arg_1 * arg_2
#         elif operation == '/':
#             if arg_2 == 0:
#                 print(f'На ноль делить нельзя')
#                 continue
#             else:
#                 result = arg_1 / arg_2
#         print(f'Результат: {result}')
#     else:
#         print("Неверный знак операции!")


# №2 ------------------------------------------------------------------------------------
task_section(2)
"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

# number = input('Введите число: ')
number = '34560'

count_even = 0
count_odd = 0

for digit in number:
    if int(digit) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(f'Четных {count_even}\nНечетных:{count_odd}')


# №3 ------------------------------------------------------------------------------------
task_section(3)
"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

# number = input('Введите число: ')
number = '3486'

print('Перевернутое число:', ''.join(reversed(number)))
print('Перевернутое число:', number[::-1])

number = int(number)
new_number = 0

while number > 0:
    new_number = new_number * 10 + number % 10
    number = number // 10
print('Перевернутое число:', new_number)


# №4 ------------------------------------------------------------------------------------
task_section(4)
"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

# count_numbers = int(input('Введите количество элементов: '))
count_numbers = 6
new_num = 1
numbers = ''

for num in range(count_numbers):
    numbers += str(new_num) + ' '
    new_num /= -2

print('Ряд чисел:', numbers)


# №5 ------------------------------------------------------------------------------------
task_section(5)
"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def get_ascii_symbols(a, b, columns=10):
    for i in range(a, b + 1):
        print(f'{i:<3} - {chr(i):<5}', end='')
        if i % columns == 0:
            print()


get_ascii_symbols(32, 127)

# # №6 ------------------------------------------------------------------------------------
task_section(6)
"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

# secret_number = random.randint(0, 100)
# attempt = 0
#
# while attempt < 10:
#     number = int(input('Угадайте число: '))
#     if number < secret_number:
#         print('Больше')
#     elif number > secret_number:
#         print('Меньше')
#     else:
#         print('Верно!')
#         break
#     attempt += 1
# else:
#     print('Загаданное число', secret_number)


# №7 ------------------------------------------------------------------------------------
task_section(7)
"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

n = 10

result_1 = 0
result_2 = n * (n + 1) / 2

for num in range(n+1):
    result_1 += num

print(result_1, result_2, result_1 == result_2)

# №8 ------------------------------------------------------------------------------------
task_section(8)
"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

sequence = '1233456677789'
number = '3'
print(sequence.count(number))


# # №9 ------------------------------------------------------------------------------------
task_section(9)
"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

nubmer = int(input('Введите число:'))
max_sum = 0
max_num = 0
while nubmer != 0:
    num = nubmer
    sum = 0
    while nubmer > 0:
        sum += nubmer % 10
        nubmer //= 10
    if sum > max_sum:
        max_sum = sum
        max_num = num
    nubmer = int(input('Введите число:'))
print('Число', max_num, 'имеет максимальную сумму цифр:', max_sum)
