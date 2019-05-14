# Пару месяцев назад небходимо было отсортировать довольно большой массив (~200 000)
# Нашел быструю сортировку. Не совсем понял как она работает, но использовал.
# Наконец вы объяснили, сасибо. Я понял принцип. Могу осознанно применять с рекурсией.
# Одако ту, что я использовал использует что-то типа стека - вот ее пока не очень понял )
# Ниже быстрая с рекурсией. Решил брать случайный элемент в качестве опорного.

from random import randint, choice

example = [randint(-100, 100) for _ in range(10)]

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = choice(arr)
        pivot_index = arr.index(pivot)
        less = [i for i in arr[:pivot_index] + arr[pivot_index + 1:] if i < pivot]
        greater = [i for i in arr[:pivot_index] + arr[pivot_index + 1:] if i >= pivot]
#        print(pivot, arr, less, greater)

        return quick_sort(greater) + [pivot] + quick_sort(less)

print(example)
print(quick_sort(example))
