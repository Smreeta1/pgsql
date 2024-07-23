from operations.db_connect import get_connection

def delete_data_by_name(table_name, name):
    conn=get_connection()
    with conn.cursor() as cur:
        delete_data = f"""
        DELETE FROM {table_name}
        WHERE name = %s;
        """
        cur.execute(delete_data, (name,))
        conn.commit()
   