from operations.insert import insert_data
from operations.update import update_data
from operations.db_connect import get_connection
conn = get_connection()

def test_update_data(setup_table):
    table = setup_table
    data = ['Hari', '1990-12-10', 'hari@gmail.com', '123123123', 'Lalitpur']
    insert_data(table, data)
    
    # Update data
    update_data(table, 'email', 'hari.updated@gmail.com', "name = 'Hari'")
    
    with conn.cursor() as cur: 
           
        cur.execute(f"SELECT * FROM {table} WHERE name = %s;", ('Hari',))
        result = cur.fetchone()
        conn.commit()
        assert result is not None
        assert result[3] == 'hari.updated@gmail.com'
    
  
