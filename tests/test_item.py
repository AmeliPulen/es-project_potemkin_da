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