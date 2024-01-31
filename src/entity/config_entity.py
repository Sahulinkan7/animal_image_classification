from dataclasses import dataclass
import os,sys
from src.utils.commonutils import read_yaml
from src.constants import PARAMS_FILE_PATH

params : dict = read_yaml(PARAMS_FILE_PATH)

@dataclass
class TrainingPipelineConfig:
    root_dir = os.path.join("artifacts")

@dataclass
class DataIngestionConfig:
    root_dir = os.path.join(TrainingPipelineConfig.root_dir,"data_ingestion")
    data_source_url = f"https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"
    downloaded_data = os.path.join(root_dir,"downloaded_data","data.zip")
    extracted_data=os.path.join(root_dir,"extracted_data")
    
@dataclass
class PrepareBaseModelConfig:
    root_dir = os.path.join(TrainingPipelineConfig.root_dir,"prepare_base_model")
    base_model_filepath = os.path.join(root_dir,"prepared_base_model","basemodel.h5")
    updated_base_model_filepath = os.path.join(root_dir,"updated_base_model","updatedbasemodel.h5")
    params_image_size= params["IMAGE_SIZE"]
    params_learning_rate = params['LEARNING_RATE']
    params_include_top = params['INCLUDE_TOP']
    params_weights = params['WEIGHTS']
    params_classes=params['CLASSES']