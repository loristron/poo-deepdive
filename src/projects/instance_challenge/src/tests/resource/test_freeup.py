from classes.resource import Resource
import pytest

class TestFreeup():

    r = Resource('Intel Core i9-9900K', 'Intel', 50, allocated=10)

    def test_sucess_freeup(self):
        self.r.freeup(10)
        assert self.r.allocated == 0 and self.r.available == 50 

    def test_value_error_freeup(self):
        with pytest.raises(ValueError) as ve:
            self.r.freeup(30)
        assert ve

    def test_type_error_freeup(self):
        with pytest.raises(TypeError) as te:
            self.r.freeup('n')
        assert te
