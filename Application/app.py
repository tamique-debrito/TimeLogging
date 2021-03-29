import tkinter as tk


class App(tk.Tk):
    def __init__(self, view):
        tk.Tk.__init__(self)
        self.view = view
        self.current_frame = None
        self.display_frame(Home)

    def activity_in_progress(self):
        """
        Returns boolean value indicating whether an activity is currently in progress
        """
        return self.view.activity_in_progress()

    def handle_start_activity(self):
        self.view.handle_start_activity()

    def handle_end_activity(self):
        self.view.handle_end_activity()

    def handle_switch_to_note_entry(self):
        self.view.handle_switch_to_note_entry()

    def handle_switch_to_tag_entry(self):
        self.view.handle_switch_to_tag_entry()

    def handle_submit(self):
        self.view.handle_submit()

    def refresh_home(self):  # redisplays the home frame. This is for when an activity is started, so that the button switches
        self.show_home_frame()

    def show_home_frame(self):
        self.display_frame(Home)

    def show_activity_entry_frame(self):
        self.display_frame(ActivityEntry)

    def show_note_entry_frame(self):
        self.display_frame(NoteEntry)

    def show_tag_entry_frame(self):
        self.display_frame(TagEntry)

    def get_activity_data(self):
        assert type(
            self.current_frame) is ActivityEntry, "Tried to get activity data when currect frame is not ActivityEntry. " \
                                                  f"Current frame is {type(self.current_frame)}"
        return self.get_data()

    def get_note_data(self):
        assert type(self.current_frame) is NoteEntry, "Tried to get note data when currect frame is not NoteEntry. " \
                                                      f"Current frame is {type(self.current_frame)}"
        return self.get_data()

    def get_tag_data(self):
        assert type(self.current_frame) is TagEntry, "Tried to get tag data when currect frame is not TagEntry. " \
                                                     f"Current frame is {type(self.current_frame)}"
        return self.get_data()

    def get_data(self):
        return self.current_frame.get_data()

    def display_frame(self, frame_class):
        """
        Switches current frame to 'frame_class'
        """
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()

    def update_timer_display(self, display_text):
        assert type(self.current_frame) == Home, "Tried to update timer display when current frame is not Home. " \
                                                 f"(current frame is {type(self.current_frame)})"
        self.current_frame.update_timer_display(display_text)


class Home(tk.Frame):
    def __init__(self, master: App):
        tk.Frame.__init__(self, master)
        timer_label = tk.Label(self, text="00:00:00")
        if not master.activity_in_progress():
            start_or_end_activity = tk.Button(self, text="Start activity",
                                              command=lambda: master.handle_start_activity())
        else:
            start_or_end_activity = tk.Button(self, text="End activity",
                                              command=lambda: master.handle_end_activity())

        add_note = tk.Button(self, text="Add note",
                             command=lambda: master.handle_switch_to_note_entry())

        add_tag = tk.Button(self, text="Add tag",
                            command=lambda: master.handle_switch_to_tag_entry())

        self.timer_label = timer_label
        self.start_or_end_activity = start_or_end_activity
        self.add_note = add_note
        self.add_tag = add_tag

        self.timer_label.pack()
        self.start_or_end_activity.pack()
        self.add_note.pack()
        self.add_tag.pack()

    def update_timer_display(self, display_text):
        self.timer_label.config(text=display_text)


class ActivityOrNoteEntry(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        title_label = tk.Label(self, text="Title")
        title = tk.Entry(self)
        tags_label = tk.Label(self, text="Tags")
        tags = tk.Entry(self)
        details_label = tk.Label(self, text="Details")
        details = tk.Text(self)
        submit = tk.Button(self, text="Submit",
                           command=lambda: master.handle_submit())

        self.title_label = title_label
        self.title = title
        self.tags_label = tags_label
        self.tags = tags
        self.details_labels = details_label
        self.details = details
        self.submit = submit

        self.title_label.pack()
        self.title.pack()
        self.tags_label.pack()
        self.tags.pack()
        self.details_labels.pack()
        self.details.pack()
        self.submit.pack()

    def get_data(self):
        return {
            'title': self.title.get(),
            'tags': self.tags.get(),
            'details': self.details.get("1.0", tk.END)
        }


class ActivityEntry(ActivityOrNoteEntry):
    pass


class NoteEntry(ActivityOrNoteEntry):
    pass


class TagEntry(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        name_label = tk.Label(self, text="Tag Name")
        name = tk.Entry(self)
        definition_label = tk.Label(self, text="Definition")
        definition = tk.Text(self)
        submit = tk.Button(self, text="Submit",
                           command=lambda: master.handle_submit())

        self.name_label = name_label
        self.name = name
        self.definition_label = definition_label
        self.definition = definition
        self.submit = submit

        self.name_label.pack()
        self.name.pack()
        self.definition_label.pack()
        self.definition.pack()
        self.submit.pack()

    def get_data(self):
        return {
            'name': self.name.get(),
            'definition': self.definition.get("1.0", tk.END)
        }
