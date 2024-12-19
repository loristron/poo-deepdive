from models.resource import Resource
import pytest

class TestClaim():

    r = Resource('Intel Core i9-9900K', 'Intel', 50, allocated=10)

    def test_read_only_name(self):
        with pytest.raises(AttributeError) as at:
            self.r.name = 'Name'
        assert at

    def test_read_only_manufacturer(self):
        with pytest.raises(AttributeError) as at:
            self.r.manufacturer = 'Name'
        assert at 
    
    def test_read_only_total(self):
        with pytest.raises(AttributeError) as at:
            self.r.total = 10 
        assert at 

    def test_read_only_allocated(self):
        with pytest.raises(AttributeError) as at:
            self.r.allocated = 10 
        assert at 

    def test_read_only_available(self):
        with pytest.raises(AttributeError) as at:
            self.r.available = 10 
        assert at 

    def test_read_only_category(self):
        with pytest.raises(AttributeError) as at:
            self.r.cateogry = 'teste'
        assert at 
        
    def test_category(self):
        assert True if self.r.cateogry == 'resource' else False