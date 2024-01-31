from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionArtifact:
    downloaded_data_filepath : Path
    extracted_data_filepath : Path


@dataclass
class PrepareBaeModelArtifact:
    base_model_filepath : Path
    updated_base_model_filepath : Path