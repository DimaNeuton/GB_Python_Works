def open_file():
    with open('phones.txt', 'r', encoding = 'utf-8') as data:
        temp = data.readlines()
        print('Файл открыт\n')
        return temp

class PhoneBook:
    def __init__(self, temp_pb):    # конструктор для создания объекта
        self.temp_pb = []
    def save_file(self):
        with open('phones.txt', 'w', encoding = 'utf-8') as data:
            data.write(''.join(self.temp_pb))
            print('Контакты сохранены\n')
    def show_contacts(self):
        if self.temp_pb == []: print('Файл не открыт\n')
        else: print(''.join(self.temp_pb))
    def add_contact(self):
        if self.temp_pb == []: print('Файл не открыт\n')
        else: self.temp_pb.append(input('Введите новый контакт в формате "Имя_Фамилия телефон (цифры через дефис)'
                                        ' комментарий": ') + '\n')
    def change_contact(self):
        print('Выберите контакт для изменения: ')
        changed_contact = self.find_contact()
        if changed_contact != 0:
            print('Какую информацию вы хотите изменить?\n'
                  '0. Имя абонента\n'
                  '1. Номер телефона\n'
                  '2. Комментарий\n')
            num = int(input('Введите цифру: '))
            for index, contact in enumerate(changed_contact):
                if contact == changed_contact:
                    changed_contact = changed_contact.split()
                    changed_contact[num] = input('Введите новые данные: ')
                    self.temp_pb[index] = ' '.join(changed_contact) + '\n'
    def find_contact(self):
        cantact_name = input('Введите имя контакта: ')
        for contact in self.temp_pb:
            if cantact_name in contact:
                print(contact)
                return contact
        else:
            print('Нет такого контакта\n')
            return 0
    def del_contact(self):
        print('Выберите контакт для удаления: ')
        deleted_contact = self.find_contact()
        for contact in self.temp_pb:
            if contact == deleted_contact:
                self.temp_pb.remove(contact)
        print(f'Контакт {deleted_contact[:-1]} удален\n')