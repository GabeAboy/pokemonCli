import sqlite3
db = sqlite3.connect('C:/repos/UVM/PokemonDB.db')
cursor = db.cursor() #opens up singular connection threat to the database to run SQL transactions


# cursor.execute("SELECT * FROM tblPokemon;")
# print(cursor.fetchall())

buffer = ""

print "Enter your SQL commands to execute in sqlite3, include semicolon."
print "Enter a blank line to exit."

while True:
    line = raw_input()
    if line == "":
        break
    buffer += line
    print("Query: "+buffer)
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            print("Query: "+buffer)
            cursor.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print cursor.fetchall()
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
        buffer = ""
