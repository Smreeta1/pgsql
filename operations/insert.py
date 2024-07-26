from psycopg2.extras import execute_batch
from operations.db_connect import get_connection
import json

conn = get_connection()

def insert_data(table_name, data):
    with conn.cursor() as cur:
        insert_into = f"""
        INSERT INTO {table_name} (person_data)
        VALUES (%s);
        """
        # Prepare data for JSONB column
        data_format = [
            (
                json.dumps(
                    {
                        "name": name,
                        "dob": dob,
                        "email": email,
                        "phone": phone,
                        "address": address,
                    }
                ),
            )
            for name, dob, email, phone, address in data
        ]
    
        execute_batch(cur, insert_into, data_format)
        
    conn.commit()
