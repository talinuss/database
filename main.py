import sys
import sqlite3 as sql
from PyQt5 import QtWidgets
import Main_Window
import Search_Window

class SearchWindow(QtWidgets.QMainWindow, Search_Window.Ui_MainWindow):
    def __init__(self, root):
        super().__init__(root)
        self.setup(self)
        self.main = root
        self.button_search.clicked.connect(self.search)

    def search(self):
        connection = sql.connect('data_base')
        cursor = connection.cursor()

        ID = (str(self.ID_search.text())).strip()
        surname = str(self.Surname_search.text()).strip()
        name = str(self.Name_search.text()).strip()
        second_name = str(self.Second_name_search.text()).strip()
        phone_num = str(self.Phone_num_search.text()).strip()

        request = ''
        
        if ID != '':
            request = ' id = '+ ID

        if surname != '':
            if request != '':
                request = request + ' AND surname = "'+ surname + '"'
            else:
                request = request + ' surname = "'+ surname + '"'

        if name != '':
            if request != '':
                request =  request + ' AND name = "'+ name + '"'
            else:
                request =  request + ' name = "'+ name + '"'
                
        if second_name != '':
            if request != '':
                request =  request + ' AND second_name = "'+ second_name + '"'
            else:
                request =  request + ' second_name = "'+ second_name + '"'
              
        if phone_num != '':
            if request != '':
                request = request + ' AND phone_num = "'+ phone_num + '"'
            else:
                request = request + ' phone_num = "'+ phone_num + '"'
        
        req = 'SELECT * FROM users where ('+ request +')'
        try:
            self.mass_search = cursor.execute(req).fetchall()
            print(req)
            print(self.mass_search)
        except:
            self.mass_search = False
            print('Oops... There is no request')


        cursor.close()
        connection.close()

        self.search_show()
        
    def search_show(self):
        connection = sql.connect('data_base')
        cursor = connection.execute('SELECT * FROM users')

        if self.mass_search:
            names = list(map(lambda x: x[0], cursor.description))
            self.table.setColumnCount(len(self.mass_search[0]))
            self.table.setRowCount(len(self.mass_search))
            self.table.setHorizontalHeaderLabels(names)
            

        cursor.close()
        connection.close()


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
        self.button_search.clicked.connect(self.search)

    def insert_db(self):
        surname = str(self.Surame_data.text())
        name = str(self.Name_data.text())
        second_name = str(self.Second_name_data.text())
        phone_num = str(self.Phone_num_data.text())
        new_row = [surname, name, second_name, phone_num]
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
        self.Second_name_data.setText(str(self.mass[index][3]))
        self.Phone_num_data.setText(str(self.mass[index][4]))

    def sort(self):
        if self.comboBox.currentIndex() == 0:
            self.mass = sorted(self.mass, key = lambda k: k[0]) #ID
        elif self.comboBox.currentIndex() == 1:
            self.mass = sorted(self.mass, key = lambda k: k[1]) #Surname
        elif self.comboBox.currentIndex() == 2:
            self.mass = sorted(self.mass, key = lambda k: k[2]) #Name
        elif self.comboBox.currentIndex() == 3:
            self.mass = sorted(self.mass, key = lambda k: k[3]) #Second_name

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

    def search(self):
        window_search = SearchWindow(self)
        window_search.show()






def main():
    app = QtWidgets.QApplication(sys.argv)
    window_main = MainWindow()
    window_main.show()
    app.exec_()

main()