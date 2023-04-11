import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class App(QApplication):
    class MainWidget(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint)
            self.setGeometry(300, 300, 300, 200)
            self.setMouseTracking(True)
            self.setWindowTitle('Teleport Button')

            self.lbl = QLabel('Close this program?', self)
            self.lbl.move(50, 50)
            font = QFont('Comic Sans MS', 14, 75)
            self.lbl.setFont(font)

            self.btn_yes = QPushButton('Yes', self)
            self.btn_yes.move(50, 100)
            self.btn_yes.clicked.connect(self.teleport)
            self.btn_yes.setCursor(Qt.PointingHandCursor)

            self.btn_no = QPushButton('No', self)
            self.btn_no.move(150, 100)
            self.btn_no.setCursor(Qt.PointingHandCursor)
            self.btn_no.clicked.connect(self.showMessageBox)

            shortcut = QShortcut(QKeySequence('Ctrl+Q'), self)
            shortcut.activated.connect(QApplication.quit)

            self.show()

        def showMessageBox(self):
            QMessageBox.information(self, 'Really?', 'Ok.')
            QApplication.quit()

        def teleport(self):
            x = QRandomGenerator.global_().bounded(self.width() - self.btn_yes.width())
            y = QRandomGenerator.global_().bounded(self.height() - self.btn_yes.height())
            self.btn_yes.move(x, y)

    def __init__(self, args):
        super().__init__(args)
        self.main_widget = self.MainWidget()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
