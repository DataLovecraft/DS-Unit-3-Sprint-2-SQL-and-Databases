import os
import sqlite3

# Path to database
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "../data/", "rpg_db.sqlite3")

# Use sqlite3 to load and write queries to explore the data, and answer the following questions:
"""""
How many total Characters are there?
How many of each specific subclass?
How many total Items?
How many of the Items are weapons? How many are not?
How many Items does each character have? (Return first 20 rows)
How many Weapons does each character have? (Return first 20 rows)
On average, how many Items does each Character have?
On average, how many Weapons does each character have?
"""""

# Connecting to the database file
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "../data/", "rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()


db_query = '.tables '
db_results = curs.execute(db_query)
print(db_results)
#SHOW SCHEMAS



# How many total characters are there?
print('How many total characters are there?')
char_query = 'SELECT COUNT(*) FROM charactercreator_character'
char_results = curs.execute(char_query)
print('There are', char_results.fetchall()[0][0], 'total characters')


# How many of each specific subclass?
print('How many of each specifuc subclass')



# How many total items?
print('How many total items')



# how many of the items are weapons? How many are not?
print('How many of these items are weapons?')



print('How many are not?')

# How many items does each cahracter have? (Return first 20 rows)
i


# How many weapons does each character have? (Return first 20 rows)


# One average, how many items does each character have?



# One average, how many weapons does each character have?



conn.close()
