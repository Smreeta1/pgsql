def insert_temp_data(conn):
    cursor = conn.cursor()

    # Insert data into temporary authors table
    cursor.execute("""
    INSERT INTO temp_authors (author_id, name, birthdate) VALUES (%s, %s, %s)
    """, (3, "GK Rowling", "1965-07-31"))

    # Insert data into temporary books table
    cursor.execute("""
    INSERT INTO temp_books (book_id, title, author_id) VALUES (%s, %s, %s)
    """, (3, "AnyBook", 3))

    # Insert data into temporary members table
    cursor.execute("""
    INSERT INTO temp_members (member_id, name, join_date) VALUES (%s, %s, %s)
    """, (4, "Sita", "2024-07-18"))

    # Insert data into temporary fine table
    cursor.execute("""
    INSERT INTO temp_fine (book_id, member_id, amount, fine_date) VALUES (%s, %s, %s, %s)
    """, (3, 4, 10.00, "2024-07-18"))

    # Commit the changes
    conn.commit()
    cursor.close()
