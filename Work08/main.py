# открыть файл
# сохранить файл
# показать контакты
# добавить контакт
# изменить контакт
# найти контакт
# удалить контакт
# выход

import module
temp_file = []
temp_file1 = module.open_file()
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
    data = int(input('Введите номер действия: '))
    return data

while True:
    user_choice = print_menu()
    match user_choice:
        case 1:
            temp_file = module.open_file()
        case 2:
            module.save_file(temp_file)
        case 3:
            module.show_contacts(temp_file)
        case 4:
            module.add_contact(temp_file)
        case 5:
            module.change_contact(temp_file)
        case 6:
            module.find_contact(temp_file)
        case 7:
            module.del_contact(temp_file)
        case 8:
            if temp_file != temp_file1:
                choice = int(input('Если вы уверены, что хотите выйти без сохранения, нажмите 1: '))
                if choice == 1:
                    print('Выход\n')
                    break
        case _:
            print('Введена некорректная команда\n')




