
from operator import itemgetter
from typing import List, Tuple, Any


class CD:
    """CD-диск"""

    def __init__(self, id, title, sal, lib_id):
        self.id = id
        self.title = title
        self.sal = sal
        self.lib_id = lib_id


class Lib:
    """Библиотека CD-дисков"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class CDLib:
    """
    '' для реализации
    связи многие-ко-многим
    """

    def __init__(self, lib_id, cd_id):
        self.lib_id = lib_id
        self.cd_id = cd_id

# библиотеки
libs = [
    Lib(1, 'NewCD'),
    Lib(2, 'CDAGE'),
    Lib(3, 'Discs'),
    Lib(4, 'CDshop'),
    Lib(5, 'Archive'),
]

# Диски
cds = [
    CD(1, 'All music', 250, 3),
    CD(2, 'Orchestra music', 220, 2),
    CD(3, 'Rock music', 450, 5),
    CD(4, 'Amy Winehouse Pop hits', 350, 2),
    CD(5, 'Jazz for all', 550, 3),
]

cds_libs = [
    CDLib(1, 3),
    CDLib(2, 2),
    CDLib(3, 5),
    CDLib(4, 2),
    CDLib(5, 3),

    CDLib(1, 2),
    CDLib(2, 4),
    CDLib(3, 1),
    CDLib(4, 4),
    CDLib(5, 1),
]
def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
one_to_many = [(c.title, c.sal,l.name)
               for l in libs
               for c in cds
               if c.lib_id == l.id]

# Соединение данных многие-ко-многим
many_to_many_temp = [(l.name, cl.lib_id, cl.cd_id)
                     for l in libs
                     for cl in cds_libs
                     if l.id == cl.lib_id]

many_to_many = [(c.title, c.sal, lib_name)
                for lib_name, lib_id, cd_id in many_to_many_temp
                for c in cds if c.id == cd_id]

print('Задание B1:')
res11 = []
for title, _, libs in one_to_many:
    if title[0] == "A":
        res11.append((title, libs))
print(res11, "\n")

print('Задание В2')
res12 = [[one_to_many[0][2], one_to_many[0][1]]]
for title, sal, libs in one_to_many:
    if libs == res12[len(res12)-1][0]:
        if sal < res12[len(res12)-1][1]:

            res12[len(res12)-1][1] = sal
    else:
            res12.append([libs, sal])
print(sorted(res12, key=itemgetter(1)), "\n")


print('Задание В3')
res13 = []
for title, _, libs in many_to_many:
    res13.append((title, libs))
# print (res_13)
print(sorted(res13, key=itemgetter(0)), "\n")

if __name__ == '__main__':
    main()
