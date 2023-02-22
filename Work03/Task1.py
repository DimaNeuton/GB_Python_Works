
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
from random import randint

list_len = int(input('Введите длину списка: '))
number = int(input('Введите искомое число: '))
list1 = []
for _ in range(list_len):
    list1.append(randint(1, 100))
print(list1)
print("Упорядочим список для простой проверки")
print(sorted(list1))
count = 0
max_near_left = 0
max_near_right = 100
for item in list1:
    if item == number: count += 1
    else:
        if item < number and item >= max_near_left:
            max_near_left = item
        if item > number and item <= max_near_right:
            max_near_right = item
if count != 0:
    print(f'Число {number} встречается в списке {count} раз')
else:
    print(f'Максимально близкое число слева от {number} - {max_near_left}')
    print(f'Максимально близкое число справа от {number} - {max_near_right}')

