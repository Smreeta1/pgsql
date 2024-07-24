from operations.db_connect import get_connection
conn = get_connection() 

def create_table(table_name):
    with conn.cursor() as cur:
        cur.execute(f"""
         CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            dob DATE NOT NULL,
            email VARCHAR(100),
            phone VARCHAR(20),
            address TEXT
        );
        """)
        conn.commit()
    conn.close()  # Close the connection after use
