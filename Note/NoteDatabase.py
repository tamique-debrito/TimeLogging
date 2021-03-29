import os
import pickle

SAVE_PATH = '../data/note_db'

class NoteDatabase:
    """
    A simple database for recorded notes
    Assumes that notes are added in chronological order
    """

    def __init__(self, skip_load=False):
        self.db = []
        if os.path.exists(SAVE_PATH) and not skip_load:
            self.load()

    def add_note(self, note):
        self.db.append(note)


    def load(self):
        with open(SAVE_PATH, 'rb') as db:
            self.db = pickle.load(db)

    def save(self):
        with open(SAVE_PATH, 'wb') as db:
            pickle.dump(self.db, db, pickle.HIGHEST_PROTOCOL)

    def __str__(self):
        s = f'Note database with {len(self)} entries'
        return s

    def __len__(self):
        return len(self.db)

    def __getitem__(self, index):
        return self.db[index]

if __name__ == "__main__":
    pass
