from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig
import os,sys
from urllib import request
from pathlib import Path
from zipfile import ZipFile

class DataIngestion:
    def __init__(self,data_ingestion_config : DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            os.makedirs(self.data_ingestion_config.root_dir,exist_ok=True)
            
        except Exception as e:
            logging.error(f"Data Ingestion component initiation Interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def download_data(self) -> Path:
        try:
            logging.info(f"Starting data downloading from source")
            os.makedirs(os.path.dirname(self.data_ingestion_config.downloaded_data),exist_ok=True)
            if not os.path.exists(self.data_ingestion_config.downloaded_data):
                request.urlretrieve(
                    url=self.data_ingestion_config.data_source_url,
                    filename=self.data_ingestion_config.downloaded_data
                )
                logging.info(f"data downloaded successfully of size {os.path.getsize(self.data_ingestion_config.downloaded_data)}!")
            else:
                logging.info(f"File already exists of size {os.path.getsize(self.data_ingestion_config.downloaded_data)/(1024*1024)} MB")
            return self.data_ingestion_config.downloaded_data
        
        except Exception as e:
            logging.error(f"Data downloading from source interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def extract_downloaded_data(self,downloaded_data_filepath):
        try:
            logging.info(f"Starting Extraction of zipped downloaded data from {downloaded_data_filepath}")
            downloaded_data = self.data_ingestion_config.downloaded_data
            os.makedirs(self.data_ingestion_config.extracted_data)
            
            unzip_dir = self.data_ingestion_config.extracted_data
            with ZipFile(downloaded_data,'r') as ziprefernce:
                ziprefernce.extractall(unzip_dir)
                logging.info(f"Downloaded data got extracted to the filepath {unzip_dir}")
                
            return unzip_dir
        except Exception as e:
            logging.error(f"Extracting downloaded data Interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        