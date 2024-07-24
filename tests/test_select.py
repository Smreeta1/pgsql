from operations.db_connect import get_connection
from operations.insert import insert_data
from operations.select import select_data
conn=get_connection()

def test_select_data(setup_table):
    table = setup_table
    data = ['Shyam', '1980-05-15', 'shyam@gmail.com', '1231231231', 'Pokhara']
    insert_data(table, data)
    try:
        # Select data
        rows = select_data(table)
        assert len(rows) > 0
        assert any(row[1] == data[0] for row in rows)  # Check if 'Shyam' is in the result
    except Exception as e:
        conn.rollback()
        raise e