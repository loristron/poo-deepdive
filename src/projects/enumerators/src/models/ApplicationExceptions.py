import enum 

@enum.unique
class ApplicationExceptions(enum.Enum):

    def __new__(cls, member_value, member_error, member_message):
        member = object.__new__(cls)
        member._value_ = member_value
        member.error = member_error
        member.message = member_message
        return member

    NotAnInteger = 100, ValueError, 'Value is not an integer'
    Timeout = 500, TimeoutError, 'Timeout reached'

    def throw(self, custom_message=None):
        custom_message = custom_message or self.message
        raise self.error(custom_message)
    
    @property
    def code(self):
        return self.value