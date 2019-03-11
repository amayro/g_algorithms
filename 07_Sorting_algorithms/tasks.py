import random
import timeit


def task_section(task):
    print(f'\n{"":-^10} №{task} {"":-^10}')


# №1 ------------------------------------------------------------------------------------
task_section(1)
"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. 
"""

numbers = [random.randint(-100, 100) for _ in range(10)]


def bubble_reverse(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1 - j):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


print('Исходный массив:', numbers)
print('Обратная пузырьковая:', bubble_reverse(numbers[:]))

# №2 ------------------------------------------------------------------------------------
task_section(2)
"""
2. Отсортируйте по возрастанию методом слияния одномерный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""


def merge_sort(nums):
    if len(nums) > 1:
        center = len(nums) // 2
        left = nums[:center]
        right = nums[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        return nums


print('Исходный массив:', numbers)
print('Сортировка слиянием:', merge_sort(numbers[:]))


# №3 ------------------------------------------------------------------------------------
task_section(3)
"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
"""

import statistics

numbers = [2, 8, 5, 1, 4]


def median(nums):
    half = len(nums) // 2
    nums.sort()
    if not len(nums) % 2:
        return (nums[half - 1] + nums[half]) / 2
    return nums[half]


print('Исходный массив:', numbers)
print('Медиана:', median(numbers[:]))
print('Медиана statistics:', statistics.median(numbers[:]))

#  ------------------------------------------------------------------------------------
task_section(4)


def bubble(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


def insertion(nums):
    for i in range(len(nums)):
        j = i - 1
        key = nums[i]
        while nums[j] > key and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


numbers = [random.randint(-100, 100) for _ in range(10)]

print('Исходный массив:', numbers)
print('Сортировка пузырьковая:', bubble(numbers[:]))
print('Сортировка вставками:  ', insertion(numbers[:]))
print('Сортировка быстрая:    ', quicksort(numbers[:]))

time_bubble = timeit.timeit("bubble(numbers)", setup="from __main__ import bubble, numbers", number=100)
time_insertion = timeit.timeit("insertion(numbers)", setup="from __main__ import insertion, numbers", number=100)
time_quicksort = timeit.timeit("quicksort(numbers)", setup="from __main__ import quicksort, numbers", number=100)
time_merge = timeit.timeit("merge_sort(numbers)", setup="from __main__ import merge_sort, numbers", number=100)

print(time_bubble)
print(time_insertion)
print(time_quicksort)
print(time_merge)

"""
Замеры времени алгоритмов сортировки
100 элементов:
Сортировка пузырьковая: 0.06826326493795386
Сортировка вставками: 0.0020771900320177006
Сортировка быстрая: 0.0184890091439128
Сортировка слиянием: 0.0335509709666237

1000 элементов:
Сортировка пузырьковая: 6.135812749917102
Сортировка вставками: 0.022228975189671374
Сортировка быстрая: 0.1516174043045453
Сортировка слиянием: 0.48519659517924474
"""
