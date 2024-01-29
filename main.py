x=3
y=5
import os,sys
from src.exception import CustomException
from src.logger import logging
from src.utils.commonutils import read_yaml,write_yaml

try:
    print(x/y)
    logging.info(f"result is {x/y}")
    content = read_yaml('design.yaml')
    write_yaml(os.path.join("test.yaml"),content=content)
    write_yaml(os.path.join("datavalidation","report.yaml"),content={'name':'linkan3343'})
    print(content)
except Exception as e:
    logging.error(f"{CustomException(e,sys)}")
    print(CustomException(e,sys))
    raise CustomException(e,sys)