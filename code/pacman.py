import sys
from code.ghosts import Ghosts
from PyQt4 import QtGui, QtCore
from code.walls import taken_by_walls
from code.direction import Direction
from code.pac_dots import *
from code.text import Text
from code.pair import Pair

PAC_DOT_POINTS = 10
BIG_PAC_DOT_POINTS = 50
GHOST_POINTS = 100
STEP = 12
ALL_PAC_DOTS = 262
filename = "./file.txt"


class Pacman(QtGui.QGraphicsPixmapItem):
    def __init__(self):
        super(Pacman, self).__init__()

        self.pac_dots = 0
        self.level = 1
        self.score = 0
        self.lives = 3
        self.big_pac_dot_eaten = False
        self.direction = None
        self.ghosts_eaten = 0
        self.moving = 0

        self.current_lives = Text("Lives: "+str(self.lives))
        self.current_lives.upgrade(QtCore.Qt.red,
                                   QtGui.QFont("times", 18), 350, 500)

        self.current_score = Text("Score: "+str(self.score))
        self.current_score.upgrade(QtCore.Qt.blue,
                                   QtGui.QFont("helvetica", 18), 0, 500)

        self.setPixmap(QtGui.QPixmap("./resources/images/pacman_left.png"))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.direction = Direction.UP
        elif event.key() == QtCore.Qt.Key_Down:
            self.direction = Direction.DOWN
        elif event.key() == QtCore.Qt.Key_Left:
            self.direction = Direction.LEFT
        elif event.key() == QtCore.Qt.Key_Right:
            self.direction = Direction.RIGHT
        else:
            self.direction = None

        self.move()

    def move(self):
        front_ = self.front()

        if (front_[0] < 21 or front_[0] > 430) \
                and 220 < front_[1] < 246:
            self.teleport()

        if self.front_blocked(self, front_) is True:
            return

        if self.direction == Direction.UP:
            self.move_up()
        elif self.direction == Direction.DOWN:
            self.move_down()
        elif self.direction == Direction.LEFT:
            self.move_left()
        elif self.direction == Direction.RIGHT:
            self.move_right()

        self.moving += 1
        self.set_image()
        self.collisions()

    def move_up(self):
        self.setPos(self.x(), self.y() - STEP)

    def move_down(self):
        self.setPos(self.x(), self.y() + STEP)

    def move_left(self):
        self.setPos(self.x() - STEP, self.y())

    def move_right(self):
        self.setPos(self.x() + STEP, self.y())

    def front(self):
        if self.direction == Direction.UP:
            return [self.x(), self.y() - STEP]
        elif self.direction == Direction.DOWN:
            return [self.x(), self.y() + STEP]
        elif self.direction == Direction.LEFT:
            return [self.x() - STEP, self.y()]
        elif self.direction == Direction.RIGHT:
            return [self.x() + STEP, self.y()]

    @staticmethod
    def front_blocked(self, front):
        if front[0] < 21 or front[0] > 430 or front[1] < 13 or front[1] > 465:
            return True
        return taken_by_walls[int(front[0])][int(front[1])]

    def collisions(self):
        colliding_items = list(self.collidingItems())
        for i in range(colliding_items.__len__()):
            if type(colliding_items[i]) is Ghosts \
                    and self.big_pac_dot_eaten is True:
                colliding_items[i].set_image("./resources/images/eyes.png")
                colliding_items[i].return_home()
                goal = Pair(self.x(), self.y())
                colliding_items[i].chase(goal)
            elif type(colliding_items[i]) is Ghosts:
                self.lives -= 1
                if self.lives == 0:
                    self.game_over()
                else:
                    self.game_continue()
            elif type(colliding_items[i]) is PacDot:
                self.pac_dots += 1
                self.increase_points(PAC_DOT_POINTS)
                self.scene().removeItem(colliding_items[i])
            elif type(colliding_items[i]) is BigPacDots:
                self.pac_dots += 1
                self.big_pac_dot_eaten = True
                self.increase_points(BIG_PAC_DOT_POINTS)
                self.scene().removeItem(colliding_items[i])
                QtCore.QTimer.singleShot(7000, self.uneaten)
                self.change_ghosts("./resources/images/ghost.png")

    def increase_points(self, points):
        self.score += points
        self.current_score.show_on_screen("Score: " + str(self.score))

    def level_up(self):
        if self.pac_dots == ALL_PAC_DOTS:
            self.level += 1
            self.pac_dots = 0
            self.game_continue()

    def game_over(self):
        dialog = QtGui.QInputDialog()
        name, ok = dialog.getText(dialog, "GAME OVER", "Input your name:")
        file = open(filename, 'a')
        file.write("{0} {1}\n".format(name, str(self.score)))
        file.close()
        #if ok is True:
        sys.exit()

    def game_continue(self):
        pass

    def uneaten(self):
        self.big_pac_dot_eaten = False
        self.ghosts_return()

    def set_focus(self):
        self.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)
        super(Pacman, self).setFocus()

    def set_image(self):
        if self.moving % 2 == 1:
            self.setPixmap(QtGui.QPixmap("./resources/images/pac.png"))
        elif self.direction == Direction.UP:
            self.setPixmap(QtGui.QPixmap("./resources/images/pacman_up.png"))
        elif self.direction == Direction.DOWN:
            self.setPixmap(QtGui.QPixmap("./resources/images/pacman_down.png"))
        elif self.direction == Direction.LEFT:
            self.setPixmap(QtGui.QPixmap("./resources/images/pacman_left.png"))
        elif self.direction == Direction.RIGHT:
            name = "./resources/images/pacman_right.png"
            self.setPixmap(QtGui.QPixmap(name))

    def teleport(self):
        if self.x() < -20:
            self.setPos(466, self.y())
        elif self.x() > 476:
            self.setPos(-10, self.y())
        elif self.direction == Direction.LEFT:
            self.setPos(self.x() - STEP, self.y())
        elif self.direction == Direction.RIGHT:
            self.setPos(self.x() + STEP, self.y())
        self.moving += 1
        self.set_image()
        self.collisions()

    def change_ghosts(self, name):
        ghosts = list(self.scene().items())
        for i in range(ghosts.__len__()):
            if type(ghosts[i]) is Ghosts:
                ghosts[i].set_image(name)

    def ghosts_return(self):
        ghosts = list(self.scene().items())
        for i in range(ghosts.__len__()):
            if type(ghosts[i]) is Ghosts and ghosts[i].going_home is False:
                ghosts[i].set_image(ghosts[i].name)