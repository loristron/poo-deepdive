from models.cpu import CPU
from models.resource import Resource
import pytest

def test_success_creation():
    cpu = CPU(name='Intel Core i9-9900K', manufacturer='Intel', total=100, allocated=20, cores=8, socket='AM4', power_watts=94)
    assert True if isinstance(cpu, CPU) and isinstance(cpu, Resource) else False

def test_cpu_type_error_cores():
    with pytest.raises(TypeError) as ve:
        cpu = CPU(name='Intel Core i9-9900K', manufacturer='Intel', total=100, allocated=20, cores='a', socket='AM4', power_watts=94)
    assert ve 

def test_cpu_type_error_socket():
    with pytest.raises(TypeError) as ve:
        cpu = CPU(name='Intel Core i9-9900K', manufacturer='Intel', total=100, allocated=20, cores=8, socket=5, power_watts=94)
    assert ve 

def test_cpu_type_error_power_watts():
    with pytest.raises(TypeError) as ve:
        cpu = CPU(name='Intel Core i9-9900K', manufacturer='Intel', total=100, allocated=20, cores=8, socket='AM4', power_watts='TEST')
    assert ve 

def test_cpu_value_error_cores():
    with pytest.raises(ValueError) as ve:
        cpu = CPU(name='Intel Core i9-9900K', manufacturer='Intel', total=100, allocated=20, cores=0, socket='AM4', power_watts=94)
    assert ve 

def test_cpu_value_error_socket():
    with pytest.raises(ValueError) as ve:
        cpu = CPU(name='Intel Core i9-9900K', manufacturer='Intel', total=100, allocated=20, cores=8, socket='g', power_watts=94)
    assert ve 

def test_cpu_value_error_power_watts():
    with pytest.raises(ValueError) as ve:
        cpu = CPU(name='Intel Core i9-9900K', manufacturer='Intel', total=100, allocated=20, cores=8, socket='AM4', power_watts=0)
    assert ve 
