import psycopg2
import os
from dotenv import load_dotenv
from Basics.db_connect import get_connection

def update_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Update the amount for a specific fine_id
    cursor.execute("""
    UPDATE fine
    SET amount = %s
    WHERE fine_id = %s
    """, (19.00, 30))  

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    update_data()
