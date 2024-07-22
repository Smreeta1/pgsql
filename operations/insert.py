from operations.db_connect import get_connection
def insert_data(table_name, data):
    conn = get_connection()
    cur = conn.cursor()
    
    insert_into = f"""
    INSERT INTO {table_name} (name, dob, email, phone, address) 
    VALUES (%s, %s, %s, %s, %s);
    """
    
    cur.execute(insert_into, data)
    conn.commit()
    cur.close()
    conn.close()
