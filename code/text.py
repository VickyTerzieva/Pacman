from PyQt4 import QtGui, QtCore


class Text(QtGui.QGraphicsTextItem):
    def __init__(self, name):
        super(Text, self).__init__()

        self.setPlainText(name)

    def upgrade(self, color, font, x, y):
        self.setDefaultTextColor(color)
        self.setFont(font)
        self.moveBy(x, y)

    def show_on_screen(self, text):
        self.setPlainText(text)
