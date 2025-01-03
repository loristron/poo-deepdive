from models.part_1.IntegerField import IntegerField
from models.part_1.CharField import CharField

class Person:
    age = IntegerField(min=0, max=199)
    name = CharField(min=3, max=50)
