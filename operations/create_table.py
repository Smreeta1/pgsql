import psycopg2
from operations.db_connect import get_connection

def create_table(table_name):
    conn = get_connection()
    cur = conn.cursor()
    create_table_stmt = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        dob DATE NOT NULL,
        email VARCHAR(100),
        phone VARCHAR(20),
        address TEXT
    );
    """
    cur.execute(create_table_stmt)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_table()  # Example call to create 'person' table
