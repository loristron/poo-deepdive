import numbers

class IntegerField:
    def __init__(self, min=None, max=None):
        self._min = min 
        self._max = max 

    @property
    def min(self):
        return self._min 
    
    @property
    def max(self):
        return self._max 

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer value')
        
        if self.min is not None and value < self.min:
            raise ValueError(f'{self.prop_name} must be an integral greater than {self.min}')
        
        if self.max is not None and value > self.max:
            raise ValueError(f'{self.prop_name} must be an Integer value smaller or equal {self.max}')
        
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self 
        return instance.__dict__.get(self.prop_name, None)
