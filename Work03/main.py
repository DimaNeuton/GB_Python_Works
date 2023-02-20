# Дан список чисел. Определите сколько в нем встречается различных чисел

import random
# my_list = []
# for _ in range(15):
#     my_list.append(random.randint(0, 9))
# print(my_list)
# переводим список в множество
# print(set(my_list)) # множество - это упорядоченный набор не повторяющихся данных

# Дана последовательность из N целых чисел и число K. Необходимо
# сдвинуть всю последовательность на K элементов вправо. K>0

# n = int(input("Введите n: "))
# k = int(input("Введите k: "))
# list1 = []
# for _ in range(n):
#     list1.append(random.randint(0, 9))
# print(list1)
# for _ in range(k):
#     temp = list1.pop((len(list1) - 1))
#     list1.insert(0, temp)
# list1 = list1[-k:] + list1[:-k]
# print(list1)

# Напишите программу для печати всех уникальных значений в словаре

list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
         {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
set1 = set()
set2 = set()
for item in list1:
    for key, value in item.items():
        set1.add(value.strip())
        set2.add(key.strip())
print(set1)
print(set2)



