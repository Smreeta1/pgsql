from operations.db_connect import get_connection,close_connection
from operations.insert import insert_data
from operations.create_table import create_table

def test_insert_into(setup_table):
    table_name = setup_table
    data = ['Ram', '1970-01-01', 'ram@gmail.com', '1234567890', 'Kathmandu']
    insert_data(table_name, data)
    
    # Check if data is inserted
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name} WHERE name = %s;", (data[0],))
    result = cur.fetchone()
    cur.close()
    conn.close()
    
    assert result is not None
    assert result[1] == data[0]  # Check name
    assert str(result[2]) == data[1]  # Check dob