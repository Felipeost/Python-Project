import logging
import pandas as pd

class ProcessData:
    """Processing data: removing unwanted columns, converting numeric values, and standardizing text values."""
    
    def process_data(self, df):
        """
            Process the input DataFrame by removing unwanted columns, converting numeric values, 
            and standardizing text values.
            :param df: The input dataframe to process
        """
        try:
            # Step 1: Remove unwanted columns
            columns_to_remove = ['New_Price', 'Mileage', 'Seats', 'Owner_Type']
            df = df.drop(columns=columns_to_remove, errors='ignore')
            if 'Unnamed: 0' in df.columns:
                df = df.drop(columns='Unnamed: 0')

            # Step 2: Convert numeric columns
            df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')
            df['Kilometers_Driven'] = pd.to_numeric(df['Kilometers_Driven'], errors='coerce').astype('Int64') 
            df['Engine'] = df['Engine'].str.extract('([0-9]+)').astype('Int64')
            df['Power'] = df['Power'].str.extract('([0-9.]+)').astype(float)

            # Step 3: Standardize text columns
            df['Fuel_Type'] = df['Fuel_Type'].str.upper()
            df['Transmission'] = df['Transmission'].str.upper()
            df['Name'] = df['Name'].str.upper()
            df['Location'] = df['Location'].str.upper()

            logging.info("Successfully processed data.")
            return df
        except Exception as e:
            logging.error(f"Error when processing data: {e}")
            raise