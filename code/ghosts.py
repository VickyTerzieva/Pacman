from PyQt4 import QtGui, QtCore
from code.pair import Pair
from code.breadth_first_search import breadth_first_search


class Ghosts(QtGui.QGraphicsPixmapItem):

    def __init__(self, name):
        super(Ghosts, self).__init__()

        self.set_image(name)

    def chase(self, goal):
        pos = Pair(self.x(), self.y())
        path = breadth_first_search(pos, goal)
        while not path.empty():
            aim = path.get_nowait()
            self.move_towards(aim)

    def set_image(self, name):
        self.setPixmap(QtGui.QPixmap(name))

    def return_home(self):
        goal = Pair(222, 214)
        self.chase(goal)

    def move_towards(self, goal):
        print("in")
        self.setPos(goal.first(), goal.second())