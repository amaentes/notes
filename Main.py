from NotesManager import NotesManager
from NotesRepository import NotesRepository

if __name__ == "__main__":
    repository = NotesRepository("notes.json")
    manager = NotesManager(repository)
    while True:
        command = input("Введите команду (add, read, edit, delete) или exit для выхода: ")
        if command == "add":
            manager.add()
        elif command == "read":
            notes = manager.read()
            for note in notes:
                print(f"{note.title} - {note.msg} ({note.date})")
        elif command == "edit":
            manager.edit()
        elif command == "delete":
            manager.delete()
        elif command == "exit":
            break
        else:
            print("Неверная команда")