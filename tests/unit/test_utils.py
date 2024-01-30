from src.utils.commonutils import read_yaml
from pathlib import Path
import pytest
from src.exception import CustomException

datafiles=[
    'tests/data/abc.yaml',
    'tests/data/abc2.yaml'
]

def test_read_yaml_empty():
    with pytest.raises(CustomException):
       read_yaml(datafiles[0])
       
def test_read_yaml():
    response = read_yaml(datafiles[1])
    assert isinstance(response,dict)
    
# class approach

class Test_read_yaml:
    datafiles=[
    'tests/data/abc.yaml',
    'tests/data/abc2.yaml'
    ]
    def test_read_yaml_empty(self):
        with pytest.raises(CustomException):
            read_yaml(self.datafiles[0])
       
    def test_read_yaml(self):
        response = read_yaml(self.datafiles[1])
        assert isinstance(response,dict)