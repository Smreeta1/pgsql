import pytest
from Basics.db_connect import get_connection
from Basics.create_temp_tables import create_temp_tables
from Basics.insert_temp_data import insert_temp_data

@pytest.fixture(scope='function')
def db_transaction():
    conn = get_connection()
    cursor = conn.cursor()
    conn.autocommit = False 

    # Set up temporary tables and initial data
    create_temp_tables(conn)
    insert_temp_data(conn)

    yield cursor, conn 
    
    conn.rollback()  # Rollback the transaction after the test
    cursor.close()
    conn.close()

from Basics.delete_temp_data import delete_temp_data

def test_delete_data(db_transaction):
    cursor, conn = db_transaction

    # Call the delete function
    delete_temp_data(conn)

    # Verify the data is deleted
    cursor.execute("SELECT * FROM temp_authors WHERE author_id = 3")
    authors = cursor.fetchall()
    assert len(authors) == 0
