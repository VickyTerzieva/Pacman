from PyQt4 import QtGui, QtCore


class Ghosts(QtGui.QGraphicsPixmapItem):

    def __init__(self, name):
        super(Ghosts, self).__init__()

        self.setPixmap(QtGui.QPixmap(name))

    def chase(self, pacman):
        pass
