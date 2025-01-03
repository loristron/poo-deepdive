from models.part_2.IntegerField import IntegerField
from models.part_2.CharField import CharField

class Person:
    age = IntegerField(min_=0, max_=199)
    name = CharField(min_=3, max_=50)
