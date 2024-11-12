from classes.resource import Resource

class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name=name, manufacturer=manufacturer, total=total, allocated=allocated)
        self._capacity_GB = self._integer_field_verification(capacity_GB, 'Capacity GB')

    @property
    def capacity_GB(self):
        return self._capacity_GB
    
class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._size = size #TODO: 
        self._rpm = self._integer_field_verification(rpm, 'RPM') 

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