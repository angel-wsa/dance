import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import cv2


from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel)
from PyQt5.QtGui import QImage, QPixmap

# from PyQt5.QtWidgets import QApplication, QWidget, QtGui



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hello')
        self.resize(1920, 980)
        # self.setStyleSheet('background:transparent;')
        self.ui()
        self.score()
        self.photo()
        self.music()



    def ui(self):
        grview = QtWidgets.QGraphicsView(self)  # 在win視窗程式中建立顯示圖形元件
        grview.setGeometry(0, 0, 1920, 980)  # 設定擺放圖形元件位置
        scene = QtWidgets.QGraphicsScene()  # 建立場景元件
        scene.setSceneRect(0, 0, 1915, 975)  # 設定場景元件位置
        img = QtGui.QPixmap("./ui_6.jpg")
        img = img.scaled(1920, 980)
        scene.addPixmap(img)  # 將圖片加入scene
        grview.setScene(scene)  # 設定擺放圖形元件的場景為 scene

    def score(self):
        input_1 = QtWidgets.QTextEdit(self)
        input_1.setGeometry(1450, 180, 400, 150)
        input_1.setStyleSheet('''
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


    def photo(self):
        grview = QtWidgets.QGraphicsView(self)  # 在win視窗程式中建立顯示圖形元件
        grview.setGeometry(730, 180, 370, 350 )  # 設定擺放圖形元件位置
        scene = QtWidgets.QGraphicsScene()  # 建立場景元件
        scene.setSceneRect(225, 200, 100, 150)  # 設定場景元件位置
        img = QtGui.QPixmap("./elon-musk-1.jpg")
        img.scaled(371, 371)
        scene.addPixmap(img)  # 將圖片加入scene
        grview.setScene(scene)  # 設定擺放圖形元件的場景為 scene


    def music(self):
        grview = QtWidgets.QGraphicsView(self)  # 在win視窗程式中建立顯示圖形元件
        grview.setGeometry(95, 185, 560, 510 )  # 設定擺放圖形元件位置
        scene = QtWidgets.QGraphicsScene()  # 建立場景元件
        scene.setSceneRect(22, 200, 520, 150)  # 設定場景元件位置
        img = QtGui.QPixmap("./elon-musk-1.jpg")
        img.scaled(558, 558)
        scene.addPixmap(img)  # 將圖片加入scene
        grview.setScene(scene)  # 設定擺放圖形元件的場景為 scene





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