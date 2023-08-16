import sqlite3

connection = sqlite3.connect("links.sqlite3")
cursor= connection.cursor()

for i in cursor.execute("select * from links").fetchall():
	print("-----------")
	print(i)
