import pytest
from Basics.db_connect import get_connection
from Basics.update_table import update_data 

@pytest.fixture(scope='function')
def db_transaction():
    conn = get_connection()
    cursor = conn.cursor()
    conn.autocommit = False  # To Disable autocommit to manage transactions manually
    
    yield cursor, conn  # To Provide the cursor and connection to the test
    
    conn.rollback()  # Rollback the transaction after the test
    cursor.close()
    conn.close()

def test_update_data(db_transaction):
    cursor, conn = db_transaction
    
    # Ensure the initial state of the table
    cursor.execute("SELECT * FROM fine WHERE fine_id = 30")
    initial_fine = cursor.fetchone()
    assert initial_fine is not None
    assert initial_fine[3] == 16.00  # Checking initial amount

    # Call the function to update data but doesn't commit its changes
    update_data()   
    
    # Verify the changes
    cursor.execute("SELECT * FROM fine WHERE fine_id = 30")
    updated_fine = cursor.fetchone()
    assert updated_fine is not None
    assert updated_fine[3] == 19.00  #updated amount


