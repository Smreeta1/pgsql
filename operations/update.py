from operations.db_connect import get_connection
def update_data(column, new_value, condition):
    conn = get_connection()
    cur = conn.cursor()
    update_table = f"""
    UPDATE person
    SET {column} = %s
    WHERE {condition};
    """
    cur.execute(update_table, (new_value,))
    conn.commit()
    cur.close()
    conn.close()