from models.resource import Resource
import pytest

class TestDied():

    r = Resource('Intel Core i9-9900K', 'Intel', 50, allocated=10)

    def test_died_sucess(self):
        self.r.died(10)
        assert self.r.total == 40 and self.r.allocated == 0 and self.r.available == 40

    def test_died_value_error(self):
        with pytest.raises(ValueError) as ve:
            self.r.died(100)
        assert(ve) 

    def test_died_type_error(self):
        with pytest.raises(TypeError) as te:
            self.r.died('n')
        assert(te)


