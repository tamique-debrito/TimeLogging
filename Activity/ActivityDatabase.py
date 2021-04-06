import os
import pickle

SAVE_PATH = 'C:/Users/tamiq/PycharmProjects/TimeLogging/data/activity_db'

class ActivityDatabase:
    """
    A simple database for recorded activities
    Assumes that activities are added in chronological order
    """

    def __init__(self, postfix='', skip_load=False):
        self.db = []
        if os.path.exists(SAVE_PATH) and not skip_load:
            self.load(postfix)

    def add_activity(self, activity):
        self.db.append(activity)


    def load(self, postfix=''):
        with open(SAVE_PATH + postfix, 'rb') as db:
            self.db = pickle.load(db)

    def save(self, postfix=''):
        with open(SAVE_PATH + postfix, 'wb') as db:
            pickle.dump(self.db, db, pickle.HIGHEST_PROTOCOL)

    def __str__(self):
        s = f'Activity database with {len(self)} entries'
        return s

    def __len__(self):
        return len(self.db)

    def __getitem__(self, index):
        return self.db[index]

if __name__ == "__main__":
    pass
