import maze
from moving_object import MovingObject


class Pacman(MovingObject):
    EMPTY = None
    PAC_DOT_POINTS = 10
    GHOST_POINTS = 100
    FRUIT_POINTS = 100

    def __init__(self, x, y):
        MovingObject.__init__(self, x, y)
        self.pac_dots = 0
        self.level = 1
        self.score = 0
        self.fruit = 0

    def level_up(self, labyrinth):
        if self.pac_dots == labyrinth.pac_dots:
            self.level += 1
            self.pac_dots = 0

    def increase_points(self):
        pass
