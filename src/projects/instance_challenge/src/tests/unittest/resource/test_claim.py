from models.resource import Resource
import pytest

class TestClaim():

    r = Resource('Intel Core i9-9900K', 'Intel', 50, allocated=10)

    def test_success_claim(self):
        self.r.claim(10)
        assert self.r.available == 30 and self.r.allocated == 20 

    def test_failed_claim(self):
        with pytest.raises(ValueError) as ve: 
            self.r.claim(31)
        assert(ve)

    def test_invalid_type_claim(self):
        with pytest.raises(TypeError) as tr:
            self.r.claim('r')
        assert tr 