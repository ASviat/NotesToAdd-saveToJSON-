import json
import datetime

# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.

# При чтении списка заметок реализовать фильтрацию по дате.

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.datetime.now().isoformat()


class NoteApp:
    def __init__(self):
        self.notes = []

    def create(self, title, body):
        id = len(self.notes) + 1
        note = Note(id, title, body)
        self.notes.append(note)

    def update(self, id, title, body):
        for note in self.notes:
            if note.id == id:
                note.update(title, body)

    def delete(self, id):
        self.notes = [note for note in self.notes if note.id != id]

    def view(self):
        for note in self.notes:
            print(
                f'ID: {note.id}\nTitle: {note.title}\nBody: {note.body}\nCreated at: {note.created_at}\nUpdated at: {note.updated_at}\n')

    def save(self):
        with open('myNotes.json', 'w') as f:
            json.dump([note.__dict__ for note in self.notes], f)

    def load(self):
        try:
            with open('myNotes.json', 'r') as f:
                data = json.load(f)
                self.notes = [Note(note['id'], note['title'],
                                   note['body']) for note in data]
        except FileNotFoundError:
            pass


app = NoteApp()
app.load()

while True:
    action = input('Select action:\nPress:\n1 to create\n2 to update\n3 to delete\n4 to view\n5 to exit\n')
    if action == '1':
        title = input('Enter title: ')
        body = input('Enter your text: ')
        app.create(title, body)
    elif action == '2':
        id = int(input('Enter ID of the note you want to edit: '))
        title = input('Enter new title: ')
        body = input('Enter new doby of the note: ')
        app.update(id, title, body)
    elif action == '3':
        id = int(input('Enter ID of the note you want to delete: '))
        app.delete(id)
    elif action == '4':
        app.view()
    elif action == '5':
        break

app.save()
