#! python2
import sqlite3
from os import path
dir=path.dirname(path.realpath(__file__))+"/"
db = sqlite3.connect(dir + 'database.db') 
cursor = db.cursor() #opens up singular connection threat to the database to run SQL transactions

#if this is set to true, then it runs all of our tests in sequence and ends the program without allowing user input
#if its false then the program runs in its intended state
testing_bool = False

#takes the fetched data and extracts the value of the output and converts it to a string
#if it fails it just returns the original item
def parseFetch(fetch):
	try:
		return str(fetch[0][0]).lower()
	except:
		return fetch

#hard coded table columns
location_cols = ['area','location','connections']
pokemon_cols = ['id','name','environment','percent','route']
#takes the inputs from the user determines whether a join is needed and converts to valid
#sql statements
def simpleselect(table, column, col_val,item):
	if (table == 'pokemon' and item.lower() in location_cols) or (table == 'position' and item.lower() in pokemon_cols):
		if table == 'pokemon':
			query = "select r."+item+" from tblPosition r, tblPokemon p where p.route=r.location and p."+column+"=\'"+col_val+"\';"
		else:	
			query = "select p."+item+" from tblPokemon p, tblPosition r where p.route=r.location and r."+column+"=\'"+col_val+"\';"
		
		
	else:
		query = "select " + item + " from tbl" + table + " where " + column + " like '" + col_val + "';"
		#print(query)
	return query

#the keys are the statements that are being run and the values are the expected outputs
testing = {
		"pokemon name Weedle area": "Kanto",
		"position location Route_11 name":"Drowzee",
		"pokemon name ekans id": 13,
		"pokemon name Weedle environment": "grass",
		"pokemon name Weedle route": "Route_2",
		"pokemon name Weedle percent": 0.15,
		"pokemon id 18 name": "weedle",
		"pokemon id 18 environment": "grass",
		"pokemon id 18 percent": 0.15,
		"pokemon id 18 route": "Route_2",
		"position location route_1 area": "Kanto",
		"position location route_1 connections": "pallet town <--> viridian city",
		"select r.area from tblPosition r, tblPokemon p where p.route=r.location and p.id=18;": "Kanto"
}

print("Welcome to Pokemon database!")
print("Enter help to get examples of statements")
print("Enter a blank line to exit.")

#testing_index keeps track of the index that you are accessing in the test_list
#which is the list of statements to test

test_index = 0
test_list = testing.keys()

#flag to tell loop to stop, if testing is on it will run all statements in the list,
#if testing is off it will run until the user tells it to stop
flag = True
buffer = ""
while flag:
	#if the buffer is empty then the system is ready for new input
	if buffer == "":
		line = ""
		#if testing is on then get new input from the list
		#if not then get new input from the command line interface
		if testing_bool:
			line = test_list[test_index]
			print("\nTest: " + line)
		else:
			line = raw_input()
		if line == "":
			break
		elif line.lower() == "test":
			testing_bool=True
			continue
		buffer += line
	# print("Query: "+ buffer)

	#if the query is a valid sql statement then run it and print the output
	#if not then attempt to parse it into sql using our function
	if sqlite3.complete_statement(buffer):
		try:
			#run commands through sql
			buffer = buffer.strip()
			cursor.execute(buffer)
			fetch = parseFetch(cursor.fetchall())

			#if testing is on then compare output to the values in the testing dictionary
			if testing_bool:
				print(fetch)
				if str(fetch) != str(testing[test_list[test_index]]).lower():
					print('TEST FAILED: Expected ' + str(testing[test_list[test_index]]) + \
						', got ' + str(fetch))
					f=raw_input()
				else:
					print("TEST PASSED")

				#increment the testing index for the list and if it is larger than the size of the list exit the loop
				test_index += 1
				if test_index >= len(test_list):
					testing_bool = False
			else:
				print(fetch)

		except sqlite3.Error as e:
			print("An error occurred:", e.args[0])

			#increment the testing index for the list and if it is larger than the size of the list exit the loop
			if testing_bool:
				test_index += 1
				if test_index >= len(test_list):
					flag = False

		buffer = ""
	else:
		#help info teaches you how to use the program
		if buffer == 'help':
			print('\nWelcome!')
			print('Each single table search follows the following conventions:\n' + \
						'    TableName ColumnName ItemName SearchItem\n' + \
						'\nSo an example would be: \n    pokemon name weedle id\n' + \
						'\nwhich would return the ID of 18.\n\n' + \
						'The TableNames are \'pokemon\' and \'position\'.\n' + \
						'Pokemon ColumnNames are ID, Name, Environment, Percent, Route\n' + \
						'Position ColumnNames are Area, Location, Connections\n\n' + \
						'Cross Table queries example: position location Route_11 name\nwhich returns the pokemon name Drowzee\n\n'+ \
						'Searches are not case sensitive.\nLocations must have an Underscore (i.e. Route_1)\nHave fun!\n')
			buffer = ""
		else:
			#split the buffer so that it each word can be read seperately
			split_buffer = buffer.split()
			#if it is 5 long then it must be the specific name of the thing you are searching for
			#has a space in it so this combines them together into one element in the list
			if len(split_buffer) == 5:
				new_list = []
				new_list.append(split_buffer[0])
				new_list.append(split_buffer[1])
				new_list.append(split_buffer[2] + ' ' + split_buffer[3])
				new_list.append(split_buffer[4])
				split_buffer = new_list
			#since all of our queries are 4 words long if it is not 4 words long, it cant understand it
			if len(split_buffer) == 4:
				buffer = simpleselect(split_buffer[0], split_buffer[1], split_buffer[2], split_buffer[3])
			else:
				print('Could not understand query, please retry')
				buffer = ""
