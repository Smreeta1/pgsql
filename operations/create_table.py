from operations.db_connect import get_connection

conn = get_connection()

def create_table(table_name):
    with conn.cursor() as cur:
        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                person_data JSONB NOT NULL
            );
        """)
    conn.commit()
