import os
import psycopg2
import pandas
from psycopg2.extras import execute_values
from dotenv import load_dotenv

# Load .env file for env vars, and add them to the env
load_dotenv()

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
print("FILE EXISTS?", os.path.isfile(CSV_PATH))


# Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare





#
DB_HOST = os.getenv("DB_HOST", default="Unknown Host")
DB_NAME = os.getenv("DB_NAME", default="Unknown DB Name")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="Incorrect Password")
DB_USER = os.getenv("DB_USER", default="Unknown User")

#
conn = psycopg2.connect( host=DB_HOST,
                         dbname=DB_NAME,
                         user=DB_USER,
                         password=DB_PASSWORD)
print("CONNECTION: ", conn)

#
curs = conn.cursor()
print("CURSOR: ", curs)


#Create table
create_query = """
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived int,
  pclass int,
  name varchar,
  sex varchar,
  age int,
  sib_spouse_count int,
  parent_child_count int,
  fare float8
);
"""
curs.execute(create_query)
conn.commit()


#
curs.execute("SELECT * from passengers;")
result = curs.fetchall()
print("PASSENGERS:", len(result))

# prepare csv

#df = pandas.read_csv(CSV_PATH)
#print(df.head())
#rows = list(df.itertuples(index=False, name=None))

# Load data into db using `INSERT INTO`

#insertion_query = """
#INSERT INTO passengers (
#    survived,
#    pclass,
#    name,
#    sex,
#    age,
#    sib_spouse_count,
#    parent_child_count,
#    fare
#    ) VALUES %s"""
#
#execute_values(curs, insertion_query, rows)
#df.to_sql(name="my_table", con=engine, if_exists="append", index=False)
#
# df = pandas.read_csv(CSV_FILEPATH)
# print(df.head())
#
# # rows should be a list of tuples
# # [
# #   ('A rowwwww', 'null'),
# #   ('Another row, with JSONNNNN', json.dumps(my_dict)),
# #   ('Third row', "3")
# # ]
# # h/t Jesus and https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.itertuples.html
# rows = list(df.itertuples(index=False, name=None))
# insertion_query = "INSERT INTO passengers (
#                                     survived,
#                                     pclass,
#                                     name,
#                                     sex,
#                                     age,
#                                     sib_spouse_count,
#                                     parent_child_count,
#                                     fare) VALUES %s"
# execute_values(cursor, insertion_query, rows)

if len(result) == 0:
    # INSERT RECORDS
    #CSV_FILEPATH = "data/titanic.csv"
    CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
    print("FILE EXISTS?", os.path.isfile(CSV_PATH))
    df = pandas.read_csv(CSV_PATH)
    print(df.head())
    # rows should be a list of tuples
    # [
    #   ('A rowwwww', 'null'),
    #   ('Another row, with JSONNNNN', json.dumps(my_dict)),
    #   ('Third row', "3")
    # ]
    # h/t Jesus and https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.itertuples.html
    rows = list(df.itertuples(index=False, name=None))
    insertion_query = "INSERT INTO passengers (survived, pclass, name, sex, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
    execute_values(curs, insertion_query, rows)
# ACTUALLY SAVE THE TRANSACTIONS
conn.commit()





# insert = """
# COPY %s FROM STDIN WITH
#                     CSV
#                     HEADER
#                     DELIMITER AS ','
# """
# file = open(CSV_PATH, "r")
# table = 'passengers'
# with conn.cursor() as cur:
#     cur.execute("truncate " + table + ";")
#     cur.copy_expert(sql=insert % table, file=file)
#     conn.commit()
#     cur.close()
#     conn.close()






# Load data into db using `copy_from()`
#with open(CSV_PATH, 'r') as f:
#    next(f)
#    curs.copy_from(f, "passengers", sep=",")
#    conn.commit()
#    print("Data copied")


#
#one = curs.fetchone()
#all = curs.fetchall()
#result = curs.fetchone()
#print("RESULT: ", result)

# save the transaction
conn.commit()

# close the connection
curs.close()
conn.close()
