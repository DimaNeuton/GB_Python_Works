def open_file():
    with open('phones.txt', 'r', encoding = 'utf-8') as data:
        temp_file = data.readlines()
        print('Файл открыт\n')
        return temp_file
def save_file(temp_file):
    with open('phones.txt', 'w', encoding = 'utf-8') as data:
        data.write(''.join(temp_file))
        print('Контакты сохранены')
def show_contacts(temp_file):
    if temp_file == []: print('Файл не открыт\n')
    else: print(''.join(temp_file))
def add_contact(temp_file):
    if temp_file == []: print('Файл не открыт\n')
    else: temp_file.append(input('Введите новый контакт: ') + '\n')
def change_contact(temp_file):
    print('Выберите контакт для изменения: ')
    changed_contact = find_contact(temp_file)
    if changed_contact != 0:
        print('Какую информацию вы хотите изменить?\n'
              '1. Имя абонента\n'
              '2. Номер телефона\n'
              '3. Комментарий\n')
        num = int(input('Введите цифру: '))
        for index, contact in enumerate(temp_file):
            if contact == changed_contact:
                changed_contact = changed_contact.split()
                changed_contact[num] = input('Введите новые данные: ')
                temp_file[index] = ' '.join(changed_contact) + '\n'
def find_contact(temp_file):
    cantact_name = input('Введите имя контакта: ')
    for contact in temp_file:
        if cantact_name in contact:
            print(contact)
            return contact
    else:
        print('Нет такого контакта\n')
        return 0
def del_contact(temp_file):
    print('Выберите контакт для удаления: ')
    deleted_contact = find_contact(temp_file)
    for contact in temp_file:
        if contact == deleted_contact:
            temp_file.remove(contact)
    print(f'Контакт {deleted_contact[:-1]} удален\n')