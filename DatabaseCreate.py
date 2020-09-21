import sqlite3
##db = sqlite3.connect('studentdb.db')
##cursor = db.cursor()
##cursor.execute('''
##CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT, 
##                      class TEXT, email TEXT unique, prep TEXT, content TEXT)
##''')
##db.commit()
##db.close()
##
##
##db = sqlite3.connect('tdb.db')
##cursor = db.cursor()
##cursor.execute('''
##CREATE TABLE teachers(id INTEGER PRIMARY KEY, name TEXT, 
##                      class TEXT, email TEXT unique, prep TEXT, content TEXT)
##''')
##db.commit()
##db.close()
##
##db = sqlite3.connect('adb.db')
##cursor = db.cursor()
##cursor.execute('''
##CREATE TABLE admins(id INTEGER PRIMARY KEY, name TEXT, 
##                      class TEXT, email TEXT unique)
##''')
##db.commit()
##db.close()
##
##
##
###################################################
##db = sqlite3.connect('studentdb.db')
##cursor = db.cursor()
##cursor.execute('''INSERT INTO students(name, class, email)
##                VALUES(?,?,?)''', ("Jake", "Compsci", "J@s")
##               )
##db.commit()
##db.close()












##db = sqlite3.connect('tdb.db')
##cursor = db.cursor()

##db = sqlite3.connect('tdb.db')
##cursor = db.cursor()
##cursor.execute('''INSERT INTO teachers(name, class, email)
##                VALUES(?,?,?)''', ("Jackie Macdonald", "Compsci", "J@C")
##               )
##db.commit()

##users_name = "Jackie Macdonald"
##cursor.execute('''SELECT id FROM teachers WHERE name=?''', (users_name,))
##result = cursor.fetchone()
##db.close()
##print(result)
