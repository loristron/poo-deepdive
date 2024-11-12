from models.resource import Resource
import pytest

class TestPurchased():

    r = Resource('Intel Core i9-9900K', 'Intel', 50, allocated=10)

    def test_purchase_sucess(self):
        self.r.purchased(10)
        assert self.r.total == 60 and self.r.available == 50

    def test_purchase_value_error(self):
        with pytest.raises(ValueError) as ve:
            self.r.purchased(0)
        assert(ve)

    def test_purchase_type_error(self):
        with pytest.raises(TypeError) as te:
            self.r.purchased('n')
        assert(te)
        
    

