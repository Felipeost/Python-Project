import logging
import pandas as pd
import sqlite3

class SqlTableManager:
    """
    A class for managing SQLite database operations, including table creation and 
    inserting data from a pandas DataFrame.
    """
    def __init__(self, db_name):
        """
        Initialize the connection to the SQLite database.
        :param db_name: The name of the SQLite database file.
        """
        self.db_name = db_name
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            logging.info(f"Connected to SQLite database: {self.db_name}")
        except sqlite3.Error as e:
            logging.error(f"Failed to connect to database: {e}")
            raise

    def create_table(self, table_name):
        """
        Creating SQL table if it does not already exist
        :param table_name: The name of the table to create.
        """
        
        try:
            # Define SQL command to create table
            create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                Year INTEGER,
                Kilometers_Driven INTEGER,
                Engine INTEGER,
                Power REAL,
                Fuel_Type TEXT,
                Transmission TEXT,
                Name TEXT,
                Location TEXT
            );
            """
            self.cursor.execute(create_table_sql)
            self.conn.commit()
            logging.info(f"Table '{table_name}' created or already exists.")
        except sqlite3.Error as e:
            logging.error(f"Failed to create table '{table_name}': {e}")
            raise


    def insert_data(self, df, table_name):
        """
        Insert the data from the DataFrame into the specified SQL table.
        :param df: DataFrame containing the data.
        :param table_name: Name of the SQL table.
        """
        try:
            df.to_sql(table_name, self.conn, if_exists='append', index=False)
            logging.info(f"Inserted {len(df)} rows into table '{table_name}'.")
        except Exception as e:
            logging.error(f"Failed to insert data into table '{table_name}': {e}")
            raise

    def close_connection(self):
        """Close the database connection."""
        try:
            self.conn.close()
            logging.info("Closed database connection.")
        except sqlite3.Error as e:
            logging.error(f"Error closing database connection: {e}")
            raise
