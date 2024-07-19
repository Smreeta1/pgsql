import psycopg2
import os
from dotenv import load_dotenv

def insert_data():
    load_dotenv()
    
    dbname = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host
    )
    cursor = conn.cursor()

    # Insert data into authors table
    cursor.execute("""
    INSERT INTO authors (author_id,name, birthdate) VALUES (%s,%s, %s)
    """, (2,"GK Rowling", "1965-07-31"))

    # Insert data into books table
    # author_id should match an existing ID.
    cursor.execute("""
    INSERT INTO books (book_id,title, author_id) VALUES (%s,%s, %s)
    """, (2,"AnyBook", 2))

    # Insert data into members table
    cursor.execute("""
    INSERT INTO members (member_id,name, join_date) VALUES (%s,%s, %s)
    """, (4,"Sita", "2024-07-18"))

    # Insert data into fine table
    # book_id and member_id should match existing IDs.
    cursor.execute("""
    INSERT INTO fine (book_id, member_id, amount, fine_date) VALUES (%s, %s, %s, %s)
    """, (1, 4, 10.00, "2024-07-18"))

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    insert_data()
