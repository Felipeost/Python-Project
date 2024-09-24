import logging
import pandas as pd

class LoadData:
    """Reading CSV file and returning DataFrame."""
    def load_data(self, file_path):
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)
            logging.info(f"Successfully reading data from {file_path}")
            return df
        except Exception as e:
            logging.error(f"Error when reading data from {file_path}: {e}")
            raise
