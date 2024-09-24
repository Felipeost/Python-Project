import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from load_data import LoadData

class TestLoadData(unittest.TestCase):

    def setUp(self):
        self.loader = LoadData()
        self.file_path = "tests\\test_data.csv"

    def test_load_data(self):
        # Loading test data
        df = self.loader.load_data(self.file_path)

        # Checking that the output is a dataframe that is not empty
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)

if __name__ == '__main__':
    unittest.main()