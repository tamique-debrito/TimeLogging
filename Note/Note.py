from datetime import datetime as dt

DEFAULT_TITLE_LEN = 15

class Note:
    """
    Documents a note that was taken at a specified point in time.
    Fields:
        log_time: the time note was taken
        title: a title for the activity (defaults to the first few characters of details)
        tags: a set of tags that the activity is related to
        details: a more detailed description of the activity
    """
    def __init__(self, title, tags, details, log_time):
        self.title = title
        self.tags = tags
        self.details = details
        self.log_time = log_time

    def __str__(self):
        return f'Note:\n\t{self.title}\n\t{[str(tag) for tag in self.tags]}\n\t{self.details}\n\tRecorded {self.log_time}'