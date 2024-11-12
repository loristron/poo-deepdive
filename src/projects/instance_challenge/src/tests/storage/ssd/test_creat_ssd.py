from models.resource import Resource
from models.storage import Storage, SSD
import pytest

def test_create_sucess_ssd():
    ssd = SSD(name='Solid System Disk', manufacturer='Intel', total=100, allocated=10, capacity_GB=220, interface='PCIe')
    assert True if isinstance(ssd, SSD) and isinstance(ssd, Storage) and isinstance(ssd, Resource) else False

def test_create_ssd_value_error_interface():
    with pytest.raises(ValueError) as ve:
        ssd = SSD(name='Solid System Disk', manufacturer='Intel', total=100, allocated=10, capacity_GB=220, interface='x')
    assert ve

def test_create_ssd_type_error_interface():
    with pytest.raises(TypeError) as te:
        ssd = SSD(name='Solid System Disk', manufacturer='Intel', total=100, allocated=10, capacity_GB=220, interface=0)
    assert te

