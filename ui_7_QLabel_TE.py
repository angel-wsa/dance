import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel)
from PyQt5.QtGui import QImage, QPixmap
import cv2


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hello')
        self.resize(1920, 980)
        # self.setStyleSheet('background:transparent;')
        self.ui()
        self.score()
        self.photo()
        self.top()
        self.music()



    def ui(self):
        grview = QtWidgets.QGraphicsView(self)  # 在win視窗程式中建立顯示圖形元件
        grview.setGeometry(0, 0, 1920, 980)  # 設定擺放圖形元件位置
        scene = QtWidgets.QGraphicsScene()  # 建立場景元件
        scene.setSceneRect(0, 0, 1915, 975)  # 設定場景元件位置
        img = QtGui.QPixmap("./ui_7.jpg")
        img = img.scaled(1920, 980)

        scene.addPixmap(img)  # 將圖片加入scene
        grview.setScene(scene)  # 設定擺放圖形元件的場景為 scene

    def score(self):
        self.input_1 = QtWidgets.QTextEdit(self)
        self.input_1.setGeometry(1450, 180, 400, 150)
        self.input_1.setStyleSheet('''
            QTextEdit{
                color:rgb(255, 255, 255);
                font-size: 100px;
                font-weight: normal;
                font-weight: bold;
                front-family: Arial;
                spacing: 5.0;
                background: #031d2c;
                border: #031d2c;
                text-align:center;
            }
        ''')

    def top(self):
        self.input_2 = QtWidgets.QTextEdit(self)
        self.input_2.setGeometry(1550, 400, 400, 150)
        self.input_2.setStyleSheet('''
            QTextEdit{
                color:rgb(255, 255, 255);
                font-size: 70px;
                font-weight: normal;
                font-weight: bold;
                front-family: Arial;
                background:  #031d2c;
                border: #031d2c;
                text-align:center;
            }
         ''')

    def photo(self):

        self.mylabel = QLabel('this is an image', self)

        img = cv2.imread('./elon-musk-1.jpg')
        img = cv2.resize(img,(360,360))
        print(type(img))  # numpy.ndarray
        print(img.data)  # memoryview
        height, width, channel = img.shape
        bytesPerline = 3 * width
        self.mylabel.setGeometry(735, 180, 400,350)
        self.myqimage = QImage(img.data, width, height, bytesPerline, QImage.Format_RGB888)
        self.mylabel.setPixmap(QPixmap.fromImage(self.myqimage.rgbSwapped()))



    def music(self):

        self.mylabel = QLabel('this is an image', self)

        img = cv2.imread('./elon-musk-1.jpg')
        img = cv2.resize(img,(558,558))
        print(type(img))  # numpy.ndarray
        print(img.data)  # memoryview
        height, width, channel = img.shape
        bytesPerline = 3 * width
        self.mylabel.setGeometry(98, 180, 560, 520)
        self.myqimage = QImage(img.data, width, height, bytesPerline, QImage.Format_RGB888)
        self.mylabel.setPixmap(QPixmap.fromImage(self.myqimage.rgbSwapped()))





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    screen = QtWidgets.QApplication.desktop()
    screen_w = screen.width()  # 電腦螢幕寬度
    screen_h = screen.height()  # 電腦螢幕高度
    print("視窗寬度為: ", screen_w)
    print("視窗長度為: ", screen_h)

    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())

    window = colorSelector()
    window.show()