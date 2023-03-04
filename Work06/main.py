# Дан список чисел. Посчитайте сколько в нем пар равных друг другу.

# from random import  randint
# list_len = int(input('Введите размер списка: '))
# list1 = []
# dict1 = {}
# couple_count = 0
# for i in range(list_len):
#     list1.append(randint(1,10))
# print(list1)
# for i in range(list_len):
#     if not list1[i] in dict1:
#         dict1[list1[i]] = 1
#     if list1[i] in list1[i + 1:]:
#         dict1[list1[i]] += 1
# print(dict1)
# for k, v in dict1.items():
#     couple_count += v // 2
# print(couple_count)
# couple_count = 0
# list1_set = set(list1)
# for item in list1_set:
#     couple_count += list1.count(item) // 2
# print(couple_count)

# Два различных натуральных числа n и m называются дружественными, если
# сумма делителей числа n, включая единицу, но исключая само n, равна числу m
# и наоборот. По данному числу К выведите все пары дружественных чисел,
# каждое из которыъх не превосходит К

def devisor_sum(pivot1: int):
    sum1 = 0
    for i in range(1, pivot1//2 + 1):
        if pivot1 % i == 0:
            sum1 += i
    return sum1

number = int(input('Введите число: '))
for i in range(1, number):
    for j in range(i, number):
        if devisor_sum(j) == i and devisor_sum(i) == j:
                print(f'Дружественные числа - {i} и {j}')

















