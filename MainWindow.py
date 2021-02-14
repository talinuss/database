# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowLwQnGa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(222, 245)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_delete = QPushButton(self.centralwidget)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setGeometry(QRect(60, 210, 101, 21))
        self.button_insert = QPushButton(self.centralwidget)
        self.button_insert.setObjectName(u"button_insert")
        self.button_insert.setGeometry(QRect(60, 190, 101, 21))
        self.Surname = QLabel(self.centralwidget)
        self.Surname.setObjectName(u"Surname")
        self.Surname.setGeometry(QRect(10, 70, 61, 20))
        self.Secondname = QLabel(self.centralwidget)
        self.Secondname.setObjectName(u"Secondname")
        self.Secondname.setGeometry(QRect(10, 130, 61, 21))
        self.Name = QLabel(self.centralwidget)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(10, 100, 61, 21))
        self.button_last = QPushButton(self.centralwidget)
        self.button_last.setObjectName(u"button_last")
        self.button_last.setGeometry(QRect(10, 190, 41, 41))
        self.button_next = QPushButton(self.centralwidget)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setGeometry(QRect(170, 190, 41, 41))
        self.ID = QLabel(self.centralwidget)
        self.ID.setObjectName(u"ID")
        self.ID.setGeometry(QRect(10, 40, 61, 21))
        self.Name_data = QLineEdit(self.centralwidget)
        self.Name_data.setObjectName(u"Name_data")
        self.Name_data.setGeometry(QRect(80, 100, 131, 20))
        self.Secondname_data = QLineEdit(self.centralwidget)
        self.Secondname_data.setObjectName(u"Secondname_data")
        self.Secondname_data.setGeometry(QRect(80, 130, 131, 20))
        self.Surname_data = QLineEdit(self.centralwidget)
        self.Surname_data.setObjectName(u"Surname_data")
        self.Surname_data.setGeometry(QRect(80, 70, 131, 20))
        self.Phone_num = QLabel(self.centralwidget)
        self.Phone_num.setObjectName(u"Phone_num")
        self.Phone_num.setGeometry(QRect(10, 160, 61, 20))
        self.Phone_num_data = QLineEdit(self.centralwidget)
        self.Phone_num_data.setObjectName(u"Phone_num_data")
        self.Phone_num_data.setGeometry(QRect(80, 160, 131, 20))
        self.ID_data = QLabel(self.centralwidget)
        self.ID_data.setObjectName(u"ID_data")
        self.ID_data.setGeometry(QRect(80, 40, 131, 21))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 10, 121, 21))
        self.button_sort = QPushButton(self.centralwidget)
        self.button_sort.setObjectName(u"button_sort")
        self.button_sort.setGeometry(QRect(140, 10, 31, 21))
        self.button_search = QPushButton(self.centralwidget)
        self.button_search.setObjectName(u"button_search")
        self.button_search.setGeometry(QRect(180, 10, 31, 21))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.button_insert.setText(QCoreApplication.translate("MainWindow", u"insert", None))
        self.Surname.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u044f:", None))
        self.Secondname.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.button_last.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.button_next.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.ID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.Phone_num.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.ID_data.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e ID", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0444\u0430\u043c\u0438\u043b\u0438\u0438", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0438\u043c\u0435\u043d\u0438", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u0443", None))

        self.button_sort.setText(QCoreApplication.translate("MainWindow", u"sort", None))
        self.button_search.setText(QCoreApplication.translate("MainWindow", u"search", None))
    # retranslateUi

