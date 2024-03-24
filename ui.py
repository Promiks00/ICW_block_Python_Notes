from logger import input_data, print_data, change_data, remove, print_note


def interface():
    print(
        "Добрый день! Вы запустили приложение 'Заметки'. В программе используются следующие команды:"
        "\n 1 - создание заметки \n 2 - вывод всех заметок \n 3 - вывод заметки (по номеру ID) 4 - изменение заметки" 
        "\n 5 - удаление заметки")
    command = input("Введите число: ")

    while command != "1" and command != "2" and command != "3" and command != "4" and command != "5":
        print("Неправильный ввод")
        command = input("Введите число: ")

    if command == "1":
        input_data()
    elif command == "2":
        print_data()
    elif command == "3":
        print_note()
    elif command == "4":
        change_data()
    elif command == "5":
        remove()
