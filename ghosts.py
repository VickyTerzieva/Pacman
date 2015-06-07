from moving_object import MovingObject
import maze
import pacman


class Ghosts(MovingObject):

    def random_move(self):
        pass

    def chase(self, pacman):
        if pacman.x < self.x:
            self.move_down()
        elif pacman.x > self.x:
            self.move_up()
        else:
            self.random_move()