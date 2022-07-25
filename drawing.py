# -*- coding: utf-8 -*-


from PySide6 import QtCore, QtGui, QtWidgets
import sys


font = QtGui.QFont()
font.setPointSize(20)
import random
import pandas as pd



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(743, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        # self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        # self.textBrowser.setMaximumSize(QtCore.QSize(8000, 800))
        # self.textBrowser.setObjectName("textBrowser")
        # self.textBrowser.setFont(font)
        # self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 3)

        
        self.table=pd.read_excel('组内抽签名单.xlsx')
        print(self.table)
        self.tableWidget1=QtWidgets.QTableWidget()
        self.tableWidget1.setObjectName("tableWidget")
        self.tableWidget1.setColumnCount(self.table.shape[1])
        self.tableWidget1.setRowCount(self.table.shape[0])
        self.tableWidget1.setHorizontalHeaderLabels(['姓名','顺序'])
        
        self.tableWidget1.setStyleSheet("selection-background-color:pink;")
        self.tableWidget1.raise_()
        self.gridLayout.addWidget(self.tableWidget1,0,0,1,3)
        
        
        self.fillTable(self.table)
        

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 743, 24))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.on_click)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "上海财经大学招生抽签程序"))
        self.pushButton.setText(_translate("MainWindow", "抽签"))

    def fillTable(self,market1):
        for index,row in market1.iterrows():
            self.tableWidget1.setItem(index,0,QtWidgets.QTableWidgetItem(str(row['姓名'])))
            self.tableWidget1.setItem(index,1,QtWidgets.QTableWidgetItem(str(row['顺序'])))
        
        
    def on_click(self):
        items1=list(range(1,self.table.shape[0]+1))
        random.shuffle(items1)
        self.table['顺序']=items1


        self.fillTable(self.table)




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())