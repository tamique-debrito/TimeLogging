import os
import pickle
from datetime import datetime as dt
from datetime import timedelta as td

SAVE_PATH = 'C:/Users/tamiq/PycharmProjects/TimeLogging/data/backup_tracking'

BACKUP_PERIOD = 7  # number of days before new backup will be made

class BackupTracker:
    """
    Used by the model class to ensure that a backup gets saved every week (assuming the application gets opened)
    """

    def __init__(self, databases_to_backup):
        # 'databases_to_backup' is a list of objects representing the databases to track
        # each must have a 'save(postfix)' method which saves a copy of the database with the given 'postfix'
        self.last_backup_time = None
        self.current_time = dt.now()
        self.saved_this_time = False
        self.databases_to_backup = databases_to_backup
        self.load()

    def load(self):
        # Loads datetime object representing the time of last backup if any
        if os.path.exists(SAVE_PATH):
            with open(SAVE_PATH, 'rb') as f:
                last_save = pickle.load(f)
            self.last_backup_time = last_save
        else:
            self.last_backup_time = None

    def backup_needed(self):
        # Determines whether a backup is currently needed to stay on schedule.
        # Return True if needed, otherwise False
        if self.last_backup_time is None:
            return True
        days_since_last_backup = (self.current_time - self.last_backup_time).days
        return days_since_last_backup >= BACKUP_PERIOD

    def save(self):
        # Saves a backup of each database
        if self.backup_needed():
            with open(SAVE_PATH, 'wb') as f:
                pickle.dump(self.current_time, f, pickle.HIGHEST_PROTOCOL)

            backups_postfix = '_backup' + self.current_time.strftime("%d-%m-%Y")
            for db in self.databases_to_backup:
                db.save(postfix=backups_postfix)
