from operations.db_connect import get_connection
conn=get_connection()

def insert_data(table_name, data):
    with conn.cursor() as cur:
    
        insert_into = f"""
        INSERT INTO {table_name} (name, dob, email, phone, address) 
        VALUES (%s, %s, %s, %s, %s);
        """
        cur.execute(insert_into, data)
        conn.commit()

