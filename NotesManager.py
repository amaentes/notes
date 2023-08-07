import datetime
from Note import Note
from NotesRepository import NotesRepository

class NotesManager:
    def __init__(self, repository):
        self.repository = repository
        self.notes = self.repository.load_notes()

    def add(self):
        title = input("Введите заголовок заметки: ")
        msg = input("Введите тело заметки: ")
        note = Note(len(self.notes) + 1, title, msg, str(datetime.datetime.now()))
        self.notes.append(note)
        self.repository.save_notes(self.notes)
        print("Заметка успешно сохранена")

    def read(self):
        date = input("Введите дату (в формате ГГГГ-ММ-ДД) для фильтрации или оставьте пустым для вывода всех заметок: ")
        if date == "":
            return self.notes
        else:
            filtered_notes = [note for note in self.notes if note.date[:10] == date]
            return filtered_notes

    def edit(self):
        title = input("Введите заголовок заметки для редактирования: ")
        msg = input("Введите новое тело заметки: ")
        for note in self.notes:
            if note.title == title:
                note.msg = msg
                note.date = str(datetime.datetime.now())
                break
        self.repository.save_notes(self.notes)
        print("Заметка успешно отредактирована")

    def delete(self):
        title = input("Введите заголовок заметки для удаления: ")
        self.notes = [note for note in self.notes if note.title != title]
        self.repository.save_notes(self.notes)
        print("Заметка успешно удалена")

