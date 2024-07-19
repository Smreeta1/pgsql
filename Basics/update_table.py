import psycopg2
import os
from dotenv import load_dotenv

def update_data():
    load_dotenv()

    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST')
    )
    cursor = conn.cursor()

    # Update the amount for a specific fine_id
    cursor.execute("""
    UPDATE fine
    SET amount = %s
    WHERE fine_id = %s
    """, (15.00, 2))  

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    update_data()
