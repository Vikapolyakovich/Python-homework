def write(text):
    with open("data.txt", "a", encoding="utf-8") as file:
        file.writelines(text)
        file.writelines("\n")
        print("Успешно")


def read_all():
    with open("data.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line)


def search_by_surname(surname):
    with open("data.txt", "r", encoding="utf-8") as file:
        for line in file:
            if surname in line:
                print(line)


def delete_info(surname):
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open("data.txt", "w", encoding="utf-8") as file:
        for line in lines:
            if surname not in line:
                file.write(line)
        print("Данные успешно удалены")


def change_info(old_name, new_name):
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open("data.txt", "w", encoding="utf-8") as file:
        for line in lines:
            if old_name in line:
                line = line.replace(old_name, new_name)
            file.write(line)
        print('Данные успешно изменены')


def choose(choice):
    if choice == '1':
        return write(input("Введите ваши данные пример:(фамилия имя отчество номер телефона)"))
    elif choice == "2":
        return read_all()
    elif choice == "3":
        return search_by_surname(input("Введите имя или фамилию"))
    elif choice == "4":
        return change_info(old_name = input('Введите старую информацию: '), new_name = input('Введите новую '
                                                                                             'информацию: '))

    elif choice == "5":
        return delete_info(input("Введите имя или фамилию"))
    elif choice == "-1":
        exit()
    else:
        return choose(input('Неверная команда. Введите 1, 2, 3, 4, 5 или -1: '))
