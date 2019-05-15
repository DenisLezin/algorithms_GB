# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

lst = [i for i in range(2, 100)]
counter = 0

for i in range(2, 10):
    for j in lst:
        if j % i == 0:
            counter += 1
    print(f'{i} = {counter}')
    counter = 0

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй
# массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random
lst = [random.randint(1, 99) for _ in range(11)]
lst_even = []

for i in range(len(lst)):
    if lst[i] % 2 == 0:
        lst_even.append(i)

print(lst)
print(lst_even)

# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

import random
lst = [random.randint(1, 99) for _ in range(6)]
min_elm_ind = 0
max_elm_ind = 0

print(lst)

for i in range(len(lst)):
    if lst[i] < lst[min_elm_ind]:
        min_elm_ind = i
    elif lst[i] > lst[max_elm_ind]:
        max_elm_ind = i

print(f'max = {lst[max_elm_ind]}\nmin = {lst[min_elm_ind]}')
lst[min_elm_ind], lst[max_elm_ind] = lst[max_elm_ind], lst[min_elm_ind]
print(lst)

# 4. Определить, какое число в массиве встречается чаще всего.
import random
lst = [random.randint(1, 6) for _ in range(11)]
num = lst[0]
vol = 1

for i in range(len(lst)):
    n = 1
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            n += 1
        if n > vol:
            vol = n
            num = lst[i]

print(lst)
print(f'{num} is the most popular number, it met {vol} times')

# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
lst = [random.randint(-100, -1) for _ in range(11)]
ind = -1

for i in range(len(lst)):
    if lst[i] < 0 and ind == -1:
        ind = i
    elif 0 > lst[i] > lst[ind]:
        ind = i

print(lst)
print(f"max negative num is {lst[ind]},\nit's index is {ind}")

# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
lst = [random.randint(1, 100) for _ in range(11)]
ind_max = 0
ind_min = 0

print(lst)

for i in range(1, len(lst)):
    if lst[ind_max] < lst[i]:
        ind_max = i
    elif lst[ind_min] > lst[i]:
        ind_min = i

print(f'max {lst[ind_max]}\nmin {lst[ind_min]}')
print(f'sum = {sum(lst[min(ind_min, ind_max) + 1: max(ind_min, ind_max)])}')

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

lst = [[random.randint(-10, 11) for _ in range(3)] for _ in range(3)]
lst_t = list(zip(*lst))
lst_min = [i[0] for i in lst_t]

for line in range(len(lst_t)):
    for i in lst_t[line][1:]:
        if i < lst_min[line]:
            lst_min[line] = i

print(lst)
print(lst_t)
print(lst_min)
print(f'max num from minimum of columns is {max(lst_min)}')
