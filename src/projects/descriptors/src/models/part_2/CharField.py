from models.part_2.BaseValidator import BaseValidator

class CharField(BaseValidator):
    def __init__(self, min_=None, max_=None):
        super().__init__(min_, max_)

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string')
        if self._min is not None and value < self._min:
            raise ValueError(f'{self.prop_name} must be greater than {self._min}')
        if self._max is not None and value > self._max:
            raise ValueError(f'{self.prop_name} must me less than {self._max} characters long')