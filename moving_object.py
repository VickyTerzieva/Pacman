import maze


class MovingObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, labyrinth):
        if self.x < labyrinth.size - 1 and \
        labyrinth.hindrance[self.x][self.y] is False:
            self.x += 1

    def move_down(self, labyrinth):
        if self.x > 0 and labyrinth.hindrance[self.x][self.y] is False:
            self.x -= 1

    def move_left(self, labyrinth):
        if self.y > 0 and labyrinth.hindrance[self.x][self.y] is False:
            self.y -= 1

    def move_right(self, labyrinth):
        if self.y < labyrinth.size - 1 and \
        labyrinth.hindrance[self.x][self.y] is False:
            self.y += 1

