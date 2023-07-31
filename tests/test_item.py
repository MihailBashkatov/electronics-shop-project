"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item = Item('toy', 10.5, 3)
    assert item.calculate_total_price() == 31.5
    assert type(item.calculate_total_price()) == float

def test_apply_discount():
    item = Item('toy', 10, 3)
    Item.pay_rate = 0.7
    assert item.apply_discount() == 7
    assert type(item.calculate_total_price()) == float

