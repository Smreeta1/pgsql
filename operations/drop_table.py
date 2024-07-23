from operations.db_connect import get_connection

def drop_table(table_name):
    conn = get_connection()  #Obtain a new connection
    with conn.cursor() as cur:
        cur.execute(f"DROP TABLE IF EXISTS {table_name};")
        conn.commit()
    conn.close()  # Close the connection after use
