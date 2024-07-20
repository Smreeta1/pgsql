import psycopg2
import os
from dotenv import load_dotenv

def get_connection():
    load_dotenv()

    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST')
    )
    return conn
