def insert_or_update_data(cursor):
    cursor.execute("""
    INSERT INTO authors (author_id, name, birthdate)
    VALUES (1, 'MK Rowling', '1965-07-31')
    ON CONFLICT (author_id) DO UPDATE
    SET name = EXCLUDED.name, birthdate = EXCLUDED.birthdate;
    """)

    cursor.execute("""
    INSERT INTO books (book_id, title, author_id)
    VALUES (2, 'ReadBook', 1)
    ON CONFLICT (book_id) DO UPDATE
    SET title = EXCLUDED.title, author_id = EXCLUDED.author_id;
    """)

    cursor.execute("""
    INSERT INTO members (join_date, name, member_id)
    VALUES ('2024-07-18', 'Ram', 5)
    ON CONFLICT (member_id) DO UPDATE
    SET name = EXCLUDED.name, join_date = EXCLUDED.join_date;
    """)

def run_upsert():
    from Basics.db_connect import get_connection

    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        insert_or_update_data(cursor)
        conn.commit()  # Commit the transaction to save changes otherwise no updation is shown in db
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    run_upsert()


'''
Output:

library_db=# SELECT * FROM authors;
 author_id |    name    | birthdate
-----------+------------+------------
         3 | GK Rowling | 1965-07-31
         1 | MK Rowling | 1965-07-31
(2 rows)
...............................................
library_db=# SELECT * FROM books;
 book_id |      title      | author_id
---------+-----------------+-----------
       3 | AnyBook         |         3
       1 | AnyBook AnyBook |         1
       2 | ReadBook        |         1
(3 rows)
.................................................
library_db=# SELECT * FROM members;
 member_id |   name    | join_date
-----------+-----------+------------
         4 | Sita Sita | 2024-07-18
         5 | Ram       | 2024-07-18
(2 rows)


'''