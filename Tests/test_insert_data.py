import pytest
from Basics.db_connect import get_connection
from Basics.insert_data import insert_data

@pytest.fixture(scope='function')
def db_transaction():
    conn = get_connection()
    cursor = conn.cursor()
    conn.autocommit = False 
    
    yield cursor, conn 
    
    conn.rollback()  # Rollback the transaction after the test
    cursor.close()
    conn.close()

def test_insert_data(db_transaction):
    cursor, conn = db_transaction
    
    #function call to insert data
    insert_data()
    
    # Verify the data in the authors table
    cursor.execute("SELECT * FROM authors WHERE author_id = 3")
    authors = cursor.fetchall()
    assert len(authors) == 1
    assert authors[0][1] == "GK Rowling"
    
    # Verify the data in the books table
    cursor.execute("SELECT * FROM books WHERE book_id = 3")
    books = cursor.fetchall()
    assert len(books) == 1
    assert books[0][1] == "AnyBook"
    assert books[0][2] == 3
    
    # Verify the data in the members table
    cursor.execute("SELECT * FROM members WHERE member_id = 4")
    members = cursor.fetchall()
    assert len(members) == 1
    assert members[0][1] == "Sita"
    
    # Verify the data in the fine table
    cursor.execute("SELECT * FROM fine WHERE book_id = 3 AND member_id = 4")
    fines = cursor.fetchall()
    assert len(fines) == 1
    assert fines[0][3] == 10.00
