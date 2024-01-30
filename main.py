
import os,sys
from src.exception import CustomException
from src.logger import logging
from src.utils.commonutils import read_yaml,write_yaml

try:
    content = read_yaml('abc.yaml')
    print(content)
except Exception as e:
    logging.error(f"{CustomException(e,sys)}")
    print(CustomException(e,sys))
    raise CustomException(e,sys)