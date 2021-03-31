import re
from Tag.Tag import Tag

class MetaTag:
    """
    This class represents a metatag, which is a single tag that represents a set of other tags
    Definition:
        a metatagstring is a string consisting of two hashtags '##' followed by non-whitespace alphanumeric characters
    the argument passed into the __init__ function should be a valid tagstring
    parse_tags_from_string returns a set of tag objects from a string containing zero or more valid tagstrings
    """
    @staticmethod
    def extract_name(name):  # Extracts a lower-cased tag name from a tagstring, e.g. '#CoolDay' -> 'coolday'
        return name.replace('#', '').lower()
    @staticmethod
    def parse_metatag_names_from_string(text):
        names = re.findall('##([a-z1-9_-]+)', text)
        return names

    def __init__(self, name, subtags):
        self.name = MetaTag.extract_name(name)
        self.subtags = Tag.parse_tags_from_string(subtags)

    def expand(self):
        return self.subtags

    def __str__(self):
        return '#' + self.name

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return self.name == other.name
