"""
Встроенный движок реляционных СУБД SQLite
"""
import sqlite3 

# Создаем соединение с БД
conn = sqlite3.connect('data.db') #.db , .sqlite, .sql, .bd
# Создаем ОБЪЕКТ интерфейса СУБД 
cur = conn.cursor()

"""
Первый запрос - создадим таблицу в нашей БД
"""
query_create = "CREATE TABLE IF NOT EXISTS books (id INTEGER, author TEXT, title TEXT, year INTEGER, number REAL)"
#Выполняем запрос
cur.execute(query_create)

"""
Второй запрос - добавим новую книгу в БД
"""
book1 = {"id" : 1, "author" : "JJ.Talkin", "title" : "LOTR", "year" : 1980, "number" : 5.0}
book2 = {"id" : 2, "author" : "Rawling", "title" : "HP:1", "year" : 1990, "number" : 4.99}

books = [book1, book2]

query_insert = "INSERT INTO books VALUES(?, ?, ?, ?, ?)"
#cur.execute(query_insert, (book["id"], book["author"], book["title"], book["year"], book["number"]))
#conn.commit()

for book in books:
    cur.execute(query_insert, (book["id"], book["author"], book["title"], book["year"], book["number"]))
conn.commit() # ЗАНИМАЕТ УЛЬТРА МНОГО ВРЕМЕНИ. Не более 10 000 запросов в кэше

"""
Третий запрос - чтение из БД
"""
query_select = "SELECT * FROM books"
for row in cur.execute(query_select):
    print(row)

print("\n\n######################AFTER DELETING##################\n\n")

"""
Четвертый запрос - удаление из БД
"""
query_delete = "DELETE FROM books WHERE id=1" # НИКОГДА НЕ ЗАБЫВАЙТЕ НАПИСАТЬ ФИЛЬТР : WHERE id = 10...
cur.execute(query_delete)
conn.commit()

query_select = "SELECT * FROM books"
for row in cur.execute(query_select):
    print(row)



"""
Пятый запрос - обновление существующих данных
"""
query_update = "UPDATE books SET year=2001 WHERE id=2"
cur.execute(query_update)
conn.commit()

"""
Не забудем в самом конце отключиться от БД
"""
conn.close()

