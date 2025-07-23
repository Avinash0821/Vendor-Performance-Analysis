import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Logging configuration
logging.basicConfig(
    filename='C:\\Users\\AVINASH\\data\\logs\\ingestion_db.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

# Database engine (SQLite in this case)
engine = create_engine('sqlite:///inventory.db')

# Function to ingest a DataFrame into a database table
def ingest_db(df, table_name, engine):
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f'Successfully ingested table: {table_name}')
    except Exception as e:
        logging.error(f'Failed to ingest table {table_name}. Error: {str(e)}')

# Function to load all CSVs in a folder and ingest into database
def load_raw_data():
    start = time.time()
    data_dir = 'C:\\Users\\AVINASH\\data'
    
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            try:
                file_path = os.path.join(data_dir, file)
                df = pd.read_csv(file_path)
                table_name = os.path.splitext(file)[0]
                
                logging.info(f'Ingesting {file} into DB as table "{table_name}"')
                ingest_db(df, table_name, engine)
            except Exception as e:
                logging.error(f'Failed to process file {file}. Error: {str(e)}')

    end = time.time()
    total_time = (end - start) / 60
    logging.info('----------Ingestion Complete------------')
    logging.info(f'Total Time Taken: {total_time:.2f} minutes')

# Main guard
if __name__ == '__main__':
    load_raw_data()
