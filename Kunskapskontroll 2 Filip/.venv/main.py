import logging

from load_data import LoadData
from process_data import ProcessData
from sql_table_manager import SqlTableManager

# Logging configuration
logging.basicConfig(filename="process_log.log", level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M')

file_path = "car-data.csv"

# Step 1: Load the data
loader = LoadData()
df = loader.load_data(file_path)
    
# Step 2: Process the data
processor = ProcessData()
processed_df = processor.process_data(df)
    
# Step 3: Create table if not already existing and insert the processed data into the table
db_handler = SqlTableManager("car_data.db")
db_car_table = db_handler.create_table("cars")
db_car_data = db_handler.insert_data(processed_df, "cars")

# Step 4: Give user feedback by printing finshed message
print("Car data processed and loaded into table.")