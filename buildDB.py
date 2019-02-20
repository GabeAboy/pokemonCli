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
#This opens the csv tblPosition and reads the data into the array 2D reader.
#This will be used populate the database later on.

#cursor.execue executes transactional commands through the connection opened by the cursor
#You can only do one command per cursor.execute
cursor.execute('''
	CREATE TABLE tblPosition(
						Area TEXT,
						Location TEXT PRIMARY KEY,
						Connections TEXT)
''') #AUTOINCREMENT increases the value of that field 1,2,3,4... (guarenteed unique field for every insertion)

for row in reader:
    cursor.execute("INSERT INTO tblPosition (Area, Location, Connections) VALUES (?, ?, ?);", row)
f.close()
db.commit()
#This is where we take the 2D reader array and insert each dimension as a row into the tblPosition


f = open('tblPokemon.csv','r')
next(f, None)
reader = csv.reader(f)
#This opens the csv tblPokemon and reads the data into the array 2D reader.
#This will be used populate the database later on.


#The table with the foregin key has to go second so that the key knows what it is linking to
cursor.execute('''
	CREATE TABLE tblPokemon(
					
						Name TEXT,
						Location TEXT,
						Percent TEXT,
                                                Route TEXT,
						FOREIGN KEY(ROUTE) REFERENCES tblPosition(ROUTE))
''')

for row in reader:
    cursor.execute("INSERT INTO tblPokemon (Name, Location, Percent, Route) VALUES (?, ?, ?, ?);", row)
f.close()
#This is where we take the 2D reader array and insert each dimension as a row into the tblPosition

db.commit() #commits to the database (and ergo the file)

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
db.close() #Like close file

print("Finished building database")
