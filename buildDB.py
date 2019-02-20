import sqlite3
import csv
#DDL = data definition language - this is the definition of the table, therefore
	# we should keep it seperate from the program ALWAYS
#This program creates the database fields from scratch.
#Do not change except to update database


db = sqlite3.connect('database.db')
cursor = db.cursor() #opens up singular connection threat to the database to run SQL transactions


#If this is your first time running the program, comment out the following:
cursor.execute('''
	DROP TABLE IF EXISTS tblPosition
''')
cursor.execute('''
	DROP TABLE IF EXISTS tblPokemon
''')
#This is because the tables need to Exist first before they can be dropped.
#So comment them out, run the program, then uncomment them and run it again.

f = open('tblPosition.csv','r')
next(f, None)
reader = csv.reader(f)

#cursor.execue executes transactional commands through the connection opened by the cursor
#You can only do one command per cursor.execute
cursor.execute('''
	CREATE TABLE tblPosition(
						Area TEXT,
						Location_ID INTEGER PRIMARY KEY AUTOINCREMENT,
						Location TEXT,
						Connections TEXT)
''') #AUTOINCREMENT increases the value of that field 1,2,3,4... (guarenteed unique field for every insertion)

for row in reader:
    cursor.execute("INSERT INTO tblPosition (Area, Location, Connections) VALUES (?, ?, ?);", row)
f.close()


f = open('tblPokemon.csv','r')
next(f, None)
reader = csv.reader(f)

#The table with the foregin key has to go second so that the key knows what it is linking to
cursor.execute('''
	CREATE TABLE tblPokemon(
					
						Pokemon_Name TEXT,
						Location_ID INTEGER,
						Rate_Found TEXT,
						Route TEXT,
						FOREIGN KEY(Location_ID) REFERENCES tblPosition(Location_ID))
''')

for row in reader:
    cursor.execute("INSERT INTO tblPokemon (Pokemon_Name, Location_ID, Rate_Found, Route, Location_ID) VALUES (?, ?, ?, ?, ?);", row)
f.close()
db.commit #commits to the database (and ergo the file)
print("Verifing tblPokemon:")
cursor.execute('''SELECT * FROM tblPokemon''')
rows = cursor.fetchall()
for row in rows:
    print(row)
print("\n")
print("Verifying tblPosition:")
cursor.execute('''SELECT * FROM tblPosition''')
rows = cursor.fetchall()
for row in rows:
    print(row)
db.close #Like close file

print("Finished building database")
