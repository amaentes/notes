import json
from Note import Note

class NotesRepository:
    def __init__(self, filename):
        self.filename = filename

    def save_notes(self, notes):
        with open(self.filename, "w") as f:
            json.dump([note.__dict__ for note in notes], f)

    def load_notes(self):
        try:
            with open(self.filename, "r") as f:
                notes_data = json.load(f)
                return [Note(**data) for data in notes_data]
        except FileNotFoundError:
            return []
