import unittest
import sqlite3
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sql_table_manager import SqlTableManager

class TestSqlTableManager(unittest.TestCase):

    def setUp(self):
        # Setting up test database and table
        self.db_name = "test_car_data.db"
        self.table_name = "cars"
        self.db_manager = SqlTableManager(self.db_name)
        self.df = pd.DataFrame({
            "Year": [2010, 2015],
            "Kilometers_Driven": [30000, 50000],
            "Engine": [1200, 1500],
            "Power": [85.0, 100.0],
            "Fuel_Type": ["PETROL", "DIESEL"],
            "Transmission": ["MANUAL", "AUTOMATIC"],
            "Name": ["CARA", "CARB"],
            "Location": ["CITYA", "CITYB"]
        })

        self.db_manager.create_table(self.table_name)
        self.db_manager.cursor.execute(f"DELETE FROM {self.table_name}")
        self.db_manager.conn.commit()

    def test_create_table(self):
        self.assertTrue(self.check_table_exists())

    def test_insert_data(self):
        # Testing if data is inserted into the table correctly
        self.db_manager.insert_data(self.df, self.table_name)
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        rows_count = cursor.fetchone()[0]
        self.assertEqual(rows_count, len(self.df))
        conn.close()

    def check_table_exists(self):
        # Testing if the table exists
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table_name}';")
        table_exists = cursor.fetchone() is not None
        conn.close()
        return table_exists

    def tearDown(self):
        self.db_manager.close_connection()

if __name__ == '__main__':
    unittest.main()