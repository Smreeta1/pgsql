import pytest
from Basics.db_connect import get_connection
from Basics.create_tables import create_tables
from Basics.upsert_data import insert_or_update_data


@pytest.fixture(scope="function")
def db_transaction():
    conn = get_connection()
    cursor = conn.cursor()
    conn.autocommit = False

    yield cursor, conn
    
    # Rollback to clean up
    conn.rollback()
    cursor.close()
    conn.close()


def test_upsert_data(db_transaction):
    cursor, conn = db_transaction
    
    #no need for calling fxn: create_tables() if already created:duplicate error
    
    # Perform upsert operation
    insert_or_update_data(cursor)

    # Commit changes to see the updates
    conn.commit()

    # Verify the data in the authors table
    cursor.execute("SELECT * FROM authors WHERE author_id = 1")
    authors = cursor.fetchall()
    assert len(authors) == 1
    assert authors[0][1] == "MK Rowling"

    # Verify the data in the books table
    cursor.execute("SELECT * FROM books WHERE book_id = 2")
    books = cursor.fetchall()
    assert len(books) == 1
    assert books[0][1] == "ReadBook"
    assert books[0][2] == 1

    # Verify the data in the members table
    cursor.execute("SELECT * FROM members WHERE member_id = 5")
    members = cursor.fetchall()
    assert len(members) == 1
    assert members[0][1] == "Ram"
    assert str(members[0][0]) == "5"

    """
    library_db=# SELECT * FROM books;
 book_id |      title      | author_id
---------+-----------------+-----------
       3 | AnyBook         |         3
       1 | AnyBook AnyBook |         1
       2 | ReadBook        |         1
(3 rows)

library_db=# SELECT * FROM members;
 member_id |   name    | join_date
-----------+-----------+------------
         4 | Sita Sita | 2024-07-18
         5 | Ram       | 2024-07-18
(2 rows)

    """


def test_upsert_update_data(db_transaction):
    cursor, conn = db_transaction

    # Initial upsert operation
    # insert_or_update_data(cursor)

    # Commit changes to see the updates otherwise changes not seen in db
    # conn.commit()

    # Verify the initial data
    cursor.execute("SELECT * FROM authors WHERE author_id = 1")
    authors = cursor.fetchall()
    assert len(authors) == 1
    assert authors[0][1] == "MK Rowling"

    # upsert function
    # Perform upsert operation with updated data
    cursor.execute(
        """
    INSERT INTO authors (author_id, name, birthdate)
    VALUES (1, 'J.K.Rowling', '1965-07-31')
    ON CONFLICT (author_id) DO UPDATE
    SET name = EXCLUDED.name;
    """
    )

    # Commit changes to see the updates
    conn.commit()

    # Verify the updated data
    cursor.execute("SELECT * FROM authors WHERE author_id = 1")
    authors = cursor.fetchall()
    assert len(authors) == 1
    assert authors[0][1] == "J.K.Rowling"

    """
    Output:
    test_upsert_update_data(db_transaction):
        
       -->Before upsert function:
        
        library_db=# SELECT * FROM authors;
    author_id |    name    | birthdate
    -----------+------------+------------
            3 | GK Rowling | 1965-07-31
            1 | MK Rowling | 1965-07-31
    (2 rows)
    ------------------------------------------------
     --> After upsert function:

    library_db=# SELECT * FROM authors;
    author_id |    name     | birthdate
    -----------+-------------+------------
            3 | GK Rowling  | 1965-07-31
            1 | J.K.Rowling | 1965-07-31
    (2 rows)
"""
