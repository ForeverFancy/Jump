# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JUMP.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import linecache

class Ui_MainWindow(object):
    def __init__(self,MainWindow):
        self.setupUi(MainWindow)
        self.List=[]
        self.num=1

    def setupUi(self, MainWindow):
        self.size = int(input("Please choose the size of the board:"))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 300, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(self.size)
        self.tableWidget.setRowCount(self.size)
        for i in range(0,self.size):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            self.tableWidget.setColumnWidth(i, 50)

        self.Label=QtWidgets.QLabel(self.centralwidget)
        self.Label.move(60,430)
        self.Label.setText("Choose the solution:")

        self.textbox=QtWidgets.QLineEdit(self.centralwidget)
        self.textbox.move(60,450)
        self.textbox.resize(100,40)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏表头


        item = QtWidgets.QTableWidgetItem(" ")
        item.setBackground(QtGui.QColor(240, 255, 240))
        self.tableWidget.setItem(0, 0, item)

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(90, 580, 112, 34))
        self.pushButton_1.move(300, 530)
        self.pushButton_1.setObjectName("Start")
        self.pushButton_1.setText("Start")
        self.pushButton_1.clicked.connect(lambda :(self.reset(),self.getNum(),self.read(),self.update()))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getNum(self):
        try:
            self.solutionNum=int(self.textbox.text())
        except:
            pass
        self.textbox.setText("")

    def read(self):
        k=linecache.getline("solution"+str(self.size-4)+".txt",self.solutionNum,"r+")
        self.List=str(k).strip('\n').split(',')


    def reset(self):
        for i in range(0,self.size):
            for j in range(0,self.size):
                item = QtWidgets.QTableWidgetItem(" ")
                self.tableWidget.setItem(i, j, item)

        item = QtWidgets.QTableWidgetItem(" ")
        item.setBackground(QtGui.QColor(240, 255, 240))
        self.tableWidget.setItem(0, 0, item)

    def update(self):

        self.updateThread=runThread()
        self.updateThread.counter_value.connect(self.set_item)
        self.updateThread.start()

    def set_item(self,counter):

        if counter<=self.size**2-1:
            item = QtWidgets.QTableWidgetItem(" ")
            item.setBackground(QtGui.QColor(240, 255, 240))
            self.tableWidget.setItem(int(self.List[counter][0]),int(self.List[counter][1]), item)
        else:
            try:
                self.updateThread.stop()
            except:
                pass


class runThread(QtCore.QThread):

    counter_value=QtCore.pyqtSignal(int)

    def __init__(self,parent=None,count_start=0):
        super(runThread,self).__init__(parent)
        self.counter=count_start
        self.is_Running=True

    def run(self):
        while self.counter<50 and self.is_Running==True:
            time.sleep(0.2)
            self.counter+=1
            self.counter_value.emit(self.counter)

    def stop(self):
        self.counter=0
        self.is_Running=False
        self.terminate()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
