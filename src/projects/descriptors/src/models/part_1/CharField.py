
class CharField:
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
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be an string')
        
        if self.min is not None and len(value.strip()) < self.min:
            raise ValueError(f'{self.prop_name} must be at least {self.min} characters long')
        
        if self.max is not None and len(value.strip()) > self.max:
            raise ValueError(f'{self.prop_name} must be have a limit of {self.max} characters')
        
        instance.__dict__[self.prop_name] = value.strip()

    def __get__(self, instance, owner_class):
        if instance is None:
            return self 
        else:
            return instance.__dict__.get(self.prop_name, None)