import pandas as pd

# Snowflake connector libraries
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas


#Module to create the snowflake connection and return the connection objects
def create_connection():
   conn = snow.connect(user="HRISHIKESHWARRIER",
   password="Hrishigugegushneu@98",
   account="euyozkh-hvb31240",
   warehouse="COMPUTE_WH",
   database="DBT",
   schema="PUBLIC")
   cursor = conn.cursor()
   print('SQL Connection Created')
   return cursor,conn

# Module to truncate the table if exists. This will ensure duplicate load doesn't happen
def truncate_table():
   cur,conn=create_connection()
   sql_titles = "TRUNCATE TABLE IF EXISTS TITLES_RAW"
   sql_credits = "TRUNCATE TABLE IF EXISTS CREDITS_RAW"
   cur.execute(sql_titles)
   cur.execute(sql_credits)
   print('Tables truncated')

#Module to read csv file and load data in Snowflake. Table is created dynamically
def load_data():
   cur,conn=create_connection()
   titles_file = r"/Users/hrishikeshwarrier/Desktop/Hrishikesh/ProjectPro/dbt/Code/datasets/titles.csv" # <- Replace with your path.
   titles_delimiter = "," # Replace if you're using a different delimiter.
   credits_file=r"/Users/hrishikeshwarrier/Desktop/Hrishikesh/ProjectPro/dbt/Code/datasets/credits.csv"
   credits_delimiter=","

   titles_df = pd.read_csv(titles_file, sep = titles_delimiter)
   print("Titles file read")
   credits_df = pd.read_csv(credits_file, sep = titles_delimiter)
   print("Credits file read")

   write_pandas(conn, titles_df, "TITLES",auto_create_table=True)
   print('Titles file loaded')
   write_pandas(conn, credits_df, "CREDITS",auto_create_table=True)
   print('Credits file loaded')

   cur = conn.cursor()


   # Close your cursor and your connection.
   cur.close()
   conn.close()

print("Starting Script")
truncate_table()
load_data()



