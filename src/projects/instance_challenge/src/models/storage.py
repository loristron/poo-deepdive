from models.resource import Resource

class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name=name, manufacturer=manufacturer, total=total, allocated=allocated)
        self._capacity_GB = self._integer_field_verification(capacity_GB, 'Capacity GB')

    @property
    def capacity_GB(self):
        return self._capacity_GB
    
class HDD(Storage):

    valid_sizes = ['2.5"', '3.5"']

    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._size = self.valid_sizes(size)
        self._rpm = self._integer_field_verification(rpm, 'RPM') 

    def validate_size_field(self, value):
        value = self._string_field_verification(value)
        if value not in HDD.valid_sizes:
            raise ValueError('Size must be 2.5" or 3.5"')
        return value 
    
    @property
    def size(self):
        return self._size 
    
    @property
    def rpm(self):
        return self.rpm 
    
class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._interface = self._string_field_verification(interface, 'Interface')

    @property
    def interface(self):
        return self._interface