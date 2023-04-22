import sqlite3

connection = sqlite3.connect('kanban.db')

with open('models.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (nickname) VALUES ('test')")

connection.commit()
connection.close()