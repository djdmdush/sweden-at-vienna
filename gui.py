
import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel


class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()

        QSound.play("terranova.wav")

        self.setGeometry(50, 50, 1080, 1350)
        self.setWindowTitle("Sweden at the Gates of Vienna: Main Menu")
        self.setWindowIcon(QIcon("kustaa.png"))

        self.play_game = Play()

        self.label = QLabel(self)
        background_1 = QPixmap("mainmenu.jpg")
        background_1 = background_1.scaledToHeight(1350)
        self.label.setPixmap(background_1)
        self.label.setGeometry(0, 0, 1080, 1350)

        btn_play = QPushButton("Play", self)
        #btn_play.clicked.connect(self.btn_play_clicked)
        btn_play.resize(340, 80)
        btn_play.move(380, 550)

        btn_quit = QPushButton("Quit", self)
        btn_quit.clicked.connect(self.close_game)
        btn_quit.resize(340, 50)
        btn_quit.move(380, 800)

        self.show()

    def play_game_clicked(self):
        self.play_game.show()

    def close_game(self):
        choice = QMessageBox.question(self, 'Message',
                                     "Are you sure you want to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Exited the game")
            sys.exit()
        else:
            pass

class Play(QMainWindow):
    def __init__(self):
        super(Play, self).__init__()

        self.setGeometry(100, 50, 1000, 600)
        self.setWindowTitle("Sweden at the Gates of Vienna: Game")
        self.setWindowIcon(QIcon("kustaa.png"))


if __name__ == "__main__":

    def run():
        app = QApplication(sys.argv)
        Gui = MainMenu()
        sys.exit(app.exec_())

run()