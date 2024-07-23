from operations.db_connect import get_connection

def select_data(table_name):
    conn=get_connection()
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM {table_name};")
        rows = cur.fetchall()
        return rows
    