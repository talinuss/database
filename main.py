import sys
import sqlite3 as sql
from PyQt5 import QtWidgets
import Main_Window

class MainWindow(QtWidgets.QMainWindow, Main_Window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.link = 0 #соответсвует индексу текущего пользоваетля из массива self.mass
        self.read_db()
        self.show_items(self.link)
        self.button_sort.clicked.connect(self.sorted)
        self.button_next.clicked.connect(self.next)
        self.button_last.clicked.connect(self.last)

    def insert_db(self):
        surname = str(self.Surame_data.text())
        name = str(self.Name_data.text())
        secondname = str(self.Secondname_data.text())
        phone_num = str(self.Phone_num_data.text())
        new_row = [surname, name, secondname, phone_num]
        connection = sql.connect('data_base')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (surname, name, second_name, phone_num) VALUES (?, ?, ?, ?)', new_row)
        cursor.close()
        connection.commit()
        connection.close()
        self.link = 0
        self.show_items(self.link)

    def read_db(self):
        connection = sql.connect('data_base')
        cursor = connection.cursor()
        self.mass = cursor.execute('SELECT * FROM users').fetchall()
        cursor.close()
        connection.close()

    def show_items(self, index):
        self.ID_data.setText(str(self.mass[index][0]))
        self.Surname_data.setText(str(self.mass[index][1]))
        self.Name_data.setText(str(self.mass[index][2]))
        self.Secondname_data.setText(str(self.mass[index][3]))
        self.Phone_num_data.setText(str(self.mass[index][4]))

    def sort(self):
        if self.comboBox.currentIndex() == 0:
            self.mass = sorted(self.mass, key = lambda k: k[0]) #ID
        elif self.comboBox.currentIndex() == 1:
            self.mass = sorted(self.mass, key = lambda k: k[1]) #Surname
        elif self.comboBox.currentIndex() == 2:
            self.mass = sorted(self.mass, key = lambda k: k[2]) #Name
        elif self.comboBox.currentIndex() == 3:
            self.mass = sorted(self.mass, key = lambda k: k[3]) #Secondname

    def sorted(self):
        self.sort()
        self.show_items(self.link)

    def next(self):
        if self.link == len(self.mass) - 1:
            self.link = 0
            self.show_items(self.link)
        else:
            self.link += 1
            self.show_items(self.link)

    def last(self):
        if self.link == 0:
            self.link = len(self.mass)-1
            self.show_items(self.link)
        else:
            self.link -= 1
            self.show_items(self.link)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

main()