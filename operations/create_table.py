import psycopg2
from operations.db_connect import get_connection

def create_table(create_table):
    conn = get_connection()
    cur = conn.cursor()
    create_table = """
    CREATE TABLE IF NOT EXISTS person (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        dob DATE NOT NULL,
        email VARCHAR(100),
        phone VARCHAR(20),
        address TEXT
    );
    """
    cur.execute(create_table)
    conn.commit()
    cur.close()
    conn.close()
    
if __name__ == "__main__":
    create_table()

