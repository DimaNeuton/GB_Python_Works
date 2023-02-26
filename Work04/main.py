# Напишите программу, которая принимает на вход строку и отслеживает
# сколько раз каждый символ уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# string = 'w e f g j u g d x v g h k i y g'
# list1 = 'w e f g j u g d x v g h k i y g'.split()
# dict1 = {}
# list2 = []
# for letter in list1:
#     dict1[letter] = dict1.get(letter, 0) + 1
#     if dict1.get(letter) > 1:
#         list2.append(letter + '_' + str(dict1.get(letter)))
#     else:
#         list2.append(letter)
# print(' '.join(list2))

# Пользователь вводит текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите сколько различных слов содержится в этом тексте.

# text = 'dfdfsd sdfsdfds hnghg ihmyu     sdcern yukhgb hnghg ihmyu'
# text_list = text.split()
# temp = set(text_list)
# print(len(temp))

# Дана последовательность чисел. Получить список уникальных элементов.

# list1 = [1, 2, 3, 5, 1, 5, 3, 10]
# dict1 = {}
# list2 = []
# for item in list1:
#     dict1[item] = dict1.get(item, 0) + 1
# for item in dict1:
#     if dict1[item] == 1:
#         list2.append(item)
# print(list2)

# list1 = [1, 2, 3, 5, 1, 5, 3, 10]
# list2 = []
# for item in list1:
#     if list1.count(item) == 1:
#         list2.append(item)
# print(list2)