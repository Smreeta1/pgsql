def create_temp_tables(conn):
    cursor = conn.cursor()

    # Create temporary tables
    cursor.execute("""
    CREATE TEMPORARY TABLE temp_authors (
        author_id INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        birthdate DATE
    );
    """)

    cursor.execute("""
    CREATE TEMPORARY TABLE temp_books (
        book_id INTEGER PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        author_id INTEGER REFERENCES temp_authors(author_id)
    );
    """)

    cursor.execute("""
    CREATE TEMPORARY TABLE temp_members (
        member_id INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        join_date DATE
    );
    """)

    cursor.execute("""
    CREATE TEMPORARY TABLE temp_fine (
        fine_id SERIAL PRIMARY KEY,
        book_id INTEGER REFERENCES temp_books(book_id),
        member_id INTEGER REFERENCES temp_members(member_id),
        amount FLOAT NOT NULL,
        fine_date DATE
    );
    """)

    # Commit the changes
    conn.commit()
    cursor.close()
