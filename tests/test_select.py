import pytest
from operations.db_connect import get_connection
from operations.insert import insert_data
from operations.create_table import create_table
from operations.select import select_data

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

def test_select_data(setup_table):
    table = setup_table
    data = ['Shyam', '1980-05-15', 'shyam@gmail.com', '1231231231', 'Pokhara']
    insert_data(table, data)
    
    # Select data
    rows = select_data(table)
    
    assert len(rows) > 0
    assert any(row[1] == data[0] for row in rows)  # Check if 'Shyam' is in the result
