class Resource:
    def __init__(self, name: str, 
                 manufacturer: str,
                 total: int, 
                 allocated: int):
        
        self._name = self._string_field_verification(name, 'Resource name')
        self._manufacturer = self._string_field_verification(manufacturer, 'manufacturer')
        
        if total >= allocated:
            self._total = self._integer_field_verification(total, 'Total') 
            self._allocated = self._integer_field_verification(allocated, 'allocated')
        else:
            raise ValueError('Total inventory must be greater than allocated') 
        
    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return f"Resource(name={self.name}, manufacturer={self.manufacturer}, total={self.total}, allocated={self.allocated})"

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def name(self):
        return self._name 

    @property
    def total(self):
        return self._total 
    
    @property
    def allocated(self):
        return self._allocated
    
    @property 
    def available(self):
        return self.total - self.allocated 
    
    @property
    def cateogry(self):
        return f"{str(self.__class__.__name__).lower()}"
    
    @staticmethod
    def _string_field_verification(value, field='Field'):
        if not isinstance(value, str):
            raise TypeError(f'{str(field).strip().capitalize()} must be a string')
        if  len(value.strip()) < 2:
            raise ValueError(f'{str(field).strip().capitalize()} must be a valid string ')
        return value.strip()
    
    @staticmethod
    def _integer_field_verification(value, field):
        if not isinstance(value, int):
            raise TypeError(f'{str(field).strip().capitalize()} must be a integer')
        if int(value) <= 0:
            raise ValueError(f'{str(field).strip().capitalize()} must be a greater than zero integer')
        return value 

    def claim(self, n: int) -> None:
        self._integer_field_verification(n, 'Claim')
        if n <= self.available:
            self._allocated += n
        else:
            raise ValueError('Claimed value must be available')
        
    def freeup(self, n):
        self._integer_field_verification(n, 'Freeup')
        if n <= self.allocated:
            self._allocated -= n 
        else:
            raise ValueError("Free up value must be less or equal than the total allocated value")
        
    def died(self, n):
        self._integer_field_verification(n, 'Died')
        if n <= self.allocated:
            self._allocated -= n 
            self._total -= n 
        else:
            raise ValueError('Died value must be less or equal than the total available')
    
    def purchased(self, n):
        self._integer_field_verification(n, 'Purchased')
        self._total += n