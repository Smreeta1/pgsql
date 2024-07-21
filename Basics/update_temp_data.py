def update_temp_data(conn):
    cursor = conn.cursor()

    # Update data in the temporary authors table
    cursor.execute("""
    UPDATE temp_authors
    SET name = %s
    WHERE author_id = %s
    """, ("J.K. Rowling", 3))
    conn.commit()

    cursor.close()
    
    
    
    

