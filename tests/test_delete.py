from operations.insert import insert_data
from operations.delete import delete_data_by_name
from tests.db_context_manager import with_connection_and_cursor

def test_delete_data_by_name(setup_table):
    table = setup_table
    data = ['Gita', '1995-12-12', 'gita@gmail.com', '111222333', 'bkt']
    insert_data(table, data)
    
    # Delete data
    delete_data_by_name(table, 'Gita')
    
    def check_deletion(cur):
        cur.execute(f"SELECT * FROM {table} WHERE name = %s;", ('Gita',))
        result = cur.fetchone()
        assert result is None  # Check if data is deleted
    
    with_connection_and_cursor(check_deletion)
