import pytest
from models.part_1.Person import Person
from models.part_1.CharField import CharField

@pytest.fixture
def person():
    return Person()

def test_name_not_string(person):
    with pytest.raises(ValueError):
        person.name = 10

def test_name_smaller(person):
    with pytest.raises(ValueError):
        person.name = 'a'

def test_name_greater(person):
    with pytest.raises(ValueError):
        person.name = 'a'*60

def test_name_success(person):
    person.name = 'Lorena'
    assert True if person.name == 'Lorena' else False

def test_type_name_instance(person):
    person.name = 'Lorena'
    assert True if isinstance(type(person).name, CharField) else False