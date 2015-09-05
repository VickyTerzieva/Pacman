from PyQt4 import QtGui, QtCore
from code.pair import Pair
from code.breadth_first_search import breadth_first_search
import functools


class Ghosts(QtGui.QGraphicsPixmapItem):

    def __init__(self, name, in_home, x, y, time):
        super(Ghosts, self).__init__()

        self.set_image(name)
        self.name = name
        self.going_home = False
        self.setPos(x, y)
        self.eaten = False
        self.in_home = in_home
        self.initial_x = x
        self.initial_y = y
        self.time = time
        self.timer = QtCore.QTimer()
        self.timer.singleShot(self.time, self.set_free)

    def chase(self, goal):
        pos = Pair(self.x(), self.y())
        path = breadth_first_search(pos, goal)

        func = functools.partial(self.move_towards, path)

        self.timer.timeout.connect(func)
        self.timer.start(200)

    def set_image(self, name):
        self.setPixmap(QtGui.QPixmap(name))

    def return_home(self):
        self.going_home = True
        goal = Pair(226, 174)
        self.chase(goal)

    def move_towards(self, path):
        if path.empty():
            if self.going_home is True:
                self.setPos(222, 214)
                QtCore.QTimer.singleShot(100, self.get_out_of_home)
                return
            else:
                return
        goal = path.get_nowait()
        self.setPos(goal.first(), goal.second())

    def get_out_of_home(self):
        self.eaten = False
        self.setPos(222, 214)
        QtCore.QTimer.singleShot(150, self.go_out)

    def set_free(self):
        if self.in_home is True:
            self.get_out_of_home()

    def go_out(self):
        self.setPos(226, 174)
        self.going_home = False
        self.set_image(self.name)