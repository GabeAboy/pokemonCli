import sqlite3
#DDL = data definition language - this is the definition of the table, therefore
	# we should keep it seperate from the program ALWAYS
#This program creates the database fields from scratch. 

db = sqlite3.connect('./pokemonDB')
cursor = db.cursor() #opens up singular connection threat to the database to run SQL transactions


#If this is your first time running the program, comment out the following:
cursor.execute(''' 
	DROP TABLE town
''')
cursor.execute('''
	DROP TABLE pokemon
''')
#This is because the tables need to Exist first before they can be dropped.
#So comment them out, run the program, then uncomment them and run it again.


#cursor.execue executes transactional commands through the connection opened by the cursor
#You can only do one command per cursor.execute
cursor.execute('''
	CREATE TABLE town(Route_ID integer primary key AUTOINCREMENT,
						Town_Name TEXT,
						Area Text)
''') #AUTOINCREMENT increases the value of that field 1,2,3,4... (guarenteed unique field for every insertion)

#The table with the foregin key has to go second so that the key knows what it is linking to
cursor.execute('''
	CREATE TABLE pokemon(
						Pokemon_ID integer primary key AUTOINCREMENT,
						Pokemon_Name TEXT,
						Location TEXT,
						Rate_Found TEXT,
						Route_ID integer,
						FOREIGN KEY(Route_ID) REFERENCES town(Route_ID)
						)
''')


#Prevents from puting two same-named pokemon in twice (no two pikachus)
cursor.execute('''
	CREATE UNIQUE INDEX pokemonUC on pokemon(Pokemon_Name);
''')
cursor.execute('''
	CREATE UNIQUE INDEX townUC on town(Town_Name);
''')

db.commit #commits to the database (and ergo the file)
db.close #Like close file