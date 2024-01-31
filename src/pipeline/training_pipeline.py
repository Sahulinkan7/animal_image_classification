from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig

diconfig=DataIngestionConfig()

dt=DataIngestion(data_ingestion_config=diconfig)
data_ingestion_artifacts = dt.initiate_data_ingestion()
print(data_ingestion_artifacts)