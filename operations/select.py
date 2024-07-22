from operations.db_connect import get_connection
def select_data(table_name):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute(f"SELECT * FROM {table_name};")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows