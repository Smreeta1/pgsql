import pytest
from Basics.db_connect import get_connection
from Basics.delete import delete_data 

@pytest.fixture(scope='function')
def db_transaction():
    conn = get_connection()
    cursor = conn.cursor()
    conn.autocommit = False  

    # Record with fine_id = 3 must exist
    cursor.execute("""
    INSERT INTO fine (fine_id, book_id, member_id, amount, fine_date)
    VALUES (3, 3, 4, 10.00, '2024-07-18')
    """)
    conn.commit()

    yield cursor, conn  #cursor and connection to the test

    conn.rollback()  # Rollback to undo any changes made during the test
    cursor.close()
    conn.close()

def test_delete_data(db_transaction):
    cursor, conn = db_transaction

    # Ensure the initial state of the table
    cursor.execute("SELECT * FROM fine WHERE fine_id = 3")
    initial_fine = cursor.fetchone()
    assert initial_fine is not None
    assert initial_fine[3] == 10.00  # Check initial amount
    
    '''
        library_db=# SELECT * FROM fine WHERE fine_id = 3;
    fine_id | book_id | member_id | amount | fine_date
    ---------+---------+-----------+--------+------------
        3 |       3 |         4 |     10 | 2024-07-18
    (1 row)
    '''

    # Call the function to delete data
    delete_data()
    
    '''
        library_db=# SELECT * FROM fine WHERE fine_id = 3;
    fine_id | book_id | member_id | amount | fine_date
    ---------+---------+-----------+--------+-----------
    (0 rows)

    '''

    # Verify the deletion
    cursor.execute("SELECT * FROM fine WHERE fine_id = 3")
    deleted_fine = cursor.fetchone()
    assert deleted_fine is None  