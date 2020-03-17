# DS Unit 3 Sprint 2

## Class 1

> Hey @channel, tomorrow we'll begin our second sprint with an introduction to relational databases and SQL. To prepare for class, I recommend you:
>
>    1) Download this example sqlite database called "chinook" (https://www.sqlitetutorial.net/sqlite-sample-database/), which we'll use to practice SQL queries.
>
>    2) Optionally download and install this database management software called TablePlus (https://tableplus.com/) which will allow you to interface with Sqlite and PostgreSQL databases we'll be working with in this unit. FYI: TablePlus is my preferred / recommended tool these days, but you could always use alternative tools like DB Browser and/or PgAdmin instead, as referenced in the materials.
>
>    Heads-up: I'll share a lecture repo link before class tomorrow morning. See you then!

Lambda Material:

  + https://learn.lambdaschool.com/ds/module/recmwiPQG5zueKFCG/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module1-introduction-to-sql

DBMS Tool:

  + https://tableplus.com/

SQLite:

  + https://docs.python.org/3/library/sqlite3.html
  + https://kite.com/python/examples/3884/sqlite3-use-a-row-factory-to-access-values-by-column-name

Practice SQLite Database:

  + https://www.sqlitetutorial.net/sqlite-sample-database/
  + https://www.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf

Database Concept Notes (FYI / BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/conceptual-design.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/physical-design.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/entity-relationship-diagramming.md


SQL Notes (FYI / BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/best-practices.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/sql-style-guide.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/single-table-sql.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/single-table-aggregate-sql.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/multi-table-sql.md

### Part I - Single Table SQL

```sql
SELECT
    1 as first_col,
    2 as second_col,
    3,
    "hello" as my_message,
    2 * 10,
    6
```

```sql
-- who are our customers? (what are their names?)
SELECT
  CustomerId
  ,FirstName
  ,LastName
FROM customers
```

```sql
-- which customers are from the US?
SELECT
  CustomerId
  ,FirstName
  ,LastName
FROM customers
WHERE Country = "USA"
```

```sql
-- which customers are from the US?
SELECT
  CustomerId
  ,FirstName
  ,LastName
  ,Country
FROM customers
-- WHERE Country = "USA"
-- WHERE Country <> "USA"
-- WHERE Country = "USA" or Country = "United Kingdom"
WHERE Country in ("USA", "United Kingdom")
```

```sql
-- example of ORDER BY
SELECT
  *
FROM customers
WHERE Country in ("USA", "United Kingdom")
ORDER BY Country ASC, State DESC -- ASC is the default
```

### Part I (cont'd) - Single Table SQL w/ Aggregations

```sql
-- how many customers do we have?
SELECT
  -- count(*) as customer_count -- > 59
  -- count(CustomerId) as customer_count
  count(distinct CustomerId) as customer_count -- > 59
FROM customers
```

> NOTE: when using the GROUP BY clause, we specify our result set should have a "row per" all the attributes included in the GROUP BY clause.

> RULE OF THUMB: when using the GROUP BY clause, all selected attributes that are not included in the GROUP BY clause should be removed from the SELECT clause, or or aggregated in the SELECT clause

```sql
-- how many customers in each country?
SELECT
  Country
  ,count(distinct CustomerId) as customer_count -- > 59
FROM customers
GROUP BY Country
```

```sql
-- which 5 countries have the most customers?
SELECT
  Country
  ,count(distinct CustomerId) as customer_count -- > 59
FROM customers
GROUP BY Country
ORDER BY customer_count DESC
LIMIT 5
```

### Part II - Multi-Table SQL

![a venn diagram depicting the difference between inner and outer joins](https://www.ionos.com/digitalguide/fileadmin/DigitalGuide/Screenshots_2018/Outer-Join.jpg)

Taking an iterative approach to illustrate the difference between inner and outer (i.e. left) joins.

```sql
-- for each artist,
-- how many albums?
-- and how many tracks?
-- row per artist (275)
-- row per artist (204???)
SELECT
  artists.ArtistId
  ,artists.Name as ArtistName
  ,count(distinct albums.AlbumId) as AlbumCount
  ,count(distinct tracks.TrackId) as TrackCount
FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON tracks.AlbumId = albums.AlbumId
GROUP BY artists.ArtistId
```

Why are we losing some artists? Because not all artists have albums. Maintain original table by using an outer join:

```sql
-- for each artist,
-- how many albums?
-- and how many tracks?
-- row per artist (275)
SELECT
  artists.ArtistId
  ,artists.Name as ArtistName
  ,albums.AlbumId
  ,tracks.TrackId
FROM artists
LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
LEFT JOIN tracks ON tracks.AlbumId = albums.AlbumId
```

```sql
-- for each artist,
-- how many albums?
-- and how many tracks?
-- row per artist (275)
SELECT
  artists.ArtistId
  ,artists.Name as ArtistName
  ,count(distinct albums.AlbumId) as AlbumCount
  ,count(distinct tracks.TrackId) as TrackCount
FROM artists
LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
LEFT JOIN tracks ON tracks.AlbumId = albums.AlbumId
GROUP BY artists.ArtistId
```


### Part III - Executing SQL from Python

Executing an SQL query:

```py
import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = "SELECT * FROM customers;"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)
```

Iterating through all records in our results set:

```py
import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

#query = "SELECT * FROM customers;"
query = """
SELECT
  Country
  ,count(distinct CustomerId) as CustomerCount -- > 59
FROM customers
GROUP BY Country
ORDER BY CustomerCount DESC
LIMIT 5
"""

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)

for row in result2:
    print(type(row))
    print(row)
    print(row[0])
    print(row[1])
    print("-----")
```

Reference also ["app/chinook_queries.py"](/app/chinook_queries.py).

## Class 2

> To prepare for class, please sign up for an Elephant SQL account https://www.elephantsql.com/

Lambda Material:

  + https://learn.lambdaschool.com/ds/module/recSdx6IFkDxqgxGb/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module2-sql-for-analysis

PostgreSQL & Psycopg Docs:

  + https://www.psycopg.org/docs/
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/psycopg.md
  + https://www.postgresql.org/docs/9.5/datatype.html

Environment Variables:
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/environment-variables.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/modules/os.md#environment-variables
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/dotenv.md

Database Management SQL (FYI / BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-management/database-management-sql.md

Installing package dependencies:

```sh
# for Pipenv users:
pipenv install python-dotenv psycopg2-binary # NOTE: the "-binary"

# for conda users:
pip install pandas python-dotenv psycopg2
```

Reference ["app/elephant.py"](/app/elephant.py).

## Class 3

> To prepare for class, please sign up for a MongoDB Atlas account https://account.mongodb.com/

Lambda Material:

  + https://learn.lambdaschool.com/ds/module/rec3JRFsRH2yeALwS/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module3-nosql-and-document-oriented-databases

MongoDB Docs:

  + https://api.mongodb.com/python/current/tutorial.html
  + https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_one
  + https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_many
  + https://api.mongodb.com/python/current/tutorial.html#range-queries
  + https://docs.mongodb.com/manual/reference/operator/query/

Installing packages:

```sh
# for pipenv users:
pipenv install pymongo dnspython

# for conda users:
pip install pymongo dnspython
```

Reference ["app/mongo_prep.py"](/app/mongo_prep.py).

## Class 4

Lambda Material:

  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module4-acid-and-database-scalability-tradeoffs
  + https://learn.lambdaschool.com/ds/module/rec9c9nW20Sn6TBAO/
  + [Sprint Challenge](https://github.com/LambdaSchool/DS-Material/blob/master/unit3-data-engineering/sprint2-sql-and-databases/sprint-challenge/challenge.md)

Database Transactions and ACID Properties:

  + https://www.essentialsql.com/what-is-meant-by-acid/
  + https://www.techopedia.com/definition/23949/atomicity-consistency-isolation-durability-acid
  + https://pynative.com/python-mysql-transaction-management-using-commit-rollback/

Normalization Practice (FYI / BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/logical-design.md
  + https://docs.google.com/spreadsheets/d/1xZ98yXEieMtaWuVQh3lQjCuP5aIqhinQcnzbnux52tY/edit?usp=sharing

SQL Review:

  + https://www.w3schools.com/sql/sql_exercises.asp
