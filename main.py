import json
import os
import datetime

# Путь к файлу для сохранения заметок
file_path = "notes.json"

# Проверка наличия файла и создание, если его нет
if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        json.dump([], file)

def load_notes():
    with open(file_path, "r") as file:
        return json.load(file)

def save_notes(notes):
    with open(file_path, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    notes = load_notes()
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена.")

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"{note['id']}. {note['title']} ({note['timestamp']})")
        print(note['body'])
        print()

def edit_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note['title'] = title
            note['body'] = body
            note['timestamp'] = timestamp
            save_notes(notes)
            print("Заметка отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена.")
            return
    print("Заметка с указанным ID не найдена.")

while True:
    print("Выберите действие:")
    print("1. Добавить заметку")
    print("2. Список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Введите номер действия: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        list_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")