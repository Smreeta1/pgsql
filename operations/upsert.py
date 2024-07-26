from psycopg2.extras import execute_batch
from operations.db_connect import get_connection
conn = get_connection()

#upsert for conflict on email column
def upsert_data(table_name,data):
    with conn.cursor() as cur:
        
            insert_into = f"""
            INSERT INTO {table_name} (name, dob, email, phone, address)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (email) DO UPDATE SET
            name = EXCLUDED.name,
            dob = EXCLUDED.dob,
            phone = EXCLUDED.phone,
            address = EXCLUDED.address;
            """
            execute_batch(cur,insert_into,data)
    conn.commit()