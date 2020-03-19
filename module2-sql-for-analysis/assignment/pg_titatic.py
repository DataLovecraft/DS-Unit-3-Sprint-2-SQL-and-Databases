import os
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

# Load .env file for env vars, and add them to the env
load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="Unknown Host")
DB_NAME = os.getenv("DB_HOST", default="Unknown DB Name")
DB_PASSWORD = os.getenv("DB_HOST", default="Incorrect Password")
DB_USER = os.getenv("DB_HOST", default="Unknown User")

conn = psycopg2.connect( host=DB_HOST,
                         dbname=DB_NAME,
                         user=DB_USER,
                         password=DB_PASSWORD)
print("CONNECTION: ", conn)


curs = conn.cursor()
print("CURSOR: ", curs)

curs.execute("SELECT * ; ")


result = curs.fetchone()
print("RESULT: ", result)
