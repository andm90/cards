import sqlite3

db = sqlite3.connect('Winners.db') 

db.execute('''CREATE TABLE winners
             (name TEXT, points INTEGER)''')


db.close()