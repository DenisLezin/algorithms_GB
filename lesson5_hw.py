# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

import collections

quart = 4
Factories = collections.namedtuple('Factories', ['name', 'quarters', 'profit'])
all_factories = set()

num_factories = int(input('Insert the number of factories: '))
total_profit = 0

for i in range(num_factories):
    profit = 0
    quarters = []
    name = input(f'Input name of the {i + 1} factory: ')

    for j in range(quart):
        quarters.append(int(input(f'Input the {j + 1} quarter profit: ')))
        profit += quarters[j]

    fact = Factories(name=name, quarters=tuple(quarters), profit=profit)

    all_factories.add(fact)
    total_profit += profit

avg = total_profit / num_factories

print(f'Average profit is {avg}')

print('Factories with profit equal or greater then average:')
for i in all_factories:
    if i.profit >= avg:
        print(f'Factory "{i.name}", profit = {i.profit}')

print('Factories with profit less then average:')
for i in all_factories:
    if i.profit < avg:
        print(f'Factory "{i.name}", profit = {i.profit}')
