def delete_temp_data(conn):
    cursor = conn.cursor()

    #1.delete dependent records from temp_fine
    cursor.execute("""
    DELETE FROM temp_fine WHERE book_id IN (
        SELECT book_id FROM temp_books WHERE author_id = %s
    )
    """, (3,))
    #
    #delete the record from temp_books
    cursor.execute("""
    DELETE FROM temp_books WHERE author_id = %s
    """, (3,))

    #delete the record from temp_authors
    cursor.execute("""
    DELETE FROM temp_authors WHERE author_id = %s
    """, (3,))

    conn.commit()
    cursor.close()
