import pytest
from Basics.db_connect import get_connection
from Basics.create_temp_tables import create_temp_tables

@pytest.fixture(scope='function')
def db_transaction():
    conn = get_connection()
    cursor = conn.cursor()
    conn.autocommit = False 

    # Set up temporary tables
    create_temp_tables(conn)

    yield cursor, conn 

    conn.rollback()  # Rollback the transaction after the test
    cursor.close()
    conn.close()

def test_temp_tables_creation(db_transaction):
    cursor, conn = db_transaction

    # Check if temp_authors table exists and has the correct columns
    cursor.execute("""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'temp_authors'
    """)
    columns = [row[0] for row in cursor.fetchall()]
    assert 'author_id' in columns
    assert 'name' in columns
    assert 'birthdate' in columns

    # Check if temp_books table exists and has the correct columns
    cursor.execute("""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'temp_books'
    """)
    columns = [row[0] for row in cursor.fetchall()]
    assert 'book_id' in columns
    assert 'title' in columns
    assert 'author_id' in columns

    # Check if temp_members table exists and has the correct columns
    cursor.execute("""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'temp_members'
    """)
    columns = [row[0] for row in cursor.fetchall()]
    assert 'member_id' in columns
    assert 'name' in columns
    assert 'join_date' in columns

    # Check if temp_fine table exists and has the correct columns
    cursor.execute("""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'temp_fine'
    """)
    columns = [row[0] for row in cursor.fetchall()]
    assert 'fine_id' in columns
    assert 'book_id' in columns
    assert 'member_id' in columns
    assert 'amount' in columns
    assert 'fine_date' in columns

   