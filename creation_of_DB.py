import random as rd
import sqlite3 as sql
import os

file_path = 'H:/_My_Docs/Database/data_base'
if os.path.isfile(file_path):
    os.remove(file_path)

names = ['Егор', 'Данил', 'Андрей', 'Антон', 'Алексей']
surnames = ['Белявцев', 'Прошалыкин', 'Буткеев', 'Басюра', 'Агеев']
second_names = ['Сергеевич', 'Андреевичч', 'Витальевич', 'Тарасович', 'Павлович']
phone_nums = ['+79236357970', '+79234906581', '+79045743116', '+79236315984', '+79913720869']

users = [[surnames[i], names[i], second_names[i], phone_nums[i]] for i in range(len(names))]
print(users)

connection = sql.connect('data_base')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, surname VARCHAR, name VARCHAR, second_name VARCHAR, phone_num VARCHAR)')
cursor.executemany('INSERT INTO users (surname, name, second_name, phone_num) VALUES (?, ?, ?, ?)', users)

connection.commit()
