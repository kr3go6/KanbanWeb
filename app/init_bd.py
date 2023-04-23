import sqlite3

connection = sqlite3.connect('kanban.db')

with open('models.sql') as f:
    connection.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO users (nickname) VALUES ('test')")
# cur.execute("INSERT INTO kanbans (uid, type, content) VALUES (1, 'todo', 'open window')")

# connection.commit()
connection.close()