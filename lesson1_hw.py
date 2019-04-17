# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''
num = input('Input the number: ')
num_sum = 0
num_mult = 1

for i in range(len(num)):
    num_sum += (int(num) // (1 * (10 ** i)) % 10)
    num_mult *= (int(num) // (1 * (10 ** i)) % 10)

print(num_sum)
print(num_mult)

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

a = 5
b = 6
print(f'bin a = {bin(a)}, bin b = {bin(b)}')
print(f'bin or  : {bin(a | b)} <=> {a | b}')
print(f'bin and : {bin(a & b)} <=> {a & b}')
print(f'bin xor : {bin(a ^ b)} <=> {a ^ b}')
print(f'swap to left a << 2: {bin(a << 2)} <=> {a << 2} <=> a = 5 * (2 ** 2) = {5 * (2 ** 2)}')
print(f'swap to right a >> 2: {bin(a >> 2)} <=> {a >> 2} <=> a = 5 // (2 ** 2) = {5 // (2 ** 2)}')

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y=kx+b, проходящей через эти точки.

x1 = float(input('Input x1: '))
y1 = float(input('Input y1: '))
x2 = float(input('Input x2: '))
y2 = float(input('Input y2: '))

if x1 == x2:
    print(f'x = {x1:.2f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k:.2f} * x + {b:.3f}')

# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

num_start = int(input('Input start int number: '))
num_end = int(input('Input end int number: '))
print(f'Random number from range is {random.randint(num_start, num_end)}')

num_start = float(input('Input start int number: '))
num_end = float(input('Input end int number: '))
print(f'Random number from range is {random.uniform(num_start, num_end)}')

num_start = ord(input('Input start int symbol: '))
num_end = ord(input('Input end int symbol: '))
print(f'Random number from range is {chr(random.randint(num_start, num_end))}')

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они
# стоят и сколько между ними находится букв.

chr1 = ord(input('Input the first letter: '))
chr2 = ord(input('Input the second letter: '))
chr1 = chr1 - ord('a') + 1
chr2 = chr2 - ord('a') + 1
print(f'place fo then first letter {chr1}; of the second - {chr2}')
print(f'letters between of input letters - {abs(chr2 - chr1)- 1}')
'''
# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter = int(input('Input number of any letter (1 - 26): '))
begin = ord('a')
print(f'Yur letter is "{chr(begin + letter - 1)}"')
