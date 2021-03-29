from datetime import datetime as dt

DEFAULT_TITLE_LEN = 15

class Activity:
    """
    Documents an activity that happened for a period of time.
    Fields:
        start_time: the start time of the activity as a datetime object
        end_time: the end time of the activity as a datetime object
        total_time: the length of the activity as a timedelta object
        title: a title for the activity (defaults to the first few characters of details)
        tags: a set of tags that the activity is related to
        details: a more detailed description of the activity

    Methods:
        begin_activity(): sets start time of activity to current time
        end_activity(): sets end time of activity to current time
        set_title(title): sets title
        add_tags(tags): adds the list of tags to the set of current tags
        set_details(details): sets details
        finish(): sets total time based off of start and end times and fills unfilled fields
                    must call begin_activity() and end_activity() before calling this
    """
    def __init__(self, title, tags, details, start_time, end_time):
        if len(title) == 0:
            title = details[:DEFAULT_TITLE_LEN]
        self.start_time = start_time
        self.end_time = end_time
        self.total_time =  end_time - start_time
        self.title = title
        self.tags = tags
        self.details = details

    def __str__(self):
        return f'Activity:\n\t{self.title}\n\t{[str(tag) for tag in self.tags]}\n\t{self.details}\n\t' \
               f'From {self.start_time} to {self.end_time} (total time {self.total_time})'

    # The following was written before I learned of the existence of the MVP pattern, and is
    # not relevant to current application setup

    def begin_activity(self):
        self.start_time = dt.now()

    def end_activity(self):
        self.end_time = dt.now()

    def add_tags(self, tags):
        self.tags.union(tags)

    def set_details(self, details):
        self.details = details

    def set_title(self, title):
        self.title = title

    def finish(self):
        assert self.start_time is not None and self.end_time is not None, 'Tried to finish activity without setting both start and end times. ' \
                                                                          f'Start time was {"not" if self.start_time is None else ""} set. ' \
                                                                          f'End time was {"not" if self.end_time is None else ""} set.'
        if self.details is None:
            self.details = ''
        if self.title is None:
            self.title = self.details[:DEFAULT_TITLE_LEN]

        self.total_time = self.start_time - self.end_time