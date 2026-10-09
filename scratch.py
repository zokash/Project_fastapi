import psycopg
import os
from dotenv import load_dotenv
from psycopg.rows import dict_row


load_dotenv()

with psycopg.connect(
    dbname = os.environ["DB_NAME"], 
    user = os.environ["USER"] ,
    password = os.environ["PASSWORD"], 
    row_factory=dict_row
) as conn:
    print("connected")

    #establishing a cursor to perforn db operations
    with conn.cursor() as cur:

        #inserting a record into companies 
        try:
            cur.execute("INSERT INTO companies(company_name, service_type,address) VALUES (%s, %s, %s)",('Uber', 'Delivery Services', 'Hyderabad'))
        except psycopg.errors.UniqueViolation as e:
            print("the Company already exists")
            conn.rollback()


        #executing a select command
        cur.execute("SELECT * FROM companies")
        #print("using fetchone:\n",cur.fetchone())

        print("using fetchall:\n", cur.fetchall())
        #print("using fetchall:\n", cur.fetchall())
        #noticed that the first print prints only one record (first record) and second print prints all records but starting from 2nd record. suspecting a pointer that starts from the start of the table when cur.execute and keeps on incrementing with all print statements below it. last print prints an empty list hence proved.
        #input("paused")
        conn.commit()
        

