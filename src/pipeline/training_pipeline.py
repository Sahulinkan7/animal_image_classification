from src.components.data_ingestion import DataIngestion
from src.components.prepare_basemodel import PrepareBaseModel

from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import PrepareBaseModelConfig

# diconfig=DataIngestionConfig()

# dt=DataIngestion(data_ingestion_config=diconfig)
# data_ingestion_artifacts = dt.initiate_data_ingestion()
# print(data_ingestion_artifacts)


pr = PrepareBaseModel(prepare_base_model_config=PrepareBaseModelConfig())
