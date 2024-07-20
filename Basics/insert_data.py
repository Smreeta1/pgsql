from Basics.db_connect import get_connection

def insert_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert data into authors table
    cursor.execute("""
    INSERT INTO authors (author_id, name, birthdate) VALUES (%s, %s, %s)
    """, (3, "GK Rowling", "1965-07-31"))

    # Insert data into books table
    cursor.execute("""
    INSERT INTO books (book_id, title, author_id) VALUES (%s, %s, %s)
    """, (3, "AnyBook", 3))

    # Insert data into members table
    cursor.execute("""
    INSERT INTO members (member_id, name, join_date) VALUES (%s, %s, %s)
    """, (4, "Sita", "2024-07-18"))

    # Insert data into fine table
    cursor.execute("""
    INSERT INTO fine (book_id, member_id, amount, fine_date) VALUES (%s, %s, %s, %s)
    """, (3, 4, 10.00, "2024-07-18"))

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    insert_data()
