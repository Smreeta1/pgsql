import pytest
from operations.create_table import create_table
from operations.drop_table import drop_table
from operations.db_connect import get_connection

@pytest.fixture()
def setup_table():
    table_name = 'person_test'
    get_connection()
    
    # Drop the table if it exists
    drop_table(table_name)
    
    create_table(table_name)
    yield table_name
    
    # Cleanup after test
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            drop_table(table_name)
            conn.commit()
    finally:
        conn.close()
   
