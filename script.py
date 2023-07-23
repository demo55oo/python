import json
import pandas as pd
import sqlite3

def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def convert_json_to_sqlite(json_data):
    # Flatten the nested JSON data
    flattened_data = pd.json_normalize(json_data)

    # Convert data types to string (to handle various data types in JSON)
    flattened_data = flattened_data.astype(str)

    # Create an in-memory SQLite database
    conn = sqlite3.connect(":memory:")

    # Write the flattened data to SQLite
    flattened_data.to_sql('data_table', conn, index=False)

    # Create the target SQLite database file
    target_file = "sqlite.db"
    target_conn = sqlite3.connect(target_file)

    # Copy the data from the in-memory database to the target file
    conn.backup(target_conn)

    # Close the connections
    conn.close()
    target_conn.close()

    print("SQLite database file created as 'sqlite.db'")

if __name__ == '__main__':
    json_file_path = 'input.json'  # Change this to your JSON file's name if different

    # Read JSON data from the file
    json_data = read_json_from_file(json_file_path)

    # Convert JSON data to SQLite and save as 'sqlite.db'
    convert_json_to_sqlite(json_data)
