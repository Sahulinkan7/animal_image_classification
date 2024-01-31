from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import PrepareBaseModelConfig
import os,sys

class PrepareBaseModel:
    def __init__(self,prepare_base_model_config: PrepareBaseModelConfig):
        try:
            self.prepare_base_model_config = prepare_base_model_config
        except Exception as e:
            logging.error(f"Prepare base model object inititation interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def get_base_model(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)