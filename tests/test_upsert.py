# test_upsert.py
from operations.upsert import upsert_data
from operations.db_connect import get_connection
conn = get_connection()

#nserting new rows and updating existing rows based on the email column conflict.
def test_upsert_data(setup_table):
    table_name = setup_table
    initial_data = [
        ('Ram', '1970-01-01', 'ram@gmail.com', '1234567890', 'Kathmandu'),
        ('Hari', '1990-12-10', 'hari@gmail.com', '123123123', 'Lalitpur'),
        ('krishna', '1980-05-15', 'Krishna@gmail.com', '1231231234', 'PKR')
    ]
    upsert_data(table_name, initial_data)
    
    # Data to upsert (update existing and insert new)
    new_data = [
        ('Ram', '1970-01-01', 'ram@gmail.com', '0987654321', 'Bhaktapur'), #Duplicate email
        ('Shyam', '1980-05-15', 'shyam@gmail.com', '1231231231', 'Pokhara'),#non duplicate--will insert as new
        ('krishna', '1980-05-15', 'Krishna@gmail.com', '123456789', 'BRT') #Duplicate email
    ]
    upsert_data(table_name, new_data)
    
    with conn.cursor() as cur:
        # Check if 'Ram' is updated
        cur.execute(f"SELECT * FROM {table_name} WHERE email = %s;", ('ram@gmail.com',))
        result = cur.fetchone()
        assert result is not None
        assert result[1] == 'Ram'
        assert result[5] == 'Bhaktapur'  # Check updated address
        assert result[4] == '0987654321'  # Check updated phone
        
        # Check if 'Shyam' is inserted
        cur.execute(f"SELECT * FROM {table_name} WHERE email = %s;", ('shyam@gmail.com',))
        result = cur.fetchone()
        assert result is not None
        assert result[1] == 'Shyam'
        assert result[5] == 'Pokhara'
        
         # Check if 'Krishna' is updated
        cur.execute(f"SELECT * FROM {table_name} WHERE email = %s;", ('Krishna@gmail.com',))
        result = cur.fetchone()
        assert result is not None
        # assert result[1] == 'Krishna'
        assert result[5] == 'BRT'  #Check updated address
        assert result[4] == '123456789'  #Check updated phone
        
        conn.commit()
