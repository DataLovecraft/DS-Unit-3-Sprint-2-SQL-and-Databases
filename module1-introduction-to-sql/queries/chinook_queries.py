import os
import sqlite3

# Path to database
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "../data/", "chinook.db")


# First we create a `connection` object that represents the database
conn = sqlite3.connect(DB_FILEPATH)
print('CONNECTION:', conn)

# Then we create a `cursor` object and call its `excecute()` method to
# perform SQL commands
c = conn.cursor()
print('CURSOR', c)

query = """
SELECT
    trackid,
    name,
    bytes
FROM
    tracks
ORDER BY
    bytes DESC
LIMIT 10;
"""
result = c.execute(query).fetchall()
print("RESULTS: ", result)






