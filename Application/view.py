import time
import tkinter as tk

from Application.app import App
from Application.presenter import Presenter


TIME_FORMAT = '%H:%M:%S'
UPDATE_TIME_MSEC = 500


class View:
    def __init__(self):
        self.presenter = Presenter(self)
        self.app = App(view=self)
        self.auto_update_timer_display()
        self.app.protocol("WM_DELETE_WINDOW", self.handle_quit)
        self.app.mainloop()

    def activity_in_progress(self):
        return self.presenter.activity_in_progress()

    def auto_update_timer_display(self):
        if self.presenter.activity_in_progress():
            self.presenter.update_timer_display()
            self.app.after(UPDATE_TIME_MSEC, self.auto_update_timer_display)

    def handle_start_activity(self):
        self.presenter.handle_start_activity()

    def handle_end_activity(self):
        self.presenter.handle_end_activity()

    def handle_switch_to_note_entry(self):
        self.presenter.handle_switch_to_note_entry()

    def handle_switch_to_tag_entry(self):
        self.presenter.handle_switch_to_tag_entry()

    def handle_submit(self):
        self.presenter.handle_submit()

    def handle_quit(self):
        self.presenter.handle_quit()

    def quit(self):
        self.app.destroy()

    def get_activity_data(self):
        return self.app.get_activity_data()

    def get_note_data(self):
        return self.app.get_note_data()

    def get_tag_data(self):
        return self.app.get_tag_data()

    def get_data(self):
        return self.app.get_data()

    ######### Display functions

    def show_home(self):
        self.app.show_home_frame()

    def show_activity_entry(self):
        self.app.show_activity_entry_frame()

    def show_note_entry(self):
        self.app.show_note_entry_frame()

    def show_tag_entry(self):
        self.app.show_tag_entry_frame()

    def refresh_home(self):
        self.app.refresh_home()
