from PyQt5 import QtCore, QtGui, QtWidgets

a = int(input('Введите пароль:'))
if a == 2077:
    print('Пароль верный')
else:
    print('Пароль неверный')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.action5 = QtWidgets.QAction(MainWindow)
        self.action5.setObjectName("action5")
        self.action6 = QtWidgets.QAction(MainWindow)
        self.action6.setObjectName("action6")
        self.action7 = QtWidgets.QAction(MainWindow)
        self.action7.setObjectName("action7")
        self.action8 = QtWidgets.QAction(MainWindow)
        self.action8.setObjectName("action8")
        self.action9 = QtWidgets.QAction(MainWindow)
        self.action9.setObjectName("action9")
        self.action10 = QtWidgets.QAction(MainWindow)
        self.action10.setObjectName("action10")
        self.action11 = QtWidgets.QAction(MainWindow)
        self.action11.setObjectName("action11")
        self.action12 = QtWidgets.QAction(MainWindow)
        self.action12.setObjectName("action12")
        self.action13 = QtWidgets.QAction(MainWindow)
        self.action13.setObjectName("action13")
        self.action14 = QtWidgets.QAction(MainWindow)
        self.action14.setObjectName("action14")
        self.action15 = QtWidgets.QAction(MainWindow)
        self.action15.setObjectName("action15")
        self.action16 = QtWidgets.QAction(MainWindow)
        self.action16.setObjectName("action16")
        self.action17 = QtWidgets.QAction(MainWindow)
        self.action17.setObjectName("action17")
        self.action18 = QtWidgets.QAction(MainWindow)
        self.action18.setObjectName("action18")
        self.action19 = QtWidgets.QAction(MainWindow)
        self.action19.setObjectName("action19")
        self.action20 = QtWidgets.QAction(MainWindow)
        self.action20.setObjectName("action20")
        self.action21 = QtWidgets.QAction(MainWindow)
        self.action21.setObjectName("action21")
        self.action22 = QtWidgets.QAction(MainWindow)
        self.action22.setObjectName("action22")
        self.action23 = QtWidgets.QAction(MainWindow)
        self.action23.setObjectName("action23")
        self.action24 = QtWidgets.QAction(MainWindow)
        self.action24.setObjectName("action24")
        self.action25 = QtWidgets.QAction(MainWindow)
        self.action25.setObjectName("action25")
        self.action26 = QtWidgets.QAction(MainWindow)
        self.action26.setObjectName("action26")
        self.action27 = QtWidgets.QAction(MainWindow)
        self.action27.setObjectName("action27")

        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action3)
        self.menu.addAction(self.action4)
        self.menu.addAction(self.action5)
        self.menu.addAction(self.action6)
        self.menu.addAction(self.action7)
        self.menu.addAction(self.action8)
        self.menu.addAction(self.action9)
        self.menu.addAction(self.action10)
        self.menu.addAction(self.action11)
        self.menu.addAction(self.action12)
        self.menu.addAction(self.action13)
        self.menu.addAction(self.action14)
        self.menu.addAction(self.action15)
        self.menu.addAction(self.action16)
        self.menu.addAction(self.action17)
        self.menu.addAction(self.action18)
        self.menu.addAction(self.action19)
        self.menu.addAction(self.action20)
        self.menu.addAction(self.action21)
        self.menu.addAction(self.action22)
        self.menu.addAction(self.action23)
        self.menu.addAction(self.action24)
        self.menu.addAction(self.action25)
        self.menu.addAction(self.action26)
        self.menu.addAction(self.action27)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "Выбрать слой или карту"))
        self.action1.setText(_translate("MainWindow", "Комната №1"))
        self.action2.setText(_translate("MainWindow", "Комната №2"))
        self.action3.setText(_translate("MainWindow", "Комната №3"))
        self.action4.setText(_translate("MainWindow", "Комната №4"))
        self.action5.setText(_translate("MainWindow", "Комната №5"))
        self.action6.setText(_translate("MainWindow", "Комната №6"))
        self.action7.setText(_translate("MainWindow", "Коридор"))
        self.action8.setText(_translate("MainWindow", "Несущие стены"))
        self.action9.setText(_translate("MainWindow", "Окна"))
        self.action10.setText(_translate("MainWindow", "Комната №1 слой граница"))
        self.action11.setText(_translate("MainWindow", "Комната №1 слой батареи"))
        self.action12.setText(_translate("MainWindow", "Комната №1 слой лестница"))
        self.action13.setText(_translate("MainWindow", "Комната №2 слой граница"))
        self.action14.setText(_translate("MainWindow", "Комната №2 слой батареи"))
        self.action15.setText(_translate("MainWindow", "Комната №2 слой пол"))
        self.action16.setText(_translate("MainWindow", "Комната №3 слой граница"))
        self.action17.setText(_translate("MainWindow", "Комната №3 слой батареи"))
        self.action18.setText(_translate("MainWindow", "Комната №3 слой шкафы"))
        self.action19.setText(_translate("MainWindow", "Комната №4 слой граница"))
        self.action20.setText(_translate("MainWindow", "Комната №4 слой батареи"))
        self.action21.setText(_translate("MainWindow", "Комната №4 слой шкафы"))
        self.action22.setText(_translate("MainWindow", "Комната №5 слой граница"))
        self.action23.setText(_translate("MainWindow", "Комната №5 слой батареи"))
        self.action24.setText(_translate("MainWindow", "Комната №5 слой шкафы"))
        self.action25.setText(_translate("MainWindow", "Комната №6 слой граница"))
        self.action26.setText(_translate("MainWindow", "Комната №6 слой батареи"))
        self.action27.setText(_translate("MainWindow", "Комната №6 слой шкафы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


