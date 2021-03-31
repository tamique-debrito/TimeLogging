from Activity.ActivityDatabase import ActivityDatabase
from Note.NoteDatabase import NoteDatabase
from Tag.TagDatabase import TagDatabase


class Model:
    def __init__(self):
        self.activity_db = ActivityDatabase()
        self.note_db = NoteDatabase()
        self.tag_db = TagDatabase()

    def add_activity(self, activity):
        self.activity_db.add_activity(activity)

    def add_note(self, note):
        self.note_db.add_note(note)

    def add_tag(self, name, definition):
        self.tag_db.add_tag(name, definition)

    def add_metatag(self, metatag):
        self.tag_db.add_metatag(metatag)

    def save(self):
        self.activity_db.save()
        self.note_db.save()
        self.tag_db.save()

    def expand_metatag(self, metatag_name):
        return self.tag_db.expand_metatag(metatag_name)
