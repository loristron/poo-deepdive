from models.resource import Resource

class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
        super().__init__(name=name, manufacturer=manufacturer, total=total, allocated=allocated)
        self._cores = self._integer_field_verification(cores, 'Cores') 
        self._socket = self._string_field_verification(socket, 'Socket')
        self._power_watts = self._integer_field_verification(power_watts, 'Power Watts')

    def __str__(self) -> str:
        return super().__str__()
    
    def __repr__(self) -> str:
        return f"CPU(name={self.name}, manufacturer={self.manufacturer}, allocated={self.allocated}, cores={self.cores}, socket={self.socket}, power_watts={self.power_watts})"

    @property 
    def cores(self):
        """Cores property

        Returns:
            int: Return the name of the cores in CPU
        """
        return self._cores 
    
    @property
    def socket(self):
        """Socket property

        Returns:
            str: CPU Socket name
        """
        return self._socket 
    
    @property
    def power_watts(self):
        """Power Watts property

        Returns:
            int: CPU Power watts 
        """
        return self._power_watts