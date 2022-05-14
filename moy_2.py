import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap

from moy import Ui_MainWindow              # <-------

class Example(QMainWindow):                                #(QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle('Red Rock')
        self.image = "ima.jpg"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action1.triggered.connect(self.load_image1)
        self.ui.action2.triggered.connect(self.load_image2)
        self.ui.action3.triggered.connect(self.load_image3)
        self.ui.action4.triggered.connect(self.load_image4)
        self.ui.action5.triggered.connect(self.load_image5)
        self.ui.action6.triggered.connect(self.load_image6)
        self.ui.action7.triggered.connect(self.load_image7)
        self.ui.action8.triggered.connect(self.load_image8)
        self.ui.action9.triggered.connect(self.load_image9)
        self.ui.action10.triggered.connect(self.load_image10)
        self.ui.action11.triggered.connect(self.load_image11)
        self.ui.action12.triggered.connect(self.load_image12)
        self.ui.action13.triggered.connect(self.load_image13)
        self.ui.action14.triggered.connect(self.load_image14)
        self.ui.action15.triggered.connect(self.load_image15)
        self.ui.action16.triggered.connect(self.load_image16)
        self.ui.action17.triggered.connect(self.load_image17)
        self.ui.action18.triggered.connect(self.load_image18)
        self.ui.action19.triggered.connect(self.load_image19)
        self.ui.action20.triggered.connect(self.load_image20)
        self.ui.action21.triggered.connect(self.load_image21)
        self.ui.action22.triggered.connect(self.load_image22)
        self.ui.action23.triggered.connect(self.load_image23)
        self.ui.action24.triggered.connect(self.load_image24)
        self.ui.action25.triggered.connect(self.load_image25)
        self.ui.action26.triggered.connect(self.load_image26)
        self.ui.action27.triggered.connect(self.load_image27)
        # ...
        self.hbox = QHBoxLayout(self.ui.centralwidget)

        self.initUI()

    def initUI(self):      
        # hbox = QHBoxLayout(self.ui.centralwidget)
        pixmap = QPixmap(self.image)        #("0.bmp")
        self.lbl = QLabel()                 #(self)
        self.lbl.setPixmap(pixmap)
        self.hbox.addWidget(self.lbl)

#        self.setLayout(hbox)
#        self.move(100, 200)
#        self.show()        

    def load_image1(self):
        self.image = "ais_1.1.png"
        self.lbl.hide()
        self.initUI()
    def load_image2(self):
        self.image = "ais_2.1.png"
        self.lbl.hide()
        self.initUI()

    def load_image3(self):
        self.image = "ais_3.png"
        self.lbl.hide()
        self.initUI()
    def load_image4(self):
        self.image = "ais_4.png"
        self.lbl.hide()
        self.initUI()
    def load_image5(self):
        self.image = "ais_5.png"
        self.lbl.hide()
        self.initUI()
    def load_image6(self):
        self.image = "ais_6.png"
        self.lbl.hide()
        self.initUI()
    def load_image7(self):
        self.image = "ais_korid.png"
        self.lbl.hide()
        self.initUI() 
    def load_image8(self):
        self.image = "ais_stena.png"
        self.lbl.hide()
        self.initUI()
    def load_image9(self):
        self.image = "ais_okno.png"
        self.lbl.hide()
        self.initUI()
    def load_image10(self):
        self.image = "комната №1 слой граница и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image11(self):
        self.image = "комната №1 слой батареи и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image12(self):
        self.image = "комната №1 слой лестница и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image13(self):
        self.image = "комната №2 слой граница и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image14(self):
        self.image = "комната №2 слой батареи и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image15(self):
        self.image = "комната №2 слой пол и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image16(self):
        self.image = "комната №3 слой граница и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image17(self):
        self.image = "комната №3 слой батареи и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image18(self):
        self.image = "комната №3 слой шкафы и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image19(self):
        self.image = "комната №4 слой граница и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image20(self):
        self.image = "комната №4 слой батареи и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image21(self):
        self.image = "комната №4 слой шкафы и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image22(self):
        self.image = "комната №5 слой граница и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image23(self):
        self.image = "комната №5 слой батарея и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image24(self):
        self.image = "комната №5 слой шкафы и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image25(self):
        self.image = "комната №6 слой граница и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image26(self):
        self.image = "комната №6 слой батарея и его атрибуты.png"
        self.lbl.hide()
        self.initUI()
    def load_image27(self):
        self.image = "комната №6 слой шкафы и его атрибуты.png"
        self.lbl.hide()
        self.initUI()                
    # ...    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

a = int(input('Введите пароль:'))
if a == 2077:
    print('Пароль верный')
else:
    print('Пароль неверный')
