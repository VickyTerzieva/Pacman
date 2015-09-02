class Pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_second(self, x):
        self.x = x

    def set_first(self, y):
        self.y = y

    def first(self):
        return int(self.x)

    def second(self):
        return int(self.y)
