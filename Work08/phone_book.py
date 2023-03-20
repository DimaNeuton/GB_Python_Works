import module_pb_class as pb    #импортируем модуль
from module_pb_class import PhoneBook


# функция для вывода меню в консоль
def print_menu():
    print('Это телефонный справочник. Выберите действие: \n'
          '1. Открыть файл\n'
          '2. Сохранить файл\n'
          '3. Показать контакты\n'
          '4. Добавить контакт\n'
          '5. Изменить контакт\n'
          '6. Найти контакт\n'
          '7. Удалить контакт\n'
          '8. Выход\n')
    menu_choice = int(input('Введите номер действия: '))
    return menu_choice

temp_pb1 = pb.open_file()   #сохраняем в переменную данные до изменения

# бесконечнй цикл для повторения вывода меню после каждого действия
while True:
    user_choice = print_menu()
    match user_choice:
        case 1:
            temp_pb = pb.open_file()    #временный список из контактов, с которым будем работать
            phone_book = PhoneBook(temp_pb)     #объект класса PhoneBook
        case 2:
            phone_book.save_file()
        case 3:
            phone_book.show_contacts()
        case 4:
            phone_book.add_contact()
        case 5:
            phone_book.change_contact()
        case 6:
            phone_book.find_contact()
        case 7:
            phone_book.del_contact()
        case 8:
            if temp_pb1 != phone_book.temp_pb:
                choice = int(input('Если вы уверены, что хотите выйти без сохранения, нажмите 1: '))
                if choice == 1:
                    print('Выход\n')
                    break
        case _:
            print('Введена некорректная команда\n')




