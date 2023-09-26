import sqlite3
import os
from db_interaction import connect_to_db, create_table, insert_data, read_data

def test_db_interaction():
    # Ensure clean slate
    if os.path.exists("test.db"):
        os.remove("test.db")

    conn, cursor = connect_to_db("test.db")
    create_table(cursor)
    
    insert_data(cursor, "Test User", 29)
    data = read_data(cursor)
    assert data == [(1, "Test User", 29)]

    conn.close()

if __name__ == "__main__":
    test_db_interaction()
    print("All tests passed!")
