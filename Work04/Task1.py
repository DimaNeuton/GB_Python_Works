 # Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

user_collect1_length = int(input('Введите длину первого множества: '))     # не понятно зачем это делаем
user_collect2_length = int(input('Введите длину второго множества: '))
user_collect1_str = input('Введите первый набор целых чисел через пробел: ')     # вводим строку из чисел
user_collect2_str = input('Введите второй набор целых чисел через пробел: ')
user_collect1_list_str = user_collect1_str.split()     # преобразуем строку в список из строк
user_collect2_list_str = user_collect2_str.split()
user_collect1_list_int = [int(item) for item in user_collect1_list_str]     # преобразуем список из строк в список из целых чисел
user_collect2_list_int = [int(item) for item in user_collect2_list_str]
user_collect1_set_int = set(user_collect1_list_int)     # преобразуем список в множество
user_collect2_set_int = set(user_collect2_list_int)
result_collect = user_collect1_set_int.intersection(user_collect2_set_int)     # находим общие элементы в множествах
print(result_collect)