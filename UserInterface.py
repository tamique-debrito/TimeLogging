import tkinter as tk
from datetime import datetime as dt


def string_format_timedelta(delta):
    seconds = delta.seconds % 60
    minutes = (delta.seconds // 60) % 60
    hours = delta.seconds // (60 * 60)
    return f'{hours:0>2}:{minutes:0>2}:{seconds:0>2}'


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()
        self.clock_start = None

    def update_clock(self):
        now = self.get_deltatime_string()
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

    def get_deltatime_string(self):
        delta = dt.now() - self.clock_start