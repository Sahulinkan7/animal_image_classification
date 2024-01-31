from dataclasses import dataclass
import os,sys

@dataclass
class TrainingPipelineConfig:
    root_dir = os.path.join("artifacts")

@dataclass
class DataIngestionConfig:
    root_dir = os.path.join(TrainingPipelineConfig.root_dir,"DataIngestion")
    