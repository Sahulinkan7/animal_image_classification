from dataclasses import dataclass
import os,sys

@dataclass
class TrainingPipelineConfig:
    root_dir = os.path.join("artifacts")

@dataclass
class DataIngestionConfig:
    root_dir = os.path.join(TrainingPipelineConfig.root_dir,"DataIngestion")
    data_source_url = f"https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"
    downloaded_data = os.path.join("downloaded_data","data.zip")
    extracted_data=os.path.join("extracted_data")
    