from PyQt4 import QtGui, QtCore


class Walls(QtGui.QGraphicsPixmapItem):
    def __init__(self, name):
        super(Walls, self).__init__()
        self.setPixmap(QtGui.QPixmap(name))


# think about obtimization if there is enough time
def create_walls():
    obstacles = []

    wall1 = Walls("./resources/images/obstacle1.png")
    wall1.setPos(175, 102)

    wall2 = Walls("./resources/images/obstacle1.png")
    wall2.setPos(175, 295)

    wall3 = Walls("./resources/images/obstacle1.png")
    wall3.setPos(175, 391)

    wall4 = Walls("./resources/images/obstacle2.png")
    wall4.setPos(267, 100)

    wall5 = Walls("./resources/images/obstacle2.png")
    wall5.rotate(180)
    wall5.setPos(202, 221)

    wall6 = Walls("./resources/images/obstacle3.png")
    wall6.setPos(45, 388)

    wall7 = Walls("./resources/images/obstacle4.png")
    wall7.setPos(265, 384)

    wall8 = Walls("./resources/images/obstacle5.png")
    wall8.setPos(361, 338)

    wall9 = Walls("./resources/images/obstacle6.png")
    wall9.setPos(45, 336)

    wall10 = Walls("./resources/images/obstacle7.png")
    wall10.setPos(272, 343)

    wall11 = Walls("./resources/images/obstacle7.png")
    wall11.setPos(128, 343)

    wall12 = Walls("./resources/images/obstacle8.png")
    wall12.setPos(128, 38)

    wall13 = Walls("./resources/images/obstacle8.png")
    wall13.setPos(272, 38)

    wall14 = Walls("./resources/images/obstacle9.png")
    wall14.setPos(368, 102)

    wall15 = Walls("./resources/images/obstacle9.png")
    wall15.setPos(48, 102)

    wall16 = Walls("./resources/images/obstacle10.png")
    wall16.setPos(48, 38)

    wall17 = Walls("./resources/images/obstacle10.png")
    wall17.setPos(368, 38)

    wall18 = Walls("./resources/images/obstacle11.png")
    wall18.setPos(0, 0)

    wall19 = Walls("./resources/images/obstacle12.png")
    wall19.setPos(0, 245)

    obstacles.extend([wall1, wall2, wall3, wall4, wall5, wall6, wall7,
                      wall8, wall9, wall10, wall11, wall12, wall13,
                      wall14, wall15, wall16, wall17, wall18, wall19])
    return obstacles


def taken():
    matrix = [[False for x in range(470)] for y in range(500)]

    for x in range(155, 293):
        for y in range(178, 268):
            matrix[x][y] = True

    for x in range(28, 100):
        for y in range(19, 75):
            matrix[x][y] = True

    for x in range(108, 197):
        for y in range(19, 75):
            matrix[x][y] = True

    for x in range(205, 245):
        for y in range(12, 75):
            matrix[x][y] = True

    for x in range(251, 340):
        for y in range(19, 75):
            matrix[x][y] = True

    for x in range(348, 420):
        for y in range(19, 75):
            matrix[x][y] = True

    for x in range(28, 100):
        for y in range(83, 124):
            matrix[x][y] = True

    for x in range(107, 148):
        for y in range(83, 220):
            matrix[x][y] = True

    for x in range(130, 197):
        for y in range(130, 171):
            matrix[x][y] = True

    for x in range(155, 292):
        for y in range(83, 124):
            matrix[x][y] = True

    for x in range(204, 245):
        for y in range(104, 172):
            matrix[x][y] = True

    for x in range(299, 341):
        for y in range(83, 220):
            matrix[x][y] = True

    for x in range(251, 318):
        for y in range(130, 173):
            matrix[x][y] = True

    for x in range(348, 420):
        for y in range(83, 124):
            matrix[x][y] = True

    for x in range(22, 100):
        for y in range(127, 220):
            matrix[x][y] = True

    for x in range(424, 369):
        for y in range(127, 220):
            matrix[x][y] = True

    for x in range(22, 100):
        for y in range(226, 318):
            matrix[x][y] = True

    for x in range(356, 446):
        for y in range(227, 318):
            matrix[x][y] = True

    for x in range(107, 149):
        for y in range(227, 316):
            matrix[x][y] = True

    for x in range(299, 341):
        for y in range(227, 316):
            matrix[x][y] = True

    for x in range(156, 292):
        for y in range(274, 316):
            matrix[x][y] = True

    for x in range(203, 244):
        for y in range(295, 363):
            matrix[x][y] = True

    for x in range(28, 101):
        for y in range(323, 364):
            matrix[x][y] = True

    for x in range(59, 100):
        for y in range(344, 412):
            matrix[x][y] = True

    for x in range(108, 196):
        for y in range(323, 363):
            matrix[x][y] = True

    for x in range(252, 340):
        for y in range(323, 363):
            matrix[x][y] = True

    for x in range(348, 420):
        for y in range(323, 363):
            matrix[x][y] = True

    for x in range(349, 390):
        for y in range(345, 412):
            matrix[x][y] = True

    for x in range(21, 51):
        for y in range(368, 412):
            matrix[x][y] = True

    for x in range(157, 292):
        for y in range(371, 411):
            matrix[x][y] = True

    for x in range(205, 244):
        for y in range(392, 459):
            matrix[x][y] = True

    for x in range(107, 149):
        for y in range(372, 437):
            matrix[x][y] = True

    for x in range(28, 196):
        for y in range(418, 458):
            matrix[x][y] = True

    for x in range(253, 420):
        for y in range(418, 460):
            matrix[x][y] = True

    for x in range(299, 343):
        for y in range(372, 437):
            matrix[x][y] = True

    for x in range(348, 460):
        for y in range(132, 220):
            matrix[x][y] = True

    for x in range(397, 446):
        for y in range(371, 412):
            matrix[x][y] = True

    return matrix

taken_by_walls = taken()
