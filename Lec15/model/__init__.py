import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

query_create = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT)'
cur.execute(query_create)

conn.close()