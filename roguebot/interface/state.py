from collections import deque


class FrameHistory():
    def __init__(self, buffer_size=10):
        """
        Stores frames in a deque buffer.
        self.buffer[0] stores the most recent,
        [1] is the next most recent, and so on.
        :param buffer_size: how many frames back to save.
        """
        self.buffer_size = buffer_size
        self.buffer = deque()
        for i in range(buffer_size):
            self.buffer.appendleft('')

    def add(self, frame):
        self.buffer.appendleft(frame)
        self.buffer.pop()

    def diff(self, n0, n1):
        # finds what changed between two frames
        # Might be useful to track items that have been picked up, or when the player
        # goes onto stairs, or a monster dies / vanishes...?
        pass

    def __getitem__(self, n):
        return self.buffer[n]


class StatsHistory():

    FIELDS = [
        'hp'
        'hp_max'
        'level'
        'depth'
        'strength'
        'strength_max'
        'gold'
        'exp'
        'exp_next'
        'armor'
    ]

    def __init__(self, buffer_size=10):
        self.buffer_size = buffer_size
        self.buffer = deque()
        for i in range(buffer_size):
            self.buffer.appendleft()

    def add(self, stat):
        self.buffer.appendleft(stat)
        self.buffer.pop()

    def __getitem__(self, n):
        return self.buffer[n]
