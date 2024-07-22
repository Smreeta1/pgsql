import pytest
from operations.db_connect import get_connection
from operations.insert import insert_data
from operations.create_table import create_table

@pytest.fixture()
def setup_table():
    table_name = 'person_test'
    
    # Drop the table if it exists
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {table_name};")
    conn.commit()
    cur.close()
    conn.close()
    
    # Create the table
    create_table(table_name)
    
    yield table_name

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
