import sys
import sqlite3 as sql
from PyQt5 import QtWidgets
import Main_Window

class MainWindow(QtWidgets.QMainWindow, Main_Window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.link = 0
        self.mass = self.read_db()
        self.show_items(self.link)

    def insert_db(self):
        ID = str(self.ID_data.text())
        surname = str(self.Surame_data.text())
        name = str(self.Name_data.text())
        secondname = str(self.Secondname_data.text())
        phone_num = str(self.Phone_num_data.text())

    def read_db(self):
        connection = sql.connect('data_base')
        cursor = connection.cursor()
        self.mass = cursor.execute('SELECT * FROM users').fetchall()
        return self.mass

    def show_items(self, index):
        self.ID_data.setText(str(self.mass[index][0]))
        self.Surname_data.setText(str(self.mass[index][1]))
        self.Name_data.setText(str(self.mass[index][2]))
        self.Secondname_data.setText(str(self.mass[index][3]))
        self.Phone_num_data.setText(str(self.mass[index][4]))





def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

main()