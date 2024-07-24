import pytest
from operations.db_connect import get_connection
from upsert.insert import upsert_data  # Import the upsert function
from operations.create_table import create_table

@pytest.fixture()
def setup_test_table():
    create_table('person')
    yield 'person'  # Return the test table name

def test_upsert_data(setup_test_table):
    table = setup_test_table
    
    # Test data
    data1 = ('Alice', '1990-05-15', 'alice@example.com', '1234567890', 'Wonderland')
    data2 = ('Alice', '1990-05-15', 'alice.updated@example.com', '0987654321', 'Wonderland')  # Updated email

    # Insert data
    upsert_data(table, data1)
    
    # Check if data is inserted
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table} WHERE name = %s;", ('Alice',))
    result = cur.fetchone()
    cur.close()
    conn.close()
    
    assert result is not None
    assert result[2] == 'alice@example.com'  # Check email from first insert

    # Update data
    upsert_data(table, data2)
    
    # Check if data is updated
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table} WHERE name = %s;", ('Alice',))
    result = cur.fetchone()
    cur.close()
    conn.close()
    
    assert result is not None
    assert result[2] == 'alice.updated@example.com'  # Check updated email
