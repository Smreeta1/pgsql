from operations.db_connect import get_connection

def upsert_data(table_name, data):
    conn = get_connection()
    cur = conn.cursor()
    
    upsert_query = f"""
    INSERT INTO {table_name} (name, dob, email, phone, address) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (name)  -- Assuming 'name' is a unique key or constraint
    DO UPDATE SET
        dob = EXCLUDED.dob,
        email = EXCLUDED.email,
        phone = EXCLUDED.phone,
        address = EXCLUDED.address;
    """
    
    cur.execute(upsert_query, data)
    conn.commit()
    cur.close()
    conn.close()
    
# For both:Conflict on the combination of 'id' and 'email'
# CONSTRAINT unique_id_email UNIQUE (id, email)  -- modify this-Composite Unique Constraint in create_table.py

# def upsert_data_id_email(table_name, data):
#     conn = get_connection()
#     cur = conn.cursor()
    
#     upsert_query = f"""
#     INSERT INTO {table_name} (id, name, dob, email, phone, address) 
#     VALUES (%s, %s, %s, %s, %s, %s)
#     ON CONFLICT (id, email)  -- Conflict on the combination of 'id' and 'email'
#     DO UPDATE SET
#         name = EXCLUDED.name,
#         dob = EXCLUDED.dob,
#         phone = EXCLUDED.phone,
#         address = EXCLUDED.address;
#     """
    
#     cur.execute(upsert_query, data)
#     conn.commit()
#     cur.close()
#     conn.close()

