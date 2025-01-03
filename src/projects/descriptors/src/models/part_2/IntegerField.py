from models.part_2.BaseValidator import BaseValidator
import numbers

class IntegerField(BaseValidator):

    def __init__(self, min_=None, max_=None):
        super().__init__(min_, max_)
    
    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer')
        
        if self._min is not None and value < self._min:
            raise ValueError(f'{self.prop_name} must be greater than {self.min_}')
        
        if self._max is not None and value > self._max:
            raise ValueError(f'{self.prop_name} must be less than {self.max_}')
        
