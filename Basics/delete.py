from Basics.db_connect import get_connection

def delete_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM fine
    WHERE fine_id = %s
    """, (3,))  #record with fine_id = 3 will be permanently removed from the fine table

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    delete_data()
