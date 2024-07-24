from operations.db_connect import get_connection
conn = get_connection() 

def drop_table(table_name):
     
    with conn.cursor() as cur:
        cur.execute(f"DROP TABLE IF EXISTS {table_name};")
        conn.commit()
   
