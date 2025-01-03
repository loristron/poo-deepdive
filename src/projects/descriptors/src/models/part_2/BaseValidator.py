class BaseValidator:
    
    def __init__(self, min_=None, max_=None):
        self._min = min_
        self._max = max_
    
    @property
    def min_(self):
        return self._min
    
    @property
    def max_(self):
        return self._max 
    
    @property
    def type_(self):
        return self.type_
    
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def validate(self, value):
        # This needs to be implemented specifically by each child
        pass 

    def __set__(self, instance, value):
       self.validate(value)
       instance.__dict__[self.prop_name] = value
            

        

