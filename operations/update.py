from operations.db_connect import get_connection
def update_data(table_name,column, new_value, condition):
    conn = get_connection()
    cur = conn.cursor()
    update_table = f"""
    UPDATE {table_name}
    SET {column} = %s
    WHERE {condition};
    """
    cur.execute(update_table, (new_value,))
    conn.commit()
    cur.close()
    conn.close()