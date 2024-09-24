import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from process_data import ProcessData

class TestProcessData(unittest.TestCase):

    def setUp(self):
        # Setup test dataframe
        data = {
            "Year": [2010, 2015],
            "Kilometers_Driven": ["30000", "50000"],
            "Engine": ["1200cc", "1500cc"],
            "Power": ["85 bhp", "100 bhp"],
            "Fuel_Type": ["Petrol", "Diesel"],
            "Transmission": ["Manual", "Automatic"],
            "Name": ["CarA", "CarB"],
            "Location": ["CityA", "CityB"],
            "Owner_Type": ["first", "second"],
            "Seats": ["2", "4"]
        }
        self.df = pd.DataFrame(data)
        self.processor = ProcessData()

    def test_process_data(self):
        # Test if the correct columns are still in the dataframe, also that the other have been removed.
        processed_df = self.processor.process_data(self.df)
        self.assertIn("Year", processed_df.columns)
        self.assertIn("Kilometers_Driven", processed_df.columns)
        self.assertNotIn("Owner_Type", processed_df.columns)
        self.assertNotIn("Seats", processed_df.columns)

        # Test that the different types are correct after processing
        self.assertEqual(processed_df['Year'].dtype, 'Int64')
        self.assertEqual(processed_df['Kilometers_Driven'].dtype, 'Int64')
        self.assertTrue(processed_df['Name'].str.isupper().all())

if __name__ == '__main__':
    unittest.main()