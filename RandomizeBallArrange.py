import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # 横のレイアウト
        self.horizon = QHBoxLayout()
        # 縦のレイアウト
        self.vertical = QVBoxLayout()

        # ボタンの追加
        self.button = QPushButton('Reset', self)
        self.button.move(350,720)
        self.button.clicked.connect(self.randomize)

        self.horizon.addLayout(self.vertical)
        self.setLayout(self.horizon)

        self.setGeometry(0, 50, 800, 800)
        self.setWindowTitle('Randomize Ball Arrange')

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        #背景
        painter.setBrush(Qt.gray)
        painter.drawRect(0, 0.0, 800.0, 800.0)

        # 枠
        painter.setBrush(Qt.darkGreen)
        painter.drawRect(27, 0.0, 740.0, 800.0)

        #壁
        painter.setPen(QPen(Qt.black, 11, Qt.SolidLine))
        painter.drawLine(33, 0, 33, 800)
        painter.drawLine(767, 0, 767, 800)

        #ボール配置用枠
        painter.setPen(QPen(Qt.gray, 2, Qt.SolidLine))
        #横ライン
        painter.drawLine(40, 125, 760, 125)
        painter.drawLine(40, 250, 760, 250)
        #縦ライン
        painter.drawLine(150, 25, 150, 350)
        painter.drawLine(275, 25, 275, 350)
        painter.drawLine(525, 25, 525, 350)
        painter.drawLine(650, 25, 650, 350)

        #白線
        painter.setPen(QPen(Qt.white, 4, Qt.SolidLine))
        #横ライン
        painter.drawLine(40, 400, 760, 400)
        #縦ライン
        painter.drawLine(400, 0, 400, 800)

        #台
        painter.setPen(Qt.gray)
        painter.setBrush(Qt.black)
        painter.drawRect(40, 650, 150, 150)
        painter.drawRect(610, 650, 150, 150)
        painter.setBrush(Qt.red)
        painter.drawRect(55, 665, 120, 120)
        painter.setBrush(Qt.blue)
        painter.drawRect(625, 665, 120, 120)

        #ボールの配置
        center_left = [QPoint(95, 70), QPoint(215, 70), QPoint(335, 70),
                       QPoint(95, 185), QPoint(215, 185), QPoint(335, 185),
                       QPoint(95, 300), QPoint(215, 300), QPoint(335, 300)
                       ]

        center_right = [QPoint(460, 70), QPoint(590, 70), QPoint(710, 70),
                        QPoint(460, 185), QPoint(590, 185), QPoint(710, 185),
                        QPoint(460, 300), QPoint(590, 300), QPoint(710, 300)
                        ]

        #ボールの配置をランダムに決める
        place_left = random.sample(center_left, 6)
        place_right = random.sample(center_right, 6)

        #ボール描画
        for i in range(0, 3):
            painter.setPen(Qt.white)
            painter.setBrush(Qt.red)
            painter.drawEllipse(place_left[i], 35, 35)
            painter.drawEllipse(place_right[i], 35, 35)
        for i in range(3, 6):
            painter.setPen(Qt.white)
            painter.setBrush(Qt.blue)
            painter.drawEllipse(place_left[i], 35, 35)
            painter.drawEllipse(place_right[i], 35, 35)

        painter.end()

    def randomize(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())