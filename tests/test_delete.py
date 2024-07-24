from operations.insert import insert_data
from operations.delete import delete_data_by_name
from operations.db_connect import get_connection

conn = get_connection()

def test_delete_data_by_name(setup_table):
    table = setup_table
    data = ['Gita', '1995-12-12', 'gita@gmail.com', '111222333', 'bkt']
    insert_data(table, data)
    
    # Delete data
    delete_data_by_name(table, 'Gita')
    try:
        with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM {table} WHERE name = %s;", ('Gita',))
                result = cur.fetchone()
                conn.commit()
                assert result is None  # Check if data is deleted
    except Exception as e:
        conn.rollback()
        raise e
