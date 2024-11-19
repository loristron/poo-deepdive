from models.resource import Resource
import pytest  

def test_invalid_name_creation():
    with pytest.raises(ValueError) as ve:
        r = Resource(name='A', manufacturer='Del', total=30, allocated=20)
    assert(ve)

def test_invalid_manufacturer_creation():
    with pytest.raises(TypeError) as ve:
        r = Resource(name='CDROM', manufacturer=3.15, total=30, allocated=20)
    assert(ve)

def test_invalid_total_type_creation():
    with pytest.raises(TypeError) as ve:
        r = Resource(name='CDROM', manufacturer='Del', total=30.5, allocated=20)
    assert(ve)

def test_invalid_allocated_type_creation():
    with pytest.raises(TypeError) as ve:
        r = Resource(name='CDROM', manufacturer='Del', total=30, allocated=20.8)
    assert(ve)

def test_invalid_total_creation():
    with pytest.raises(ValueError) as ve:
        r = Resource(name='CDROM', manufacturer='Del', total=10, allocated=25)
    assert(ve)

def test_sucess_resource_creation():
    r = Resource(name='CPU', manufacturer='Del', total=30, allocated=20)
    assert True if isinstance(r, Resource) else False