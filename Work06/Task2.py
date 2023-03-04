# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

list1 = []
for _ in range(10):
    list1.append(randint(-10, 10))
print(list1)
max_limit = 7
min_limit = -3
list2 = []
i = 0
while i < len(list1):
    if list1[i] >= min_limit and list1[i] <= max_limit:
        list2.append(i)
    i += 1
print(list2)




