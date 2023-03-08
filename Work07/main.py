import random

# my_list = [i for i in range(10)]
# print(my_list)
#
# my_list = [i**2 for i in range(10) if i != 5]
# print(my_list)
#
# my_list = [random.randint(0, 100) for i in range(10) if i != 5]
# print(my_list)

# string = '1 2 2 4 5 1 4'
# my_list = string.split()
# my_list = list(map(lambda x: int(x)**2, my_list))
# my_list = [i + 10 for i in my_list]
# print(my_list)

# list1 = [1, 2, 2, 4, 5, 1, 4]
# # def func(x):
# #     if x%2 == 0:
# #         return x
# # list1 = list(filter(func, list1))
# list1 = list(filter(lambda x: x % 2 == 0, list1))
# print(list1)

# list1 = [1, 2, 2, 4, 5, 1, 4]
# for i, k in enumerate(list1, 4):
#     if k > 3:
#         print(i, k)

# string = '1 2 2 4 5 1 4'
# numbers = [5, 3, 8, 2, 9 , 4, 6, 3, 7]
# print(numbers)
# print(string)
# new_list = list(zip(string, numbers))
# print(new_list)

# my_list = string.split()
#
# operation = {'+' : lambda x, y: x + y,
#              '-' : lambda x, y: x - y,
#              '*' : lambda x, y: x * y,
#              '/' : lambda x, y: x / y}
#
# example = '3 + 4 - 2'
# example = example.split()
# for i, item in enumerate(example):
#     if item in ['+', '-']:
#         example[i-1] = operation.get(item)(example[i-1], example[i+1])

import math

list_of_orbits = [(3, 5), (5, 7), (7, 3)]

def find_farthest_orbit(list_of_orbits):
    max_area = 0
    list_of_areas = list(map(lambda x: x[0] * x[1] * math.pi, list_of_orbits))
    for _ in list_of_areas:
        if _ > max_area:
            max_area = _
    for i, item in enumerate(list_of_areas):
        if item == max_area: return list_of_orbits[i]
print(find_farthest_orbit(list_of_orbits))






