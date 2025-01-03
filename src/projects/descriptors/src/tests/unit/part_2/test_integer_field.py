import pytest
from models.part_2.Person import Person
from models.part_2.IntegerField import IntegerField

@pytest.fixture
def person():
    return Person()

def test_set_age_decimal_fail(person):
    with pytest.raises(ValueError):
        person.age = 10.0

def test_set_age_negative_value(person):
    with pytest.raises(ValueError):
        person.age = -3

def test_set_age_over_bound(person):
    with pytest.raises(ValueError):
        person.age = 200

def test_set_person_age_success(person):
    person.age = 10 
    assert True if person.age == 10 else False

def test_instance_age_sucess(person):
    person.age = 10 
    assert True if isinstance(type(person).age, IntegerField) else False
