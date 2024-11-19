from models.resource import Resource

class Storage(Resource):
    """Base class for storage units. Inherits from Resource base class 
    """
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name=name, manufacturer=manufacturer, total=total, allocated=allocated)
        self._capacity_GB = self._integer_field_verification(capacity_GB, 'Capacity GB')

    @property
    def capacity_GB(self) -> int:
        """Capacity, in GB, Property 

        Returns:
            int: GB Storage capacity
        """
        return self._capacity_GB
    
class HDD(Storage):
    """Base class for HDD Items. Inherits from Storage"""

    valid_sizes = ['2.5"', '3.5"']

    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._size = self.validate_size_field(size)
        self._rpm = self._integer_field_verification(rpm, 'RPM') 

    def validate_size_field(self, value: str) -> str:
        """Check if the value field provided is inside valid sizes

        Args:
            value (str): Input value

        Raises:
            ValueError: If the size provided is not in valid sizes accepted

        Returns:
            str: Stripped version of value arg
        """
        value = self._string_field_verification(value)
        if value not in HDD.valid_sizes:
            raise ValueError('Size must be 2.5" or 3.5"')
        return value.strip() 
    
    @property
    def size(self) -> str:
        """Size field Property. Size must be between valid sizes 

        Returns:
            str: Valid size 
        """
        return self._size 
    
    @property
    def rpm(self) -> int:
        """RPM (rotations per minute) property

        Returns:
            int: HDD Rotations per minute value
        """
        return self.rpm 
    
class SSD(Storage):
    """Base class for SSD item, inherits from Storage"""
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._interface = self._string_field_verification(interface, 'Interface')

    @property
    def interface(self) -> str:
        """Interface property

        Returns:
            str: Interface name
        """
        return self._interface