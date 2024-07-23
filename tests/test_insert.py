from operations.insert import insert_data
from tests.db_context_manager import with_connection_and_cursor

def test_insert_into(setup_table):
    table_name = setup_table
    data = ['Ram', '1970-01-01', 'ram@gmail.com', '1234567890', 'Kathmandu']
    insert_data(table_name, data)
    
    def check_data(cur):
        cur.execute(f"SELECT * FROM {table_name} WHERE name = %s;", (data[0],))
        result = cur.fetchone()
        assert result is not None
        assert result[1] == data[0]  # Check name
        assert str(result[2]) == data[1]  # Check dob
    
    with_connection_and_cursor(check_data)
