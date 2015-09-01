from PyQt4 import QtGui


class PacDot(QtGui.QGraphicsPixmapItem):
    def __init__(self, name):
        super(PacDot, self).__init__()

        self.setPixmap(QtGui.QPixmap(name))


class BigPacDots(QtGui.QGraphicsPixmapItem):
    def __init__(self, name):
        super(BigPacDots, self).__init__()

        self.setPixmap(QtGui.QPixmap(name))


def create_dots():
    dots = []

    for x in range(30, 446, 16):
        for y in range(20, 148, 16):
            dot = PacDot("./resources/images/pac_dot.png")
            dot.setPos(x, y)
            if removable_dot(dot) is False:
                dots.append(dot)

    for x in range(30, 446, 16):
        for y in range(325, 485, 16):
            dot = PacDot("./resources/images/pac_dot.png")
            dot.setPos(x, y)
            if removable_dot(dot) is False:
                dots.append(dot)

    for y in range(148, 309, 16):
        dot = PacDot("./resources/images/pac_dot.png")
        dot2 = PacDot("./resources/images/pac_dot.png")
        dot.setPos(110, y)
        dot2.setPos(350, y)
        if removable_dot(dot) is False:
            dots.extend([dot, dot2])

    for x in [23, 424]:
        for y in [46, 367]:
            dot = BigPacDots("./resources/images/big_pac_dot.png")
            dot.setPos(x, y)
            dots.append(dot)

    return dots


def removable_dot(dot):
    removable_dots = []

    dot1 = [430, 52]
    dot2 = [430, 373]
    dot3 = [222, 373]
    dot4 = [238, 373]
    dot5 = [30, 52]
    dot6 = [30, 373]

    removable_dots.extend([dot1, dot2, dot3, dot4, dot5, dot6])

    for i in range(removable_dots.__len__()):
        if dot.x() == removable_dots[i][0] and dot.y() == removable_dots[i][1]:
            return True

    return False
