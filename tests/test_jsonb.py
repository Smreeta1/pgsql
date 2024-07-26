from operations.insert import insert_data
from operations.db_connect import get_connection

conn = get_connection()

def test_insert_data(setup_table):
    table_name = setup_table

    # Data insertion
    initial_data = [
        ('Ram', '1970-01-01', 'ram@gmail.com', '1234567890', 'Kathmandu'),
        ('Shyam', '1990-12-10', 'shyam@gmail.com', '123123123', 'Lalitpur'),
        ('Krishna', '1980-05-15', 'krishna@gmail.com', '1231231234', 'PKR')
    ]
    insert_data(table_name, initial_data)

    try:
        with conn.cursor() as cur:
            # Retrieving all records from the table
            cur.execute(f"SELECT person_data FROM {table_name};")
            results = cur.fetchall()

            # Check if all inserted data is present
            person_data_list = [result[0] for result in results] 

            # Check if all initial data entries are present in the retrieved results
            for name, dob, email, phone, address in initial_data:
                assert any(
                    person_data['name'] == name and
                    person_data['dob'] == dob and
                    person_data['email'] == email and
                    person_data['phone'] == phone and
                    person_data['address'] == address
                    for person_data in person_data_list
                ), f"Data not found: {name}, {email}"
     
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
