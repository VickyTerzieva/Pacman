import sys
from PyQt4 import QtGui, QtCore
from code.pacman import Pacman
from code.pacman import filename
from code.walls import *
from code.pac_dots import *
from code.ghosts import Ghosts
from code.pair import Pair
import functools


class GameWindow(QtGui.QMainWindow):
    def __init__(self):
        super(GameWindow, self).__init__()

        self.setGeometry(448, 129, 470, 530)
        self.setWindowTitle("Pacman")
        self.setWindowIcon(QtGui.QIcon("./resources/images/pacman_right.png"))
        self.main_menu()

    def start(self):
        scene = QtGui.QGraphicsScene()
        scene.setSceneRect(0, 0, 470, 530)

        view = QtGui.QGraphicsView(scene)
        view.setFixedSize(480, 540)
        view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        view.show()

        player = Pacman(view.width()/2-14, view.height()/2+96, scene)
        pinky = Ghosts("./resources/images/pink_down.png",
                       in_home=True, x=222, y=214, time=100)
        inky = Ghosts("./resources/images/blue_down.png",
                      in_home=True, x=254, y=214, time=5000)
        blinky = Ghosts("./resources/images/red_down.png",
                        in_home=False, x=178, y=174, time=0)
        clyde = Ghosts("./resources/images/orange_down.png",
                       in_home=True, x=192, y=214, time=10000)

        dots = create_dots()
        for i in range(dots.__len__()):
            scene.addItem(dots[i])

        obstacles = create_walls()
        for i in range(obstacles.__len__()):
            scene.addItem(obstacles[i])

        self.set_scene(scene, blinky, pinky, inky, clyde,
                       player, player.current_score, player.current_lives)

        self.setCentralWidget(view)
        # QtGui.QSound.play("./resources/sounds/opening music.wav")
        # !! 4000
        QtCore.QTimer.singleShot(0, player.set_focus)
        func = functools.partial(self.set_paths_to,
                                 player, blinky,
                                 pinky, inky, clyde)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(func)
        self.timer.start(500)

    def main_menu(self):
        btn = QtGui.QPushButton("Play", self)
        btn.clicked.connect(self.start)
        btn.resize(150, 50)
        btn.move(self.width()/2-btn.width()/2, self.height()/2-btn.height())

        btn2 = QtGui.QPushButton("HighScores", self)
        btn2.clicked.connect(self.high_scores)
        btn2.resize(150, 50)
        btn2.move(self.width()/2-btn2.width()/2, self.height()/2)

        btn3 = QtGui.QPushButton("Quit", self)
        btn3.clicked.connect(self.close_program)
        btn3.resize(150, 50)
        btn3.move(self.width()/2-btn3.width()/2, self.height()/2+btn3.height())
        self.show()

    def high_scores(self):
        file = open(filename)
        scores = file.read()
        self.view_text()
        self.textView.setText(scores)
        self.show()

    def view_text(self):
        self.textView = QtGui.QTextBrowser()
        self.setCentralWidget(self.textView)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape \
           or event.key() == QtCore.Qt.Key_Q:
            self.close_program()

    def close_program(self):
        option = QtGui.QMessageBox.question(self, 'Close',
                                            "Do you really want to quit?",
                                            QtGui.QMessageBox.Yes |
                                            QtGui.QMessageBox.No)
        if option == QtGui.QMessageBox.Yes:
            sys.exit()

    def closeEvent(self, event):
        option = QtGui.QMessageBox.question(self, 'Close',
                                            "Do you really want to quit?",
                                            QtGui.QMessageBox.Yes |
                                            QtGui.QMessageBox.No)
        if option == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @staticmethod
    def set_paths_to(player, *args):
        goal = Pair(player.pos().x(), player.pos().y())
        for ghost in args:
            if ghost.going_home is False:
                ghost.chase(goal)

    @staticmethod
    def set_scene(scene, *args):
        name = QtGui.QBrush(QtGui.QImage("./resources/images/background.png"))
        scene.setBackgroundBrush(name)
        for item in args:
            scene.addItem(item)

app = QtGui.QApplication(sys.argv)
game = GameWindow()
game.main_menu()
sys.exit(app.exec())
