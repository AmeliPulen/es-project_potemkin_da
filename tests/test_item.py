"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def item():
    item1 = Item("Dildo", 5000, 3)
    return item1

def test_calculate_total_price(item):
    # Проверить рассчитывается ли количество
    assert item.calculate_total_price() == 15000

def test_apply_discount(item):
    # Проверить рассчитывается ли скидка
    Item.pay_rate = 0.5
    item.apply_discount()

    assert item.price == 2500

def test_private():
    # Проверить заприватился ли атрибут
    item.name = 'VibroDildo'
    assert item.name == 'VibroDildo'


def test_name_length():
    # Проверить уменьшилась ли длина названия
    item.name = 'Sex Doll Ann'
    assert item.name == 'Sex Doll A'

def test_item_quantity():
    # Проверить количество экземпляров класса созданных из csv файла
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_strun_to_number():
    # Проверить различные типы данных в методе string_to_number
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('6.0') == 6
    assert Item.string_to_number('6.5') == 6

def test_repr():
    # Проверить правильность вызова магического метода __repr__
    assert repr(item) == "Item('VibroDildo', 2500.0, 3)"

def test_str():
    # Проверить правильность вызова магического метода __str__
    assert str(item) == 'VibroDildo'