# Найти факториал числа

# number = int(input('Введите число: '))
# i = 1
# fact = 1
# # while i <= number:
# #     fact *= i
# #     i += 1
# for i in range(1, number + 1):
#     fact *= i
# print(f"Факториал числа {number} = {fact}")

#  --------------------------------------

# Дано натуральное число а>1. Определить каким по счету
# числом Фебоначи, если не является вывести -1

# number = int(input("Введите число: "))
# f_number_2 = 1
# f_number_1 = 0
# f_number = 0
# count = 2
# while f_number <= number:
#     f_number = f_number_1 + f_number_2
#     f_number_1 = f_number_2
#     f_number_2 = f_number
#     count += 1
#     if f_number == number:
#         print(f"Число {number} соответствует {count} числу последовательности")
#         break
# else:
#     print(-1)

# Ввести количество арбузов, ввести массу каждого арбуза,
# определить самы легкий и тяжелый арбуз.

from random import randint

number = int(input("Введите количество арбузов: "))
i = 1
max = 0
min = 30
while i <= number:
    mass = randint(1, 30)
    print(f'Масса {i} арбуза = {mass}')
    if mass >= max: max = mass
    if mass <= min: min = mass
    i += 1
print(f"Максимальная масса - {max} кг\nМинимальная масса - {min} кг")
