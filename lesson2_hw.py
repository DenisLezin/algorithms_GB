# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться
# при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный
# знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
    sign = input('Input sign of operation ("+", "-", "/", "*")\nor "0" to quit: ')
    if sign == '0':
        break
    if sign == '+' or sign == '-' or sign == '/' or sign == '*':
        x = float(input('Input x: '))
        y = float(input('Input y: '))
        if sign == '+':
            print(f'x + y = {x + y:.2f}')
        elif sign == '-':
            print(f'x - y = {x - y:.2f}')
        elif sign == '*':
            print(f'x * y = {x * y:.2f}')
        elif sign == '/':
            if y == 0:
                print('Unavailable operation - Dividing by zero!')
            else:
                print(f'x / y = {x / y:.2f}')
    else:
        print('Unknown operator, try again')
    print()

# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Input number: ')
even = 0
odd = 0
if num.isdigit():
    for i in num:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
print(f'Even numbers: {even}, odd: {odd}')

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

num = int(input('Input number: '))
res = 0
while num > 0:
    res = res * 10 + num % 10
    num = num // 10
print(res)

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Input the number of sequence elements: '))
elm = 1
summ = 0
for _ in range(n):
    summ += elm
    elm /= -2
    print(elm, end=' ')
print(f'\nSum = {summ}')

# 5. Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

start = 32
stop = 127
for i in range(start, stop + 1):
    print(f'{i} - {chr(i)}', end=' ')
    if i % 10 == 1:
        print()

# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random
num = random.randint(0, 100)

for i in range(1, 11):
    answer = int(input(f'Input num, {i} attempt: '))
    if answer > num:
        print('Num is smaller')
    elif answer < num:
        print('Num is bigger')
    else:
        print(f'You find right number, attempt {i}')
        break
if i == 10:
    print(f'You loose, right number was {num}')

# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def sum_nat(n):
    return n if n == 1 else n + sum_nat(n - 1)

num = int(input('Input natural number: '))

print(f'Sum of all natural numbers = {sum_nat(num)}')
print(f'n * (n + 1) / 2 = {num * (num + 1) / 2}')
print(f'check condition 1+2+...+n = n(n+1)/2: {sum_nat(num) == num * (num + 1) / 2}')
