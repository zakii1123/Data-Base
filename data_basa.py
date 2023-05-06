from random import *
import sqlite3 as sq 

conn = sq.connect("test.db")
cursor = conn.cursor()

cursor.execute('''SELECT * FROM games''')
data = cursor.fetchall()

data = tuple(data) #Все элементы из бд

lst = list(data) #Переведение в лист(хз зачем, но подумал так надо)

# for item in lst:
#     print(item, end ='\n')#Разделение всех элементов

def recomend():
    item = list(choice(lst))
    tag = item[0]
    name = item[1]
    janr = item[2]
    year_of_create = item[3]
    creator = item[4]
    print(f'Рекомендация игры: {name}. Жанр: {janr}. Год выпуска: {year_of_create}. Создатели: {creator}.')

recomend()    
answer = input('Хотите изменить игру ? y/n: ')
answer = answer.lower()
if answer == 'y':
    recomend()
else: 
    print("Ok")
