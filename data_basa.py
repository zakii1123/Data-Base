from random import *
import sqlite3 as sq 

conn = sq.connect("test.db")
cursor = conn.cursor()

cursor.execute('''SELECT * FROM games''')
data = cursor.fetchall()

data = tuple(data) #Все элементы из бд

lst = list(data) #Переведение в лист(хз зачем, но подумал так надо)

for item in lst:
    print(item, end ='\n')#Разделение всех элементов



