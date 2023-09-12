"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


item1 = Item("Dildo", 5000, 3)
item2 = Item("Doll", 20000, 7)

# Проверить записались ли данные
assert Item.all != None

# Проверить рассчитывается ли количество
assert item1.calculate_total_price() == 15000
assert item2.calculate_total_price() == 140000

# Проверить рассчитывается ли скидка
Item.pay_rate = 0.5
item1.apply_discount()
item2.apply_discount()

assert item1.price == 2500
assert item2.price == 10000


# Проверить заприватился ли атрибут
item1.name = 'VibroDildo'
assert item1.name == 'VibroDildo'

# Проверить уменьшилась ли длина названия
item2.name = 'Sex Doll Ann'
assert item2.name == 'Sex Doll A'

# Проверить количество экземпляров класса созданных из csv файла
Item.instantiate_from_csv()
assert len(Item.all) == 5

# Проверить различные типы данных в методе string_to_number
assert Item.string_to_number('6') == 6
assert Item.string_to_number('6.0') == 6
assert Item.string_to_number('6.5') == 6

# Проверить правильность вызова магического метода __repr__
assert repr(item1) == "Item('VibroDildo', 2500.0, 3)"

# Проверить правильность вызова магического метода __str__
assert str(item1) == 'VibroDildo'