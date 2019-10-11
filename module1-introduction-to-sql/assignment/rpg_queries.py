import sqlite

```
Use sqlite3 to load and write queries to explore the data, and answer the following questions:

How many total Characters are there?
How many of each specific subclass?
How many total Items?
How many of the Items are weapons? How many are not?
How many Items does each character have? (Return first 20 rows)
How many Weapons does each character have? (Return first 20 rows)
On average, how many Items does each Character have?
On average, how many Weapons does each character have?
```

# Connecting to the database file
sqlite_file = '../rpg_db.sqlite3'
conn = sqlite3.connect()
c = conn.cursor()

# How many total characters are there?
char_query = 'SELECT COUNT(*) FROM charactercreator_character'
char_results = curs.execute(char_query)
print('1, There are', char_results.fetchall()[0][0], 'total characters') 

conn.close()
