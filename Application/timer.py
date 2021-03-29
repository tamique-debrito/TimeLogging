from datetime import datetime as dt

from enum import Enum


class TimerState(Enum):
    IDLE = 1
    RUNNING = 2


class Timer:

    def __init__(self):
        self.state = TimerState.IDLE
        self.end_time = None

    def reset(self):
        self.state = TimerState.IDLE
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = dt.now()
        self.state = TimerState.RUNNING
        self.end_time = None

    def stop(self):
        self.end_time = dt.now()
        self.state = TimerState.IDLE

    def running(self):
        return self.state == TimerState.RUNNING

    def complete(self):
        """
        Indicates whether timer currently represents a completed time period (i.e. start() then stop())
        """
        return self.start_time is not None and self.end_time is not None

    def get_endpoints(self):
        assert self.complete(), "Tried to get endpoints when timer not finished recording"
        return self.start_time, self.end_time

    def now(self):
        return dt.now()

    def get_current_display_text(self):
        if self.state == TimerState.RUNNING:
            delta = dt.now() - self.start_time
            seconds = delta.seconds % 60
            minutes = (delta.seconds // 60) % 60
            hours = delta.seconds // (60 * 60)
            return f'{hours:0>2}:{minutes:0>2}:{seconds:0>2}'
        else:
            return '00:00:00'
