# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2
# *
from random import randint

number = int(input('Введите количество монеток на столе: '))
i = 1
count_0 = 0
count_1 = 0
while i <= number:
    coin_side = randint(0, 1)
    print(coin_side)
    if coin_side == 0: count_0 += 1
    else: count_1 +=1
    i += 1
if count_1 >= count_0: print(f'Нужно перевернуь минимум {count_0} монет')
else: print(f'Нужно перевернуь минимум {count_1} монет(у,ы)')