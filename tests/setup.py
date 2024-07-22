# import pytest
# from operations.db_connect import get_connection
# from operations import create_table

# @pytest.fixture(scope="function")
# def setup_table():
#     table_name = 'person_test'
#     create_table(table_name)
#     yield table_name
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(f"DROP TABLE IF EXISTS {table_name};")
#     conn.commit()
#     cur.close()
#     conn.close()
