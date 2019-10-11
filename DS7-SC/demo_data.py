import sqlite3

'''
Part 1 - Making and populating a Database
'''

# Open a connection to a new (blank) database file demo_data.sqlite3
conn = sqlite3.connect('demo_data.sqlite3')

# Make a cursor
curs = conn.cursor()

# Execute an appropriate CREATE TABLE statement to accept the above data (name the table demo)
create_table = """CREATE TABLE demo(
                    s VARCHAR(5),
                    x INT,
                    y INT,
                    PRIMARY KEY(s)
                    );"""

curs.execute(create_table)

# Write and execute appropriate INSERT INTO statements to add the data (as shown above) to the database
insert_values = """INSERT INTO demo (s, x, y)
                    VALUES
                    ('g', 3, 9),
                    ('v', 5, 7),
                    ('f', 8, 7);"""

curs.execute(insert_values)

# Make sure to commit() so your data is saved! The file size should be non-zero.
conn.commit()

# Count how many rows you have - it should be 3!
count_query = """SELECT COUNT(x)
                 FROM demo;"""

count_result = curs.execute(count_query)

print('Count how many rows you have')
print('There are',count_result.fetchall()[0][0],'rows in the table.')
print('='*80)

# How many rows are there where both x and y are at least 5?
rows_query = """SELECT COUNT(*)
                 FROM demo
                 WHERE x >= 5 AND y >= 5;"""

rows_result = curs.execute(rows_query )

print('How many rows are there where both x and y are at least 5?')
print('There are', rows_result.fetchall()[0][0],
      'rows where both x and y are at least 5.')
print('='*80)

# How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
y_query = """SELECT COUNT(DISTINCT y)
             FROM demo;"""

y_result = curs.execute(y_query )

print('How many unique values of y are there?')
print('There are', y_result.fetchall()[0][0], 'unique values of y.')
print('='*80)



'''
OUTPUT:

Count how many rows you have
There are 3 rows in the table.
================================================================================
How many rows are there where both x and y are at least 5?
There are 2 rows where both x and y are at least 5.
================================================================================
How many unique values of y are there?
There are 2 unique values of y.
================================================================================

'''
