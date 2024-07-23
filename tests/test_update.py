import pytest
from operations.db_connect import get_connection
from operations.create_table import create_table
from operations.insert import insert_data
from operations.update import update_data

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
    
def test_update_data(setup_table):
    table = setup_table
    data = ['Hari', '1990-12-10', 'hari@gmail.com', '123123123', 'Lalitpur']
    insert_data(table, data)
    
    # Update data
    update_data(table,'email', 'hari.updated@gmail.com', "name = 'Hari'")
    
    # Verify updates
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table} WHERE name = %s;", ('Hari',))
    result = cur.fetchone()
    cur.close()
    conn.close()
    
    assert result is not None
    assert result[3] == 'hari.updated@gmail.com'  
