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


def test_insert_data(db_transaction):
    cursor, conn = db_transaction
    
    # Verify the data in the temporary authors table
    cursor.execute("SELECT * FROM temp_authors WHERE author_id = 3")
    authors = cursor.fetchall()
    assert len(authors) == 1
    assert authors[0][1] == "GK Rowling"
    
    # Verify the data in the temporary books table
    cursor.execute("SELECT * FROM temp_books WHERE book_id = 3")
    books = cursor.fetchall()
    assert len(books) == 1
    assert books[0][1] == "AnyBook"
    assert books[0][2] == 3
    
    # Verify the data in the temporary members table
    cursor.execute("SELECT * FROM temp_members WHERE member_id = 4")
    members = cursor.fetchall()
    assert len(members) == 1
    assert members[0][1] == "Sita"
    
    # Verify the data in the temporary fine table
    cursor.execute("SELECT * FROM temp_fine WHERE book_id = 3 AND member_id = 4")
    fines = cursor.fetchall()
    assert len(fines) == 1
    assert fines[0][3] == 10.00
    
    
