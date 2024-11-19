class Resource:
    """Base class for resources
    """
    def __init__(self, name: str, 
                 manufacturer: str,
                 total: int, 
                 allocated: int) -> None:
        
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
    def manufacturer(self) -> str:
        """Manufacturer property

        Returns:
            str: Manufacturer name
        """
        return self._manufacturer

    @property
    def name(self) -> str:
        """Name property

        Returns:
            str: Resource name
        """
        return self._name 

    @property
    def total(self) -> int:
        """Total property

        Returns:
            int: Total resources in the pool
        """
        return self._total 
    
    @property
    def allocated(self) -> int:
        """Allocated property

        Returns:
            int: Amount of resources allocated into use
        """
        return self._allocated
    
    @property 
    def available(self) -> int:
        """Available property

        Returns:
            int: Difference between total and allocated. It's the available amount of itens to be allocated
        """
        return self.total - self.allocated 
    
    @property
    def cateogry(self) -> str:
        """Category property. Return the name of the class that the object were created from 

        Returns:
            str: Object original class name
        """
        return f"{str(type(self).__name__).lower()}"
    
    @staticmethod
    def _string_field_verification(value: str, field='Field') -> str:
        """Validates strings for different fields. Strings must be at least 2 char of lenght when stripped.

        Args:
            value (str): Value to be validated
            field (str, optional): Field to be declared into the message error. Defaults to 'Field'.

        Raises:
            TypeError: When a non-string object is provided
            ValueError: When the string does not match the class rules

        Returns:
            str: Stripped version of the original _value_
        """
        if not isinstance(value, str):
            raise TypeError(f'{str(field).strip().capitalize()} must be a string')
        if  len(value.strip()) < 2:
            raise ValueError(f'{str(field).strip().capitalize()} must be a valid string ')
        return value.strip()
    
    @staticmethod
    def _integer_field_verification(value: int, field="Field") -> int:
        """Validation mehtod for integer values. Values must be integers and greater than zero. 

        Args:
            value (int): Value to be ckecked    
            field (str, optional): Name of the field, to be used in error message. Defaults to "Field".

        Raises:
            TypeError: When a non-integer object is provided
            ValueError: When the integer value is not greater than zero

        Returns:
            int: returns the integer value 
        """
        if not isinstance(value, int):
            raise TypeError(f'{str(field).strip().capitalize()} must be a integer')
        if int(value) <= 0:
            raise ValueError(f'{str(field).strip().capitalize()} must be a greater than zero integer')
        return value 

    def claim(self, n: int) -> None:
        """Claim item from iventory pool

        Args:
            n (int): number of pieces to be claimed

        Raises:
            ValueError: Claimed value must be available in the inventory pool 
        """
        self._integer_field_verification(n, 'Claim')
        if n <= self.available:
            self._allocated += n
        else:
            raise ValueError('Claimed value must be available')
        
    def freeup(self, n: int) -> None:
        """Deallocate inventory and returns it to the ppol

        Args:
            n (int): number of itens to be freed

        Raises:
            ValueError: Number of itens to be freed must be less or equal the total allocated
        """
        n = self._integer_field_verification(n, 'Freeup')
        if n <= self.allocated:
            self._allocated -= n 
        else:
            raise ValueError("Free up value must be less or equal than the total allocated value")
        
    def died(self, n: int) -> None:
        """When we overuse a allocated component, it can die. Function reclaims itens out of allocation and out of inventory pool 

        Args:
            n (int): died value - number of items that died

        Raises:
            ValueError: Only used products can die. Died value must be less or equal than the total available
        """
        n = self._integer_field_verification(n, 'Died')
        if n <= self.allocated:
            self._allocated -= n 
            self._total -= n 
        else:
            raise ValueError('Died value must be less or equal than the total available')
    
    def purchased(self, n: int) -> None:
        """Add new n itens into the inventory pool

        Args:
            n (int): Amount of purchased items
        """
        n = self._integer_field_verification(n, 'Purchased')
        self._total += n