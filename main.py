import sys
import sqlite3 as sql
from PyQt5 import QtWidgets
import Main_Window
import Search_Window
import Edit_Window

class SearchWindow(QtWidgets.QMainWindow, Search_Window.Ui_MainWindow):
    def __init__(self, root):
        super().__init__(root)
        self.setup(self)
        self.main = root
        self.button_search.clicked.connect(self.search)
        self.table.cellDoubleClicked.connect(self.show_in_main)

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

        self.sort_table()

        if self.mass_search:
            names = list(map(lambda x: x[0], cursor.description))
            self.table.setColumnCount(len(self.mass_search[0]))
            self.table.setRowCount(len(self.mass_search))
            self.table.setHorizontalHeaderLabels(names)

            for i in range(len(self.mass_search)):
                for j in range(len(self.mass_search[i])):
                    self.table.setItem( i, j, QtWidgets.QTableWidgetItem(str(self.mass_search[i][j])) )
        else:
            self.table.clear()           

        cursor.close()
        connection.close()

    def sort_table(self):
        if self.comboBox.currentIndex() == 0:
            self.mass_search = sorted(self.mass_search, key = lambda k: k[0]) #ID
        elif self.comboBox.currentIndex() == 1:
            self.mass_search = sorted(self.mass_search, key = lambda k: k[1]) #Surname
        elif self.comboBox.currentIndex() == 2:
            self.mass_search = sorted(self.mass_search, key = lambda k: k[2]) #Name
        elif self.comboBox.currentIndex() == 3:
            self.mass_search = sorted(self.mass_search, key = lambda k: k[3]) #Second_name
        elif self.comboBox.currentIndex() == 4:
            self.mass_search = sorted(self.mass_search, key = lambda k: k[4]) #Phone_num        

    def show_in_main(self):
        row = self.table.currentRow()
        col = self.table.currentColumn()
        value = self.table.item(row, col)
        if value:
            a = -1
            ID = int(self.table.item(row, 0).text())
            for i in self.main.mass:
                a += 1
                if i[0] == ID:
                    self.main.link = a
            self.main.show_items(self.main.link)
            self.close()     

class MainWindow(QtWidgets.QMainWindow, Main_Window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Соответсвует индексу текущего пользоваетля из массива self.mass
        self.link = 0 
        self.read_db()
        self.show_items(self.link)
        self.button_sort.clicked.connect(self.sorted)
        self.button_next.clicked.connect(self.next)
        self.button_last.clicked.connect(self.last)
        self.button_search.clicked.connect(self.search)
        self.button_insert.clicked.connect(self.insert_db)
        self.button_delete.clicked.connect(self.delete)
        self.button_edit.clicked.connect(self.edit)

    def show_items(self, index):
        if len(self.mass) >= 1:
            self.ID_data.setText(str(self.mass[index][0]))
            self.Surname_data.setText(str(self.mass[index][1]))
            self.Name_data.setText(str(self.mass[index][2]))
            self.Second_name_data.setText(str(self.mass[index][3]))
            self.Phone_num_data.setText(str(self.mass[index][4])) 
        else:
            self.ID_data.setText('')
            self.Surname_data.setText('')
            self.Name_data.setText('')
            self.Second_name_data.setText('')
            self.Phone_num_data.setText('')

    def insert_db(self):
        surname = str(self.Surname_data.text()).strip()
        name = str(self.Name_data.text()).strip()
        second_name = str(self.Second_name_data.text()).strip()
        phone_num = str(self.Phone_num_data.text()).strip()
        new_row = [surname, name, second_name, phone_num]
        connection = sql.connect('data_base')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (surname, name, second_name, phone_num) VALUES (?, ?, ?, ?)', new_row)
        cursor.close()
        connection.commit()
        connection.close()
        self.read_db()
        self.link = 0
        self.show_items(self.link)

    def delete(self):
        connection = sql.connect('data_base')
        cursor = connection.cursor()
        if len(self.mass) >= 1:   
            ID = str(self.mass[self.link][0])
            cursor.execute('DELETE FROM users WHERE id = '+ ID +'')
            cursor.close()
            connection.commit()
            connection.close()        
            self.read_db()
            self.last()

    def read_db(self):
        connection = sql.connect('data_base')
        cursor = connection.cursor()
        self.mass = cursor.execute('SELECT * FROM users').fetchall()
        cursor.close()
        connection.close()

    def sort(self):
        if self.comboBox.currentIndex() == 0:
            self.mass = sorted(self.mass, key = lambda k: k[0]) #ID
        elif self.comboBox.currentIndex() == 1:
            self.mass = sorted(self.mass, key = lambda k: k[1]) #Surname
        elif self.comboBox.currentIndex() == 2:
            self.mass = sorted(self.mass, key = lambda k: k[2]) #Name
        elif self.comboBox.currentIndex() == 3:
            self.mass = sorted(self.mass, key = lambda k: k[3]) #Second_name
        elif self.comboBox.currentIndex() == 4:
            self.mass = sorted(self.mass, key = lambda k: k[4]) #Phone_num
        

    def sorted(self):
        self.sort()
        self.link = 0
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

    def edit(self):
        window_edit = EditWindow(self)
        window_edit.show()

class EditWindow(QtWidgets.QMainWindow, Edit_Window.Ui_MainWindow):
    def __init__(self, root):
        super().__init__(root)
        self.setup(self)
        self.main = root
        self.button_save.clicked.connect(self.save)
        self.button_close.clicked.connect(self.close)
        self.show_items(self.main.link)

    def show_items(self, index):
        if len(self.main.mass) >= 1:
            self.ID_edit.setText(str(self.main.mass[index][0]))
            self.Surname_edit.setText(str(self.main.mass[index][1]))
            self.Name_edit.setText(str(self.main.mass[index][2]))
            self.Second_name_edit.setText(str(self.main.mass[index][3]))
            self.Phone_num_edit.setText(str(self.main.mass[index][4])) 
        else:
            self.main.ID_edit.setText('')
            self.main.Surname_edit.setText('')
            self.main.Name_edit.setText('')
            self.main.Second_name_edit.setText('')
            self.main.Phone_num_edit.setText('')


    def save(self):
        ID = self.ID_edit.text().strip()
        surname = self.Surname_edit.text().strip()
        name = self.Name_edit.text().strip()
        second_name = self.Second_name_edit.text().strip()
        phone_num = self.Phone_num_edit.text().strip()
        new_row = [surname, name, second_name, phone_num]

        connection = sql.connect('data_base')
        cursor = connection.cursor()
        cursor.execute('UPDATE users SET (surname, name, second_name, phone_num) = (?, ?, ?, ?) where id = '+ ID +'', new_row)
        cursor.close()
        connection.commit()
        connection.close()

        self.main.read_db()
        self.main.show_items(self.main.link)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window_main = MainWindow()
    window_main.show()
    app.exec_()

if __name__ == '__main__':
    main()