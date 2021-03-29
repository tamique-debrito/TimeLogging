import os
import pickle

SAVE_PATH = '../data/tag_db'

class TagDBEntry:
    """
    An entry in the tag database
    Fields:
        tag: the tag object
        definition: a definition of the tag's meaning
    """

    def __init__(self, tag, definition=None):
        self.tag = tag
        self.definition = definition

    def has_definition(self):
        return self.definition is not None

    def set_definition(self, definition):
        self.definition = definition

    def __str__(self):
        s = f'Tag Entry:\n\tTag: {self.tag}\n\tDef: {self.definition}'
        return s

    def __eq__(self, other):
        return self.tag == other.tag and self.definition == other.definition

class TagDatabase:
    """
    This class records tags that have been used, as well as a definition of those tags
    Field:
        tags: a dictionary mapping Tag objects to their corresponding TagDBEntry objects

    Methods:
        __init__(): loads data from the save-path if there is such data, otherwise initializes to an empty database
        add_tag(tag, definition=None): adds a tag to the database
        has_tag(tag): checks if tag is in database
        has_definition(tag): checks if tag has a definition
        load(): loads from save-path
        save(): saves to the save-path
    """

    def __init__(self, skip_load=False):
        self.db = dict()
        if os.path.exists(SAVE_PATH) and not skip_load:
            self.load()

    def add_tag(self, tag, definition=None):
        self.db[tag] = TagDBEntry(tag, definition)

    def has_definition(self, tag):
        return self.db[tag].has_definition()

    def num_undefined(self):
        return sum([1 if not self.has_definition(tag) else 0 for tag in self.db])

    def load(self):
        with open(SAVE_PATH, 'rb') as db:
            self.db = pickle.load(db)

    def save(self):
        with open(SAVE_PATH, 'wb') as db:
            pickle.dump(self.db, db, pickle.HIGHEST_PROTOCOL)

    def __str__(self):
        s = f'Tag database with {len(self.db)} tags'
        return s

    def __len__(self):
        return len(self.db)

    def __getitem__(self, tag):
        return self.db[tag]

def test_db():
    global SAVE_PATH
    SAVE_PATH = '../data/tag_db_test'
    from Tag import Tag
    tags = [Tag('#firsttag'), Tag('#andanother'), Tag('#hello')]

    print("Testing basic database operations...", end='')

    database = TagDatabase(skip_load=True)
    assert database.__str__() == 'Database with 0 tags', 'Database string is incorrect'
    assert database.num_undefined() == 0, "Database not counting number of undefined correctly"
    database.add_tag(tags[0])
    database.add_tag(tags[1], 'just another tag')
    assert database.__str__() == 'Database with 2 tags', 'Database string is incorrect'
    database.add_tag(tags[2], 'i just want to say hi')
    assert database[tags[2]] == TagDBEntry(tags[2], 'i just want to say hi'), 'Database setting values incorrectly'
    assert database.num_undefined() == 1, "Database not counting number of undefined correctly"
    print('passed')

    print("Testing Loading and saving...", end='')

    database.save()

    new_database = TagDatabase()

    assert new_database[tags[2]] == database[tags[2]], "Database did not load correctly"
    assert new_database.__str__() == 'Database with 3 tags', "Database did not load correctly"
    assert new_database.num_undefined() == 1, "Database did not load correctly"
    print('passed')


if __name__ == "__main__":
    test_db()
