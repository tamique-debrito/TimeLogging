from Application.timer import Timer
from Application.model import Model
from Activity.Activity import Activity
from Note.Note import Note
from Tag.Tag import Tag

from enum import Enum


class WindowState(Enum):
    HOME = 1
    ACTIVITY_ENTRY = 2
    NOTE_ENTRY = 3
    TAG_ENTRY = 4

ENTRY_STATES = [WindowState.ACTIVITY_ENTRY, WindowState.NOTE_ENTRY, WindowState.TAG_ENTRY]


class Presenter:
    def __init__(self, view):
        self.view = view
        self.model = Model()
        self.timer = Timer()
        self.state = WindowState.HOME

    def handle_start_activity(self):
        self.timer.start()
        self.view.refresh_home()
        self.view.auto_update_timer_display()

    def handle_end_activity(self):
        self.timer.stop()
        self.switch_to_activity_entry()

    def handle_switch_to_note_entry(self):
        self.view.show_note_entry()
        self.state = WindowState.NOTE_ENTRY

    def handle_switch_to_tag_entry(self):
        self.view.show_tag_entry()
        self.state = WindowState.TAG_ENTRY

    def handle_submit(self):
        assert self.state in ENTRY_STATES, "Presenter tried to handle submit when not in an entry state" \
                                           f"In state {self.state}"

        if self.state == WindowState.ACTIVITY_ENTRY:
            self.package_and_send_activity_data()
        elif self.state == WindowState.NOTE_ENTRY:
            self.package_and_send_note_data()
        else:
            self.package_and_send_tag_data()

        self.switch_to_home()

    def handle_quit(self):
        self.model.save()
        self.view.quit()

    def activity_in_progress(self):
        return self.timer.running()

    def package_and_send_activity_data(self):
        activity_data = self.view.get_activity_data()

        start_time, end_time = self.timer.get_endpoints()
        title = activity_data['title']
        tags = Tag.parse_tags_from_string(activity_data['tags'])
        details = activity_data['details']

        activity = Activity(start_time=start_time, end_time=end_time, title=title, tags=tags, details=details)

        self.model.add_activity(activity)
        print(activity)

    def package_and_send_note_data(self):
        note_data = self.view.get_note_data()

        title = note_data['title']
        tags = Tag.parse_tags_from_string(note_data['tags'])
        details = note_data['details']
        log_time = self.timer.now()

        note = Note(title, tags, details, log_time)
        self.model.add_note(note)

    def package_and_send_tag_data(self):
        tag_data = self.view.get_tag_data()

        name = tag_data['name']
        definition = tag_data['definition']

        self.model.add_tag(name, definition)

    def update_timer_display(self):
        display_text = self.timer.get_current_display_text()
        self.view.app.update_timer_display(display_text)

    def switch_to_home(self):
        self.view.show_home()
        self.state = WindowState.HOME

    def switch_to_activity_entry(self):
        self.view.show_activity_entry()
        self.state = WindowState.ACTIVITY_ENTRY
