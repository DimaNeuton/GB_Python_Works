# Крестики-нолики

def print_xo(dict_xo):
    print(f'1 | 2 | 3     {dict_xo[1]} | {dict_xo[2]} | {dict_xo[3]}\n'
          f'---------     ---------\n'
          f'4 | 5 | 6     {dict_xo[4]} | {dict_xo[5]} | {dict_xo[6]}\n'
          f'---------     ---------\n'
          f'7 | 8 | 9     {dict_xo[7]} | {dict_xo[8]} | {dict_xo[9]}')

# 1. Если компьютер начинает первым
dict_xo = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: 'x', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
print(dict_xo.values())
list_dict_xo = [{1: dict_xo[1], 2: dict_xo[2], 3: dict_xo[3]}, {1: dict_xo[1], 4: dict_xo[4], 7: dict_xo[7]},
                {1: dict_xo[1], 5: dict_xo[5], 9: dict_xo[9]}, {2: dict_xo[2], 5: dict_xo[5], 8: dict_xo[8]},
                {4: dict_xo[4], 5: dict_xo[5], 6: dict_xo[6]}, {3: dict_xo[3], 6: dict_xo[6], 9: dict_xo[9]},
                {7: dict_xo[7], 8: dict_xo[8], 9: dict_xo[9]}, {3: dict_xo[3], 5: dict_xo[5], 7: dict_xo[7]}]
# list_dict_xo = [[dict_xo[1], dict_xo[2], dict_xo[3]], [dict_xo[1], dict_xo[4], dict_xo[7]],
#                 [dict_xo[1], dict_xo[5], dict_xo[9]], [dict_xo[2], dict_xo[5], dict_xo[8]],
#                 [dict_xo[4], dict_xo[5], dict_xo[6]], [dict_xo[3], dict_xo[6], dict_xo[9]],
#                 [dict_xo[7], dict_xo[8], dict_xo[9]], [dict_xo[3], dict_xo[5], dict_xo[7]]]
print_xo(dict_xo)
user_move = int(input('Ваш ход:\nВведите номер ячейки, в которую нужно поставить 0, руководствуясь схемой слева:'))
dict_xo[user_move] = 'o'
print_xo(dict_xo)

for dict in list_dict_xo:
    if (dict.values().count('x') == 2 or dict.values().count('o') == 2) and dict.values().count(' ') == 0:
        for k,v in dict.items():
            if v == ' ':
                dict_xo[k] = 'x'
    elif



