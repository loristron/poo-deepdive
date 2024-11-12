import pytest 
from models.storage import HDD, Storage
from models.resource import Resource

def test_sucess_create_hdd():
    hdd = HDD(name='Hard Disk Drive', manufacturer='Siemens', total=100, allocated=20, capacity_GB=220, size='2.5"', rpm=7000)
    assert True if isinstance(hdd, HDD) and isinstance(hdd, Storage) and isinstance(hdd, Resource) else False 

def test_create_value_error_capacity():
    with pytest.raises(ValueError) as ve:
        hdd = HDD(name='Hard Disk Drive', manufacturer='Siemens', total=100, allocated=20, capacity_GB=-20, size='2.5"', rpm=7000)
    assert ve

def test_create_type_error_capacity():
    with pytest.raises(TypeError) as te:
        hdd = HDD(name='Hard Disk Drive', manufacturer='Siemens', total=100, allocated=20, capacity_GB='x', size='2.5"', rpm=7000)
    assert te

def test_create_value_error_size():
    pass #TODO 

def test_create_type_error_size():
    pass #TODO

def test_create_value_error_rpm():
    with pytest.raises(ValueError) as ve:
        hdd = HDD(name='Hard Disk Drive', manufacturer='Siemens', total=100, allocated=20, capacity_GB=20, size='2.5"', rpm=0)
    assert ve

def test_create_type_error_rpm():
    with pytest.raises(TypeError) as te:
        hdd = HDD(name='Hard Disk Drive', manufacturer='Siemens', total=100, allocated=20, capacity_GB=200, size='2.5"', rpm='x')
    assert te