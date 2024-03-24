import datetime
from data_create import header_data, body_data, id_data, current_datetime


def input_data():
    note_id = id_data()
    header = header_data()
    body = body_data()
    now = current_datetime()

    with open('notes.csv', 'a', encoding='utf-8') as f:
        f.write(f"ID заметки: {note_id}; Заголовок: {header}; Текст: {body}; Дата/время создания(изменения): {now}\n")

    print("Заметка успешно сохранена")


def print_data():
    with open('notes.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        print(*data, sep='')

def change_data():
    k = int(input("Введите номер записи, который Вы хотите изменить: "))
    input_data()           # Вызываем функцию input_data(), которая добавляет запись в конец файла
    with open('notes.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        change_line = data.pop()
        data_list = data[:k-1] + change_line + data[k:1]
    with open('notes.csv', 'w', encoding='utf-8') as f:
        f.writelines(data_list)

