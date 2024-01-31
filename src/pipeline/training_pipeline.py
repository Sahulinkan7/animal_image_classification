from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig

diconfig=DataIngestionConfig()

dt=DataIngestion(data_ingestion_config=diconfig)
downloaded_path =dt.download_data()
unzipped_path = dt.extract_downloaded_data(downloaded_path)

print(unzipped_path)