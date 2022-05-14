import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap

from untitled import Ui_MainWindow              # <-------

class Example(QMainWindow):                                #(QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle('Red Rock')
        self.image = "ima.jpg"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.triggered.connect(self.load_image1)
        self.ui.pushButton_2.triggered.connect(self.load_image2)
        self.ui.pushButton_3.triggered.connect(self.load_image3)
        self.ui.pushButton_4.triggered.connect(self.load_image2)
        self.ui.pushButton_5.triggered.connect(self.load_image2)
        self.ui.pushButton_6.triggered.connect(self.load_image2)
        # ...
        self.hbox = QHBoxLayout(self.ui.centralwidget)

        self.initUI()

    def initUI(self):      
        #hbox = QHBoxLayout(self.ui.centralwidget)
        pixmap = QPixmap(self.image)        #("0.bmp")
        self.lbl = QLabel()                 #(self)
        self.lbl.setPixmap(pixmap)
        self.hbox.addWidget(self.lbl)

#        self.setLayout(hbox)
#        self.move(100, 200)
#        self.show()        

    def load_image1(self):
        self.image = "ais_1.png"
        self.lbl.hide()
        self.initUI()
    def load_image2(self):
        self.image = "ais_2.png"
        self.lbl.hide()
        self.initUI()
    def load_image3(self):
        self.image = "ais_2.png"
        self.lbl.hide()
        self.initUI()
    # ...    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())