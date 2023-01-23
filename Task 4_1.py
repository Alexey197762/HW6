# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

from random import randint
list = [randint(-10, 10) for i in range(10)]
print(list)
count = 0
unique = []
for x in list:
    if x not in unique:
        count += 1
        unique.append(x)
print(len(unique))