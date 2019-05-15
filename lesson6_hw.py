# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# ----------------------------------------------------------------------------------------
# Сравнеие объема занимаемой памяти Именованным кортежем и объектом класса
# Информация о системе:
# os.uname()
# Out[9]: posix.uname_result(sysname='Linux', nodename='denis-asus', release='4.18.0-18-generic',
# version='#19~18.04.1-Ubuntu SMP Fri Apr 5 10:22:13 UTC 2019', machine='x86_64')
# sys.version
# Out[14]: '3.7.3 (default, Mar 27 2019, 22:11:17) \n[GCC 7.3.0]'
# ----------------------------------------------------------------------------------------

import collections
from pympler import asizeof

Factories_nt = collections.namedtuple('Factories_nt', ['name', 'quarters', 'profit'])

class Factories_cl:
    def __init__(self, name, quarters):
        self.name = name
        self.quarters = quarters
        self.profit = sum(self.quarters)


name = 'Factory'
quarters = [100, 120, 90, 130]

f_nt = Factories_nt(name, quarters, sum(quarters))
f_cl = Factories_cl(name, quarters)

print(f'Namedtuple element: {f_nt}\n'
      f'Size of namedtuple element with pympler: {asizeof.asizeof(f_nt)} bytes')
print(f'Namedtuple element: {f_cl.__dict__}\n'
      f'Size of namedtuple element: {asizeof.asizeof(f_cl)} bytes')

# ----------------------------------------------------------------------------------------
# Результаты:
# Namedtuple element: Factories_nt(name='Factory', quarters=[100, 120, 90, 130], profit=440)
# Size of namedtuple element with pympler: 384 bytes
# Namedtuple element: {'name': 'Factory', 'quarters': [100, 120, 90, 130], 'profit': 440}
# Size of namedtuple element: 656 bytes
# ----------------------------------------------------------------------------------------
# В результате объем занимаемой памяти объектом класса оказался почти в два раза больше,
# чем Именованный кортеж с аналогичными атрибутами
# ----------------------------------------------------------------------------------------
