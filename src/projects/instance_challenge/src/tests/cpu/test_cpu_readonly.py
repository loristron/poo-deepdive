from classes.cpu import CPU
import pytest

class TestCPUReadOnly:

    cpu = CPU(name='Intel Core i9-9900K', manufacturer='Intel', total=100, allocated=20, cores=8, socket='AM4', power_watts=94)

    def test_readonly_cores(self):
        with pytest.raises(AttributeError) as at:
            self.cpu.cores = 10 
        assert at 

    def test_readonly_socket(self):
        with pytest.raises(AttributeError) as at:
            self.cpu.socket = 'AM5' 
        assert at 

    def test_readonly_power_watts(self):
        with pytest.raises(AttributeError) as at:
            self.cpu.socket = 110
        assert at 

    def test_category(self):
        assert True if self.cpu.cateogry == 'cpu' else False

