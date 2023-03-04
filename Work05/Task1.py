# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии

number_A = int(input('Введите A: '))
number_B = int(input('Введите B: '))

def pow(A: int, B: int) -> int:
    if B == 0:
        return 1
    return pow(A, B - 1) * A
print(f'{number_A} в степени {number_B} равно {pow(number_A, number_B)}')