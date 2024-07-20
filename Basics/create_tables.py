from Basics.db_connect import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE authors (
        author_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        birthdate DATE
    );
    """)

    cursor.execute("""
    CREATE TABLE books (
        book_id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        author_id INTEGER REFERENCES authors(author_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE members (
        member_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        join_date DATE
    );
    """)

    cursor.execute("""
    CREATE TABLE fine (
        fine_id SERIAL PRIMARY KEY,
        book_id INTEGER REFERENCES books(book_id),
        member_id INTEGER REFERENCES members(member_id),
        amount FLOAT NOT NULL,
        fine_date DATE
    );
    """)

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_tables()
