import time


class Timer():
    def __init__(self):
        self.start = time.time()

    def set(self, value):
        self.start = time.time() - value

    def reset(self):
        self.set(0)

    def get(self):
        return time.time() - self.start


timer = Timer()
