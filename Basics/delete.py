import psycopg2
import os
from dotenv import load_dotenv

def delete_data():
    load_dotenv()

    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST')
    )
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM fine
    WHERE fine_id = %s
    """, (3,))  #record with fine_id = 3 will be permanently removed from the fine table

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    delete_data()
