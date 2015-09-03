from PyQt4 import QtGui, QtCore
from code.pair import Pair
from code.breadth_first_search import breadth_first_search
import functools


class Ghosts(QtGui.QGraphicsPixmapItem):

    def __init__(self, name):
        super(Ghosts, self).__init__()

        self.set_image(name)
        self.name = name
        self.going_home = False

    def chase(self, goal):
        pos = Pair(self.x(), self.y())
        path = breadth_first_search(pos, goal)

        func = functools.partial(self.move_towards, path)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(func)
        self.timer.start(700)

    def set_image(self, name):
        self.setPixmap(QtGui.QPixmap(name))

    def return_home(self):
        self.going_home = True
        goal = Pair(226, 174)
        self.chase(goal)
        self.set_image(self.name)

    def move_towards(self, path):
        if path.empty():
            return
        goal = path.get_nowait()
        self.setPos(goal.first(), goal.second())

    def get_out_of_home(self):
        goal = Pair(222, 214)
        self.chase(goal)
        self.setPos(226, 174)
        self.going_home = False