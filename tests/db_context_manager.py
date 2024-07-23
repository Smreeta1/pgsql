from operations.db_connect import get_connection

def with_connection_and_cursor(callback):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            callback(cur)
        conn.commit()
    finally:
        conn.close()
