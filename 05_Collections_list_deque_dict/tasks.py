import collections
from functools import reduce


def task_section(task):
    print(f'\n{"":-^10} №{task} {"":-^10}')


# №1 ------------------------------------------------------------------------------------
task_section(1)
"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

count_companies = int(input('Введите кол-во компаний: '))

companies = []

for i in range(count_companies):
    title = input('Введите название компании: ')
    profit_q1, profit_q2, profit_q3, profit_q4 = map(int, input('Квартальные прибыли через пробел: ').split(' '))
    company = {
        'title': title,
        'profit_q1': profit_q1,
        'profit_q2': profit_q2,
        'profit_q3': profit_q3,
        'profit_q4': profit_q4,
        'profit_year': profit_q1 + profit_q2 + profit_q3 + profit_q4,
    }

    companies.append(company)

profit_col = collections.Counter()
for company in companies:
    profit_comp = company.copy()
    del profit_comp['title']
    profit_col += collections.Counter(profit_comp)

print()
for company in companies:
    print(company)

average_profit = profit_col['profit_year'] / len(companies)

print('Суммарная прибыль компаний: ', profit_col)
print('Средняя годовая прибыль компаний: ', average_profit)
print('Прибыль выше среднего: ', [x['title'] for x in companies if x['profit_year'] >= average_profit])
print('Прибыль ниже среднего: ', [x['title'] for x in companies if x['profit_year'] < average_profit])


# №2 ------------------------------------------------------------------------------------
task_section(2)
"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

num_1 = 'A2'
num_2 = 'C4F'

num_1, num_2 = list(num_1), list(num_2)
print(num_1)
print(num_2)

# deq_1 = collections.deque(num_1)
# deq_2 = collections.deque(num_2)
#
# print(deq_1)
# print(deq_2)


class Hexadecimal:
    def __init__(self, num_lst):
        self._hex_codes = '0123456789ABCDEF'
        self.dec_num = reduce(lambda x, y: x * 16 + (self._hex_codes.find(y)), num_lst, 0)

    def __add__(self, other):
        self.sum = self.dec_num + other.dec_num
        self.sum = self._convert_hex(self.sum)

    def __mul__(self, other):
        self.mult = self.dec_num * other.dec_num
        self.mult = self._convert_hex(self.mult)

    def _convert_hex(self, number_dec):
        hex_num = ''
        s = number_dec
        while True:
            chas = s // 16
            ost = s % 16
            str_ost = self._hex_codes[ost]
            hex_num = str_ost + hex_num

            if chas <= 16:
                str_chas = self._hex_codes[chas]
                return str_chas + hex_num
            s = chas


num_1 = Hexadecimal(num_1)
num_2 = Hexadecimal(num_2)

num_1 + num_2
num_1 * num_2

print(list(num_1.sum))
print(list(num_1.mult))
