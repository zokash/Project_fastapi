import psycopg
import os
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()

def get_conn():
    return psycopg.connect(  # noqa: SIM117
            dbname = os.environ["DB_NAME"],
            user = os.environ["USER"],
            password = os.environ["PASSWORD"],
            row_factory=dict_row
        )

def get_key():
    return os.environ["API_KEY"]