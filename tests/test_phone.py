import pytest
from src.phone import Phone


@pytest.fixture()
def phone():
    phone1 = Phone("DildoPhone", 300, 5, 2)
    return phone1
def test_number_of_sim(phone):
    assert phone.number_of_sim == 2

def test_set_number_of_sim(phone):
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

def test_set_invalid_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = -1

def test_repr(phone):
    assert repr(phone) == "Phone('DildoPhone', 300, 5, 2)"

def test_str(phone):
    assert str(phone) == "DildoPhone"

def test_add_phones(phone):
    phone2 = Phone("Samsung", 799, 5, 1)
    total_quantity = phone + phone2
    assert total_quantity == 10

