import sys
import functools
from code.ghosts import Ghosts
from PyQt4 import QtGui, QtCore
from code.walls import taken_by_walls
from code.direction import Direction
from code.pac_dots import *
from code.text import Text
from code.walls import *


PAC_DOT_POINTS = 10
BIG_PAC_DOT_POINTS = 50
GHOST_POINTS = 100
STEP = 12
ALL_PAC_DOTS = 262
filename = "./file.txt"


class Pacman(QtGui.QGraphicsPixmapItem):
    def __init__(self, x, y, scene):
        super(Pacman, self).__init__()

        self.pac_dots = 0
        self.level = 1
        self.score = 0
        self.lives = 3
        self.big_pac_dot_eaten = False
        self.direction = None
        self.ghosts_eaten = 0
        self.moving = 0
        self.initial_x = x
        self.initial_y = y
        self.name = "./resources/images/pacman_left.png"
        self.scene = QtGui.QGraphicsScene()
        self.scene = scene

        self.current_lives = Text("Lives: "+str(self.lives))
        self.current_lives.upgrade(QtCore.Qt.red,
                                   QtGui.QFont("times", 18), 350, 500)

        self.current_score = Text("Score: "+str(self.score))
        self.current_score.upgrade(QtCore.Qt.blue,
                                   QtGui.QFont("helvetica", 18), 0, 500)

        self.setPixmap(QtGui.QPixmap(self.name))
        self.setPos(x, y)

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

        if front_.__len__() > 0 and (front_[0] < 21 or front_[0] > 430) \
                and 220 < front_[1] < 246:
            self.teleport()

        if self.front_blocked(front_) is True:
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
        else:
            return []

    @staticmethod
    def front_blocked(front):
        if front.__len__() == 0:
            return
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
                self.ghosts_eaten += 1
                if colliding_items[i].eaten is False:
                    self.increase_points(GHOST_POINTS * self.ghosts_eaten)
                colliding_items[i].eaten = True
            elif type(colliding_items[i]) is Ghosts:
                self.lives -= 1
                self.current_lives.show_on_screen("Lives: " + str(self.lives))
                if self.lives == 0:
                    self.game_over()
                else:
                    self.game_continue()
            elif type(colliding_items[i]) is PacDot:
                QtGui.QSound.play("./resources/sounds/eating.wav")
                self.pac_dots += 1
                self.increase_points(PAC_DOT_POINTS)
                self.scene.removeItem(colliding_items[i])
                if self.pac_dots == ALL_PAC_DOTS:
                    self.level_up()
                    return
            elif type(colliding_items[i]) is BigPacDots:
                QtGui.QSound.play("./resources/sounds/eating.wav")
                self.pac_dots += 1
                self.increase_points(BIG_PAC_DOT_POINTS)
                self.scene.removeItem(colliding_items[i])
                if self.pac_dots == ALL_PAC_DOTS:
                    self.level_up()
                    return
                self.big_pac_dot_eaten = True
                QtCore.QTimer.singleShot(7000, self.uneaten)
                self.change_ghosts("./resources/images/ghost.png")

    def increase_points(self, points):
        self.score += points
        self.current_score.show_on_screen("Score: " + str(self.score))

    def level_up(self):
        self.level += 1
        self.pac_dots = 0
        self.new_level()

    def game_over(self):
        dialog = QtGui.QInputDialog()
        name, ok = dialog.getText(dialog, "GAME OVER", "Input your name:")
        if ok is True:
            file = open(filename, 'a')
            file.write("{0} {1}\n".format(name, str(self.score)))
            file.close()
        sys.exit()

    def new_level(self):
        objects = list(self.scene.items())
        for object_ in objects:
            if not type(object_) == Text and not type(object_) == Walls:
                self.scene.removeItem(object_)
        func = functools.partial(self.show_everything, objects)
        QtCore.QTimer.singleShot(1000, func)

    def game_continue(self):
        objects = list(self.scene.items())
        for object_ in objects:
            if type(object_) is Ghosts or type(object_) is Pacman:
                self.scene.removeItem(object_)
        func = functools.partial(self.show_again, objects)
        QtCore.QTimer.singleShot(1000, func)

    def show_again(self, objects):
        for object_ in objects:
            if type(object_) is Ghosts:
                object_.setPos(object_.initial_x, object_.initial_y)
                self.scene.addItem(object_)
                object_.set_image(object_.name)
                if object_.in_home_copy is True:
                    object_.get_out_of_home()
            if type(object_) is Pacman:
                object_.setPos(object_.initial_x, object_.initial_y)
                self.scene.addItem(object_)
                self.setPixmap(QtGui.QPixmap(self.name))
                self.setFocus()

    def show_again_dots(self):
        dots = create_dots()
        for i in range(dots.__len__()):
            self.scene.addItem(dots[i])

    def show_everything(self, objects):
        self.show_again_dots()
        self.show_again(objects)

    def uneaten(self):
        self.ghosts_eaten = 0
        self.big_pac_dot_eaten = False
        self.ghosts_return()

    def set_focus(self):
        self.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)
        self.setFocus()

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
        ghosts = list(self.scene.items())
        for i in range(ghosts.__len__()):
            if type(ghosts[i]) is Ghosts:
                ghosts[i].set_image(name)
                ghosts[i].eaten = False

    def ghosts_return(self):
        ghosts = list(self.scene.items())
        for i in range(ghosts.__len__()):
            if type(ghosts[i]) is Ghosts and ghosts[i].going_home is False:
                ghosts[i].set_image(ghosts[i].name)

    def create_pacman_dying(self):
        pics = []
        name = "./resources/images/pacman_dying1.png"
        pic1 = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(name))
        pic1.setPos(self.x(), self.y())
        name = "./resources/images/pacman_dying2.png"
        pic2 = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(name))
        pic2.setPos(self.x(), self.y())
        name = "./resources/images/pacman_dying3.png"
        pic3 = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(name))
        pic3.setPos(self.x(), self.y())
        name = "./resources/images/pacman_dying4.png"
        pic4= QtGui.QGraphicsPixmapItem(QtGui.QPixmap(name))
        pic4.setPos(self.x(), self.y())
        name = "./resources/images/pacman_dying5.png"
        pic5 = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(name))
        pic5.setPos(self.x(), self.y())
        name = "./resources/images/pacman_dying6.png"
        pic6 = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(name))
        pic6.setPos(self.x(), self.y())
        name = "./resources/images/pacman_dying7.png"
        pic7 = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(name))
        pic7.setPos(self.x(), self.y())
        name = "./resources/images/pacman_dying8.png"
        pic8 = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(name))
        pic8.setPos(self.x(), self.y())
        name = "./resources/images/pacman_dying9.png"
        pic9 = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(name))
        pic9.setPos(self.x(), self.y())
        name = "./resources/images/pacman_dying10.png"
        pic10 = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(name))
        pic10.setPos(self.x(), self.y())
        pics.extend([pic1, pic2, pic3, pic4, pic5,
                     pic6, pic7, pic8, pic9, pic10])
        return pics