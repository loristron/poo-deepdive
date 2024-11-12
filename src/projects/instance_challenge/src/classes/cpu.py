from classes.resource import Resource

class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
        super().__init__(name=name, manufacturer=manufacturer, total=total, allocated=allocated)
        self._cores = self._integer_field_verification(cores, 'Cores') 
        self._socket = self._string_field_verification(socket, 'Socket')
        self._power_watts = self._integer_field_verification(power_watts, 'Power Watts')

    @property 
    def cores(self):
        return self._cores 
    
    @property
    def socket(self):
        return self._socket 
    
    @property
    def power_watts(self):
        return self._power_watts