# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_pars.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 526)
        MainWindow.setMinimumSize(QtCore.QSize(584, 526))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout.addWidget(self.lcdNumber_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setObjectName("label_date")
        self.verticalLayout.addWidget(self.label_date)
        self.label_wind = QtWidgets.QLabel(self.centralwidget)
        self.label_wind.setObjectName("label_wind")
        self.verticalLayout.addWidget(self.label_wind)
        self.label_level = QtWidgets.QLabel(self.centralwidget)
        self.label_level.setObjectName("label_level")
        self.verticalLayout.addWidget(self.label_level)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_date.setText(_translate("MainWindow", "TextLabel"))
        self.label_wind.setText(_translate("MainWindow", "TextLabel"))
        self.label_level.setText(_translate("MainWindow", "TextLabel"))
