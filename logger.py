import datetime
from data_create import header_data, body_data, id_data


def input_data():
    note_id = id_data()
    header = header_data()
    body = body_data()
    now = datetime.datetime.now()


    with open('notes.csv', 'a', encoding='utf-8') as f:
        f.write(f"{note_id};{header};{body};{now}\n")

    print("Заметка успешно сохранена")
