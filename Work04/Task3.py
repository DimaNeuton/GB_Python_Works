# Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных
#          0123456 789 10 11 12 13 14 15 16 17
# string ='aaaaaaa|sss s  s |d  d  d  d |a  a'
# aaaaaaasssssddddaa
# new_str = '7a5s4d2a'

text = input('Введите текст: ')
text += ' '
i = 0
count = 1
code = ''
while i < len(text) - 1:
    if text[i] == text[i + 1]:
        count += 1
    else:
        code += str(count) + text[i]
        count = 1
    i += 1
print('Сжимаем данные:')
print(code)

temp_code1 = ''
for item in code:
    if not item.isdigit():
        temp_code1 += ' ' + item + ' '
    else:
        temp_code1 += item
temp_code1 = temp_code1.split()
i = 1
temp_code2 = []
while i < len(temp_code1):
    temp_code2 += int(temp_code1[i - 1]) * list(temp_code1[i])
    i += 2
text = ''.join(temp_code2)
print('Восстанавливаем данные:')
print(text)




