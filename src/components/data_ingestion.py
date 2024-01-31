from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig
import os,sys
from urllib import request

class DataIngestion:
    def __init__(self,data_ingestion_config : DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            os.makedirs(self.data_ingestion_config.root_dir,exist_ok=True)
            
        except Exception as e:
            logging.error(f"Data Ingestion component initiation Interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def download_data(self):
        try:
            logging.info(f"Starting data downloading from source")
            os.makedirs(self.data_ingestion_config.downloaded_data,exist_ok=True)
            if not os.path.exists(self.data_ingestion_config.downloaded_data):
                request.urlretrieve(
                    url=self.data_ingestion_config.data_source_url,
                    filename=self.data_ingestion_config.downloaded_data
                )
            else:
                logging.info(f"File already exists of size {os.path.getsize(self.data_ingestion_config.downloaded_data)}")
        except Exception as e:
            logging.error(f"Data downloading from source interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        