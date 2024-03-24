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
