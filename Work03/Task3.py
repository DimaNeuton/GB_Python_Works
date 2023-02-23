# 1. Задаем с клавиатуры максимальную степень многочлена

# 2. Сгенерировать 2 многочлена и сложить их

# реплэйсы стрипы списки сплиты словари срезы
# парсинг
# koef*x**7 koef*x**2 koef*x koef

from random import randint

pow1 = int(input('Введите показатель степени первого многочлена: '))

dict1 = {}     # Создаем словарь
i = pow1
while i >= 0:
    dict1[i] = randint(-10, 10)
    i -= 1
i = pow1
polinomial1 = ''
# превращаем словарь в строку и форматируем
for key, value in dict1.items():
    if key > 1:
        if value < -1:
            polinomial1 += str(value) + '*x**' + str(key)
        if value == 1:
            polinomial1 += '+x**' + str(key)
        if value == -1:
            polinomial1 += '-x**' + str(key)
        if value > 1:
            polinomial1 += '+' + str(value) + '*x**' + str(key)
    if key == 1:
        if value < -1:
            polinomial1 += str(value) + '*x'
        if value == 1:
            polinomial1 += '+x**'
        if value == -1:
            polinomial1 += '-x**'
        if value > 1:
            polinomial1 += '+' + str(value) + '*x'
    if key == 0:
        if value < 0:
            polinomial1 += str(value)
        if value > 0:
            polinomial1 += '+' + str(value)
i = 1
temp_list = list(polinomial1)     # превращаем строку в список для изменения
# добавляем пробелы в список
while i < len(temp_list):
    if temp_list[i] == '+' or temp_list[i] == '-':
        temp_list.insert(i + 1, ' ')
        temp_list.insert(i, ' ')
        i += 3
    else:
        i += 1
polinom1 = ''.join(temp_list)     # превращаем список обратно в строку для вывода
print(f'Первый многочлен:\n{polinom1}')

# То же самое для второго многочлена

pow2 = int(input('Введите показатель степени второго многочлена: '))

dict2 = {}     # Создаем словарь
i = pow2
while i >= 0:
    dict2[i] = randint(-10, 10)
    i -= 1
i = pow2
polinomial2 = ''
# превращаем словарь в строку и форматируем
for key, value in dict2.items():
    if key > 1:
        if value < -1:
            polinomial2 += str(value) + '*x**' + str(key)
        if value == 1:
            polinomial2 += '+x**' + str(key)
        if value == -1:
            polinomial2 += '-x**' + str(key)
        if value > 1:
            polinomial2 += '+' + str(value) + '*x**' + str(key)
    if key == 1:
        if value < -1:
            polinomial2 += str(value) + '*x'
        if value == 1:
            polinomial2 += '+x**'
        if value == -1:
            polinomial2 += '-x**'
        if value > 1:
            polinomial2 += '+' + str(value) + '*x'
    if key == 0:
        if value < 0:
            polinomial2 += str(value)
        if value > 0:
            polinomial2 += '+' + str(value)
i = 1
temp_list = list(polinomial2)     # превращаем строку в список для изменения
# добавляем пробелы в список
while i < len(temp_list):
    if temp_list[i] == '+' or temp_list[i] == '-':
        temp_list.insert(i + 1, ' ')
        temp_list.insert(i, ' ')
        i += 3
    else:
        i += 1
polinom2 = ''.join(temp_list)     # превращаем список обратно в строку для вывода
print(f'Второй многочлен:\n{polinom2}')

dict3 = {}     # Создаем третий словарь
# Складываем значения словарей по одинаковым ключам
if pow1 > pow2:
    i = pow1
    while i > pow2:
        dict3[i] = dict1[i]
        i -= 1
    while i >= 0:
        dict3[i] = dict1[i] + dict2[i]
        i -= 1
else:
    i = pow2
    while i > pow1:
        dict3[i] = dict2[i]
        i -= 1
    while i >= 0:
        dict3[i] = dict1[i] + dict2[i]
        i -= 1

polinomial3 = ''
# превращаем словарь в строку и форматируем
for key, value in dict3.items():
    if key > 1:
        if value < -1:
            polinomial3 += str(value) + '*x**' + str(key)
        if value == 1:
            polinomial3 += '+x**' + str(key)
        if value == -1:
            polinomial3 += '-x**' + str(key)
        if value > 1:
            polinomial3 += '+' + str(value) + '*x**' + str(key)
    if key == 1:
        if value < -1:
            polinomial3 += str(value) + '*x'
        if value == 1:
            polinomial3 += '+x**'
        if value == -1:
            polinomial3 += '-x**'
        if value > 1:
            polinomial3 += '+' + str(value) + '*x'
    if key == 0:
        if value < 0:
            polinomial3 += str(value)
        if value > 0:
            polinomial3 += '+' + str(value)
i = 1
temp_list = list(polinomial3)     # превращаем строку в список для изменения
# добавляем пробелы в список
while i < len(temp_list):
    if temp_list[i] == '+' or temp_list[i] == '-':
        temp_list.insert(i + 1, ' ')
        temp_list.insert(i, ' ')
        i += 3
    else:
        i += 1
polinom3 = ''.join(temp_list)     # превращаем список обратно в строку для вывода

print(dict1)
print(dict2)
print(dict3)
print(f'Сумма многочленов:\n{polinom3}')









