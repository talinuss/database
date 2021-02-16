# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchWindowKHKDpp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setup(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(220, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Surname = QLabel(self.centralwidget)
        self.Surname.setObjectName(u"Surname")
        self.Surname.setGeometry(QRect(10, 40, 60, 20))
        self.Second_name_search = QLineEdit(self.centralwidget)
        self.Second_name_search.setObjectName(u"Second_name_data")
        self.Second_name_search.setGeometry(QRect(80, 100, 130, 20))
        self.ID = QLabel(self.centralwidget)
        self.ID.setObjectName(u"ID")
        self.ID.setGeometry(QRect(10, 10, 60, 20))
        self.Phone_num = QLabel(self.centralwidget)
        self.Phone_num.setObjectName(u"Phone_num")
        self.Phone_num.setGeometry(QRect(10, 130, 61, 20))
        self.Surname_search = QLineEdit(self.centralwidget)
        self.Surname_search.setObjectName(u"Surname_data")
        self.Surname_search.setGeometry(QRect(80, 40, 130, 20))
        self.Second_name = QLabel(self.centralwidget)
        self.Second_name.setObjectName(u"Second_name")
        self.Second_name.setGeometry(QRect(10, 100, 60, 20))
        self.Name = QLabel(self.centralwidget)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(10, 70, 60, 20))
        self.Name_search = QLineEdit(self.centralwidget)
        self.Name_search.setObjectName(u"Name_data")
        self.Name_search.setGeometry(QRect(80, 70, 130, 20))
        self.Phone_num_search = QLineEdit(self.centralwidget)
        self.Phone_num_search.setObjectName(u"Phone_num_data")
        self.Phone_num_search.setGeometry(QRect(80, 130, 130, 20))
        self.ID_search = QLineEdit(self.centralwidget)
        self.ID_search.setObjectName(u"ID_data")
        self.ID_search.setGeometry(QRect(80, 10, 130, 20))
        self.button_search = QPushButton(self.centralwidget)
        self.button_search.setObjectName(u"button_search")
        self.button_search.setGeometry(QRect(10, 160, 200, 30))
        self.search_table = QTableView(self.centralwidget)
        self.search_table.setModel()
        font = QFont()
        font.setFamily(u"Microsoft JhengHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_search.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Surname.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u044f:", None))
        self.ID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.Phone_num.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.Second_name.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.button_search.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
    # retranslateUi

