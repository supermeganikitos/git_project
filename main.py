import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.xpos = randint(200, 400)
        self.ypos = randint(200, 400)
        self.siz = 20
        self.color = QColor(255, 255, 0)
        self.do_paint = False
        self.setMouseTracking(True)
        self.sircle_btn.clicked.connect(self.dr)

    def dr(self):
        self.siz = randint(20, 101)
        self.xpos = randint(200, 400)
        self.ypos = randint(200, 400)
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawfigure(qp)
            qp.end()

    def drawfigure(self, qp):
        qp.setBrush(self.color)
        qp.drawEllipse(QPointF(self.xpos, self.ypos), self.siz, self.siz)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
