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
    def setup(self, SearchWindow):
        if not SearchWindow.objectName():
            SearchWindow.setObjectName(u"MainWindow")
        SearchWindow.resize(220, 300)
        self.centralwidget = QWidget(SearchWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Surname = QLabel(self.centralwidget)
        self.Surname.setObjectName(u"Surname")
        self.Surname.setFixedSize(60, 20)
        self.Second_name_search = QLineEdit(self.centralwidget)
        self.Second_name_search.setObjectName(u"Second_name_data")
        self.Second_name_search.setBaseSize(QSize(130, 20))
        self.ID = QLabel(self.centralwidget)
        self.ID.setObjectName(u"ID")
        self.ID.setFixedSize(60, 20)
        self.Phone_num = QLabel(self.centralwidget)
        self.Phone_num.setObjectName(u"Phone_num")
        self.Phone_num.setFixedSize(60, 20)
        self.Surname_search = QLineEdit(self.centralwidget)
        self.Surname_search.setObjectName(u"Surname_data")
        self.Surname_search.setBaseSize(QSize(130, 20))
        self.Second_name = QLabel(self.centralwidget)
        self.Second_name.setObjectName(u"Second_name")
        self.Second_name.setFixedSize(60, 20)
        self.Name = QLabel(self.centralwidget)
        self.Name.setObjectName(u"Name")
        self.Name.setFixedSize(60, 20)
        self.Name_search = QLineEdit(self.centralwidget)
        self.Name_search.setObjectName(u"Name_data")
        self.Name_search.setBaseSize(QSize(130, 20))
        self.Phone_num_search = QLineEdit(self.centralwidget)
        self.Phone_num_search.setObjectName(u"Phone_num_data")
        self.Phone_num_search.setBaseSize(QSize(130, 20))
        self.ID_search = QLineEdit(self.centralwidget)
        self.ID_search.setObjectName(u"ID_data")
        self.ID_search.setBaseSize(QSize(130, 20))
        self.button_search = QPushButton(self.centralwidget)
        self.button_search.setObjectName(u"button_search")
        self.button_search.setBaseSize(QSize(130, 20))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setBaseSize(QSize(130, 20))
        self.table = QTableWidget(self.centralwidget)

        hbox_ID = QHBoxLayout()
        hbox_ID.addWidget(self.ID, 0, Qt.AlignLeft)
        hbox_ID.addWidget(self.ID_search, 0)

        hbox_Surname = QHBoxLayout()
        hbox_Surname.addWidget(self.Surname, 0, Qt.AlignLeft)
        hbox_Surname.addWidget(self.Surname_search, 0)

        hbox_Name = QHBoxLayout()
        hbox_Name.addWidget(self.Name, 0, Qt.AlignLeft)
        hbox_Name.addWidget(self.Name_search, 0)

        hbox_Second_name = QHBoxLayout()
        hbox_Second_name.addWidget(self.Second_name, 0, Qt.AlignLeft)
        hbox_Second_name.addWidget(self.Second_name_search, 0)

        hbox_Phone_num = QHBoxLayout()
        hbox_Phone_num.addWidget(self.Phone_num, 0, Qt.AlignLeft)
        hbox_Phone_num.addWidget(self.Phone_num_search, 0)

        hbox_button = QHBoxLayout()
        hbox_button.addWidget(self.button_search, 0)

        hbox_combobox = QHBoxLayout()
        hbox_combobox.addWidget(self.comboBox, 0, Qt.AlignLeft)

        vbox_table = QVBoxLayout()
        vbox_table.addWidget(self.table, 0)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(hbox_ID, 0)
        self.vbox.addLayout(hbox_Surname, 0)
        self.vbox.addLayout(hbox_Name, 0)
        self.vbox.addLayout(hbox_Second_name, 0)
        self.vbox.addLayout(hbox_Phone_num, 0)
        self.vbox.addLayout(hbox_button, 0)
        self.vbox.addLayout(hbox_combobox)
        self.vbox.addLayout(vbox_table, 1)

        self.centralwidget.setLayout(self.vbox)

        font = QFont()
        font.setFamily(u"Microsoft JhengHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_search.setFont(font)

        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)

        QMetaObject.connectSlotsByName(SearchWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Surname.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u044f:", None))
        self.ID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.Phone_num.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.Second_name.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.button_search.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e ID", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0444\u0430\u043c\u0438\u043b\u0438\u0438", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0438\u043c\u0435\u043d\u0438", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u0443", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043d\u043e\u043c\u0435\u0440\u0443", None))

    # retranslateUi