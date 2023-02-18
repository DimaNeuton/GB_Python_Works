# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input('Введите число N: '))
pow = 1
result = 1
print(f'Степени двойки, не превосходящие {number}:')
while result <= number:
    print(result)
    result = 2**pow
    pow += 1


