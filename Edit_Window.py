# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditWindowKHKDpp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setup(self, EditWindow):
        if not EditWindow.objectName():
            EditWindow.setObjectName(u"MainWindow")
        EditWindow.resize(220, 220)
        self.centralwidget = QWidget(EditWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.Surname = QLabel(self.centralwidget)
        self.Surname.setObjectName(u"Surname")
        self.Surname.setFixedSize(60, 20)
        self.Second_name_edit = QLineEdit(self.centralwidget)
        self.Second_name_edit.setObjectName(u"Second_name_data")
        self.Second_name_edit.setBaseSize(QSize(130, 20))
        self.ID = QLabel(self.centralwidget)
        self.ID.setObjectName(u"ID")
        self.ID.setFixedSize(60, 20)
        self.Phone_num = QLabel(self.centralwidget)
        self.Phone_num.setObjectName(u"Phone_num")
        self.Phone_num.setFixedSize(60, 20)
        self.Surname_edit = QLineEdit(self.centralwidget)
        self.Surname_edit.setObjectName(u"Surname_data")
        self.Surname_edit.setBaseSize(QSize(130, 20))
        self.Second_name = QLabel(self.centralwidget)
        self.Second_name.setObjectName(u"Second_name")
        self.Second_name.setFixedSize(60, 20)
        self.Name = QLabel(self.centralwidget)
        self.Name.setObjectName(u"Name")
        self.Name.setFixedSize(60, 20)
        self.Name_edit = QLineEdit(self.centralwidget)
        self.Name_edit.setObjectName(u"Name_data")
        self.Name_edit.setBaseSize(QSize(130, 20))
        self.Phone_num_edit = QLineEdit(self.centralwidget)
        self.Phone_num_edit.setObjectName(u"Phone_num_data")
        self.Phone_num_edit.setBaseSize(QSize(130, 20))
        self.ID_edit = QLabel(self.centralwidget)
        self.ID_edit.setObjectName(u"ID_data")
        self.ID_edit.setBaseSize(QSize(130, 20))
        self.button_save = QPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setBaseSize(QSize(130, 20))
        self.button_cancel = QPushButton(self.centralwidget)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setBaseSize(QSize(130, 20))

        hbox_ID = QHBoxLayout()
        hbox_ID.addWidget(self.ID, 0, Qt.AlignLeft)
        hbox_ID.addWidget(self.ID_edit, 0)

        hbox_Surname = QHBoxLayout()
        hbox_Surname.addWidget(self.Surname, 0, Qt.AlignLeft)
        hbox_Surname.addWidget(self.Surname_edit, 0)

        hbox_Name = QHBoxLayout()
        hbox_Name.addWidget(self.Name, 0, Qt.AlignLeft)
        hbox_Name.addWidget(self.Name_edit, 0)

        hbox_Second_name = QHBoxLayout()
        hbox_Second_name.addWidget(self.Second_name, 0, Qt.AlignLeft)
        hbox_Second_name.addWidget(self.Second_name_edit, 0)

        hbox_Phone_num = QHBoxLayout()
        hbox_Phone_num.addWidget(self.Phone_num, 0, Qt.AlignLeft)
        hbox_Phone_num.addWidget(self.Phone_num_edit, 0)

        hbox_button_save = QHBoxLayout()
        hbox_button_save.addWidget(self.button_save, 0)

        hbox_button_cancel = QHBoxLayout()
        hbox_button_cancel.addWidget(self.button_cancel, 0)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(hbox_ID, 0)
        self.vbox.addLayout(hbox_Surname, 0)
        self.vbox.addLayout(hbox_Name, 0)
        self.vbox.addLayout(hbox_Second_name, 0)
        self.vbox.addLayout(hbox_Phone_num, 0)
        self.vbox.addLayout(hbox_button_save, 0)
        self.vbox.addLayout(hbox_button_cancel, 0)
        self.vbox.addStretch(1)
        self.centralwidget.setLayout(self.vbox)

        font = QFont()
        font.setFamily(u"Microsoft JhengHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_save.setFont(font)
        self.button_cancel.setFont(font)
        
        EditWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(EditWindow)
        QMetaObject.connectSlotsByName(EditWindow)
    # setup

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("EditWindow", u"EditWindow", None))
        self.Surname.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u044f:", None))
        self.Second_name.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.ID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.Phone_num.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.button_cancel.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
