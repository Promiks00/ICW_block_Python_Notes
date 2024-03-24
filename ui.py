from logger import input_data, print_data


def interface():
    print(
        "Добрый день! Вы запустили приложение 'Заметки'. В программе используются следующие команды:"
        "\n 1 - создание заметки \n 2 - вывод заметки \n 3 - изменение заметки \n 4 - удаление заметки")
    command = input("Введите число: ")

    while command != "1" and command != "2":
        print("Неправильный ввод")
        command = input("Введите число: ")

    if command == "1":
        input_data()
    elif command == "2":
        print_data()
