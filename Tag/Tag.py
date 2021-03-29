import re

class Tag:
    """
    This class represents a single tag, holding only the name
    Definition:
        a tagstring is a string consisting of a hashtag '#' followed by non-whitespace alphanumeric characters
    the argument passed into the __init__ function should be a valid tagstring
    parse_tags_from_string returns a set of tag objects from a string containing zero or more valid tagstrings
    """
    @staticmethod
    def extract_name(name):  # Extracts a lower-cased tag name from a tagstring, e.g. '#CoolDay' -> 'coolday'
        return name.replace('#', '').lower()
    @staticmethod
    def parse_tags_from_string(text):
        names = re.findall('#([a-z1-9]+)', text)
        return set([Tag(name) for name in names])

    def __init__(self, name):
        self.name = Tag.extract_name(name)

    def __str__(self):
        return '#' + self.name

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return self.name == other.name
